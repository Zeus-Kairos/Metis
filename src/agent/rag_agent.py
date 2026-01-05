from dataclasses import dataclass
import json
import logging
import os
from re import search
from typing import Annotated, Any, Dict, Generator, List, Tuple, TypedDict

from langchain.tools import InjectedToolCallId, ToolRuntime, tool
from langchain_core.documents import Document
from langchain_core.messages import AIMessage, SystemMessage, ToolMessage
from langchain.agents import create_agent
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.types import Command
from psycopg_pool import base

from src.memory.memory import MemoryManager 
from src.memory.thread import ThreadManager
from src.agent.prompts import (
    classify_intent_prompt,
    complement_answer_prompt,
    deep_rag_prompt,
    filter_documents_prompt,
    format_answer_prompt,
    handle_chat_prompt,
    plan_rag_prompt,
    refine_query_prompt,
    reference_check_prompt,
    review_answer_prompt,
)
from src.rag.rag_flow import RAGFlow, RAGType
from src.agent.llm import LLMRunner
from src.agent.api_llm import get_api_llm_runner
from src.agent.tools import list_children_tool, rag_search_tool
from src.utils.paths import get_index_path, get_upload_dir

logger = logging.getLogger(__name__)

@dataclass
class KnowledgeBaseItem:
    """
    Represents an item in the knowledge base index.
    """
    id: int
    name: str
    root_path: str
    index_path: str
    description: str

class AgentState(TypedDict):
    """
    State of the agent.
    """
    query: str
    messages: Annotated[List[Dict[str, str]], add_messages]
    intent: str = None
    refined_query: str = None   
    documents: list[Document] | List[Tuple[Document, float]] = None
    answer: str = None
    error_context: str = None
    knowledge_base_item: KnowledgeBaseItem = None   
    display: str = None # Displayed intermediate messages to the user

class DeepRAGState(AgentState):
    """
    State of the deep RAG sub-agent.
    """      
    searched_path: Dict[str, set[str]] = {}
    new_aspects_to_explore: str = None
    retrieve_tries: int = 0

class RAGAgent:
    def __init__(self, thread_manager: ThreadManager = None, user_id: int = None, on_langgraph_server: bool = False):
        """
        Initialize the agent.
        
        Args:
            thread_manager: Thread manager instance
            user_id: User ID to use for API configuration
            on_langgraph_server: Whether running on LangGraph server
        """
        try:
            rag_type_str = os.getenv("RAG_TYPE", "simple").lower()
            rag_type = RAGType(rag_type_str)
        except ValueError:
            rag_type = RAGType.SIMPLE        
        self.rag_type = rag_type    
        self.rag_k = int(os.getenv("RAG_K", 10))      
        
        # Initialize LLM runner based on user ID (uses ApiLLMRunner if user_id is provided)
        if user_id:
            self.llm_runner = get_api_llm_runner(user_id)
        else:
            self.llm_runner = LLMRunner()
            
        self.user_id = user_id
        self.thread_manager = thread_manager
        self.knowledgebase_id = 0
        self.knowledgebase_item = None
        self.on_langgraph_server = on_langgraph_server
        self.conn_str = os.getenv("DB_URI")
        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                checkpointer.setup()
        self.builder = self._build_graph()

        self.update_dict = {
            "classify_intent": "User intent classified",
            "handle_rag": "Retrieved documents from knowledge base.",
            "filter_documents": "Filtered documents.",
            "deep_retrieve": "Retrieved addtional documents from knowledge base.",
            "filter_additional_documents": "Filtered additional documents.",
            "complement_answer": "Complemented the answer with additional documents.",
        }

    def _build_graph(self):
        """
        Build the graph for the agent.
        """
        builder = self._build_base_graph()
        return builder

    def _classify_intent(self, state: AgentState) -> AgentState:
        """
        Classify the intent of the user query.
        """     

        prompt = classify_intent_prompt(state)

        response = self.llm_runner.invoke([SystemMessage(content=prompt)])
        intent = response.content.strip().lower()
        if intent not in ["rag", "chat"]:
            intent = "chat"

        # For debugging with LangGraph server
        if self.on_langgraph_server:
            return {
                "intent": intent,
                "messages": [{"role": "user", "content": state["query"]}],
                "knowledge_base_item": self.get_knowledgebase_item(self.user_id, 1),
            }
            
        return {
            "intent": intent,
        }

    def _handle_chat(self, state: AgentState) -> AgentState:
        """
        Handle the chat.
        """
        system_prompt = handle_chat_prompt(state)

        response = self.llm_runner.invoke([SystemMessage(content=system_prompt)])

        return {
            "messages": [response],
        }
    
    def _refine_query(self, state: AgentState) -> AgentState:
        """
        Refine the query.
        """
        if self.rag_type == RAGType.SIMPLE:
            refined_query = state["query"]
        else:
            prompt = refine_query_prompt(state)
            response = self.llm_runner.invoke([SystemMessage(content=prompt)])
            refined_query = response.content.strip()
        return {
            "refined_query": refined_query,
        }

    def _handle_rag(self, state: AgentState) -> AgentState:
        """
        Handle the RAG.
        """
        refined_query = state["refined_query"]
            
        rag_flow = RAGFlow(state["knowledge_base_item"].path)
        results = rag_flow.retrieve(self.rag_type, refined_query, k=self.rag_k)
        return {
            "documents": results,
        }

    def _filter_documents(self, state: AgentState) -> AgentState:
        """
        Filter the documents.
        """
        documents = state["documents"]
        if self.rag_type == RAGType.SIMPLE:
            return {"documents": documents}
        else:
            query = state["refined_query"]
            documents = state["documents"]          
            prompt = filter_documents_prompt(query, documents)
            response = self.llm_runner.invoke([SystemMessage(content=prompt)])
            try:
                filtered_document_indices = list(map(int, response.content.strip().split(",")))
            except ValueError:
                filtered_document_indices = list(range(len(documents)))
            return {
                "documents": [documents[i] for i in filtered_document_indices],
            }

    def _format_answer(self, state: AgentState) -> AgentState:
        """
        Format the answer.
        """
        prompt = format_answer_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)])
        
        return {
            "answer": response.content.strip(),
            "messages": [response],
        }

    def _plan_rag(self, state: DeepRAGState) -> AgentState:
        """
        Plan the RAG.
        """
        prompt = plan_rag_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)])
        new_aspects_to_explore = response.content.strip()
        return {
            "new_aspects_to_explore": new_aspects_to_explore,
            "display": f"Explore aspects:\n{new_aspects_to_explore}",
        }

    def _deep_rag(self, state: DeepRAGState) -> DeepRAGState:
        """
        Handle the deep RAG.
        """
        new_aspects_to_explore = state["new_aspects_to_explore"]
        if new_aspects_to_explore == "none":
            return { "messages": AIMessage(content="end")}

        prompt = deep_rag_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)], [list_children_tool, rag_search_tool])
        if response.content.strip():
            logger.info(f"[deep_rag] Response: {response.content.strip()}")
        return {
            "messages": [response],
        }

    def _reference_check(self, state: DeepRAGState) -> DeepRAGState:
        """
        Check the reference.
        """       
        prompt = reference_check_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)])
        return {
            "answer": response.content.strip(),
        }

    def _build_base_graph(self) -> StateGraph:
        """
        Build the base graph for the agent.
        """
        if self.rag_type == RAGType.AGENTIC:
            graph = StateGraph(DeepRAGState)
        else:
            graph = StateGraph(AgentState)  

        graph.add_node("classify_intent", self._classify_intent)
        graph.add_node("refine_query", self._refine_query)
        graph.add_node("handle_chat", self._handle_chat)
        if self.rag_type == RAGType.AGENTIC:
            graph.add_node("plan_rag", self._plan_rag)
            graph.add_node("deep_rag", self._deep_rag)      
            graph.add_node("deep_retrieve", ToolNode([list_children_tool, rag_search_tool])) 
            graph.add_node("reference_check", self._reference_check)
        else:
            graph.add_node("handle_rag", self._handle_rag)
            graph.add_node("filter_documents", self._filter_documents)
            graph.add_node("format_answer", self._format_answer)

        graph.add_edge(START, "classify_intent")
        graph.add_conditional_edges(
            "classify_intent",
            lambda state: state["intent"],
            {
                "rag": "refine_query",
                "chat": "handle_chat",
            }
        )
        graph.add_edge("handle_chat", END)
        if self.rag_type == RAGType.AGENTIC:
            graph.add_edge("refine_query", "plan_rag")
            graph.add_edge("plan_rag", "deep_rag")
            graph.add_conditional_edges(
            "deep_rag",
            tools_condition,
            {
                "tools": "deep_retrieve",
                "__end__": "reference_check",
            },
            )  
            graph.add_edge("deep_retrieve", "deep_rag")
            graph.add_edge("reference_check", END)
        else:
            graph.add_edge("refine_query", "handle_rag")
            graph.add_edge("handle_rag", "filter_documents")
            graph.add_edge("filter_documents", "format_answer")
            graph.add_edge("format_answer", END)     

        return graph

    def get_conversation_history(self, user_id: int, thread_id: str) -> List[Dict[str, Any]]:
        """
        Get the conversation history for a user and thread.
        """
        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                graph = self.builder.compile(checkpointer=checkpointer)
                return self.thread_manager.get_conversation_history(user_id, thread_id, graph)
        else:      
            graph = self.builder.compile(checkpointer=InMemorySaver())
            return self.thread_manager.get_conversation_history(user_id, thread_id, graph)
    
    def chat(self, query: str, user_id: int, knowledge_base_id: int, config: Dict[str, Any] = None) -> Generator[Dict[str, Any], None, None]:
        """
        Chat with the agent.
        """

        knowledgebase_item = self.get_knowledgebase_item(user_id, knowledge_base_id)

        logger.info(f"Chat with Knowledgebase: {knowledgebase_item.name}")

        initial_state = {
            "query": query,
            "messages": [{"role": "user", "content": query}],
            "knowledge_base_item": knowledgebase_item,
        }

        if self.conn_str:
            with PostgresSaver.from_conn_string(self.conn_str) as checkpointer: 
                graph = self.builder.compile(checkpointer=checkpointer)
                # Streaming mode: yield chunks as they become available                
                for mode, chunk in graph.stream(initial_state, 
                                                config=config, 
                                                stream_mode=["updates", "messages"]):
                    if mode == "updates":
                        for node, state in chunk.items():
                            if node in self.update_dict:
                                update = {
                                    "stage": self.update_dict[node],
                                }
                                # Only add display if it exists in the state
                                if "display" in state and state["display"]:
                                    update["display"] = state["display"]
                                yield update
                    elif mode == "messages":
                        message, meta = chunk
                        if message.content and meta["langgraph_node"] in ["handle_chat", "format_answer", "reference_check"]:
                            last_assistant_message = message.content   
                            yield {
                                "response": last_assistant_message,
                            }
        else:
            graph = self.builder.compile(checkpointer=InMemorySaver())
            
            # Streaming mode: yield chunks as they become available                
            for mode, chunk in graph.stream(initial_state, 
                                            config=config, 
                                            stream_mode=["updates", "messages"]):
                if mode == "updates":
                    for node, state in chunk.items():
                        if node in self.update_dict:
                            yield {
                                    "stage": self.update_dict[node],
                                }
                elif mode == "messages":
                    message, meta = chunk
                    if message.content and meta["langgraph_node"] in ["handle_chat", "format_answer", "complement_answer"]:
                        last_assistant_message = message.content   
                        yield {
                            "response": last_assistant_message,
                        }
    
    def get_knowledgebase_item(self, user_id: int, knowledgebase_id: int) -> KnowledgeBaseItem:
        """
        Get the knowledge base item.
        """
        if knowledgebase_id == self.knowledgebase_id:
            return self.knowledgebase_item

        knowledgebase_manager = MemoryManager().knowledgebase_manager
        knowledgebase = knowledgebase_manager.get_knowledgebase(knowledgebase_id)
        knowledgebase_name = knowledgebase["name"]
        root_path = get_upload_dir(user_id, knowledgebase_name, "")
        index_path = get_index_path(user_id, knowledgebase_name)

        knowledgebase_item = KnowledgeBaseItem(
            id=knowledgebase_id,
            name=knowledgebase_name,
            root_path=root_path,
            index_path=index_path,
            description=knowledgebase["description"],
        )        

        self.knowledgebase_id = knowledgebase_id
        self.knowledgebase_item = knowledgebase_item

        return knowledgebase_item
        

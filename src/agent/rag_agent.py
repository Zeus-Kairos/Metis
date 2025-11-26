import logging
from re import search
from typing import Annotated, Any, Dict, Generator, List, Tuple, TypedDict

from langchain_core.documents import Document
from langchain_core.messages import AIMessage, SystemMessage, ToolMessage
from langchain.agents import create_agent
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode, tools_condition
from numpy import add
from src.agent.tools import retrieve_tool
from src.agent.prompts import classify_intent_prompt, complement_answer_prompt, deep_rag_prompt, filter_documents_prompt, format_answer_prompt, handle_chat_prompt, refine_query_prompt
from src.rag.rag_flow import RAGFlow, RAGType
from src.agent.llm import LLMRunner
from src.utils.knowledge_base_reader import KnowledgeBaseItem, KnowledgeBaseReader
from src.utils.merger import merge_documents

logger = logging.getLogger(__name__)

class AgentState(TypedDict):
    """
    State of the agent.
    """
    query: str
    intent: str = None
    refined_query: str = None
    messages: Annotated[List[Dict[str, str]], add_messages]
    documents: list[Document] | List[Tuple[Document, float]] = None
    answer: str
    error_context: str = None
    knowledge_base_item: KnowledgeBaseItem = None   

class DeepRAGState(AgentState):
    """
    State of the deep RAG sub-agent.
    """
    searched_path: set[str]
    additional_documents: Dict[str, list[Document]]
    retrieve_tries: int = 0

class RAGAgent:
    def __init__(self, rag_type: RAGType = RAGType.SIMPLE, rag_k: int = 10, on_langgraph_server: bool = False):
        """
        Initialize the agent.
        """
        self.rag_type = rag_type
        self.llm_runner = LLMRunner()
        self.rag_k = rag_k
        self.on_langgraph_server = on_langgraph_server
        
        self.graph = self._build_graph()

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
        graph = self._build_base_graph()

        if self.on_langgraph_server:
            return graph.compile()
        else:
            return graph.compile(checkpointer=InMemorySaver())

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
                "knowledge_base_item": KnowledgeBaseReader().get_knowledge_base_item(1),
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

    def _handle_rag(self, state: AgentState) -> AgentState:
        """
        Handle the RAG.
        """
        if self.rag_type == RAGType.SIMPLE:
            refined_query = state["query"]
        else:
            prompt = refine_query_prompt(state)
            response = self.llm_runner.invoke([SystemMessage(content=prompt)])
            refined_query = response.content.strip()
            
        rag_flow = RAGFlow(state["knowledge_base_item"].path)
        results = rag_flow.retrieve(self.rag_type, refined_query, k=self.rag_k)
        return {
            "refined_query": refined_query,
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

    def _deep_rag(self, state: DeepRAGState) -> DeepRAGState:
        """
        Handle the deep RAG.
        """
        MAX_RETRIEVE_TRIES = 3
        retrieve_tries = state["retrieve_tries"] if "retrieve_tries" in state else 0
        if retrieve_tries >= MAX_RETRIEVE_TRIES:
            logging.info("retrieve finished.")
            return {
                "messages": [AIMessage(content="retrieve finished.")],
                "retrieve_tries": 0,
            }

        prompt = deep_rag_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)], [retrieve_tool])
        if response.content.strip():
            logger.info(f"[deep_rag] Response: {response.content.strip()}")
        return {
            "messages": [response],
            "retrieve_tries": retrieve_tries + 1,
        }

    def _filter_additional_documents(self, state: DeepRAGState) -> DeepRAGState:
        """
        Filter the documents.
        """
        # Find the last continuous ToolMessage
        tool_messages = []
        for i in range(len(state["messages"]) - 1, -1, -1):
            if isinstance(state["messages"][i], ToolMessage):
                tool_messages.append(state["messages"][i])
            else:
                break
        
        additional_documents = state["additional_documents"] if "additional_documents" in state else {}
        searched_path = state["searched_path"] if "searched_path" in state else set()
        for tool_message in tool_messages:
            context = tool_message.artifact
            query = context["query"]
            retrieved_documents = context["retrieved_documents"]
            search_path = context["search_path"]
            searched_path.add(search_path)
            logger.info(f"Retrieved {len(retrieved_documents)} documents for query: {query} on path: {search_path}")    
            if len(retrieved_documents) == 0:
                continue      
            prompt = filter_documents_prompt(query, retrieved_documents)
            response = self.llm_runner.invoke([SystemMessage(content=prompt)])
            try:
                filtered_document_indices = list(map(int, response.content.strip().split(",")))
            except ValueError:
                filtered_document_indices = list(range(len(retrieved_documents)))
            if len(filtered_document_indices) > 0:
                additional_documents[query] = [retrieved_documents[i] for i in filtered_document_indices]
            
        return {
            "searched_path": searched_path,
            "additional_documents": additional_documents,
        }

    def _complement_answer(self, state: DeepRAGState) -> DeepRAGState:
        """
        Complement the answer with the documents.
        """       
        prompt = complement_answer_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)])
        documents = state["documents"]
        if documents and isinstance(documents[0], tuple):
            documents = [doc for doc, _ in documents]
        merged_documents = merge_documents(documents + [doc for sublist in state["additional_documents"].values() for doc in sublist])
        return {
            "answer": response.content.strip(),
            "documents": merged_documents,
            "additional_documents": {}
        }

    def _build_base_graph(self) -> StateGraph:
        """
        Build the base graph for the agent.
        """
        graph = StateGraph(AgentState)

        graph.add_node("classify_intent", self._classify_intent)
        graph.add_node("handle_rag", self._handle_rag)
        graph.add_node("handle_chat", self._handle_chat)
        graph.add_node("filter_documents", self._filter_documents)
        graph.add_node("format_answer", self._format_answer)
        if self.rag_type == RAGType.AGENTIC:
            graph.add_node("deep_rag", self._deep_rag)      
            graph.add_node("deep_retrieve", ToolNode([retrieve_tool]))
            graph.add_node("filter_additional_documents", self._filter_additional_documents)
            graph.add_node("complement_answer", self._complement_answer)     

        graph.add_edge(START, "classify_intent")
        graph.add_conditional_edges(
            "classify_intent",
            lambda state: state["intent"],
            {
                "rag": "handle_rag",
                "chat": "handle_chat",
            }
        )
        graph.add_edge("handle_chat", END)
        graph.add_edge("handle_rag", "filter_documents")
        graph.add_edge("filter_documents", "format_answer")
        if self.rag_type == RAGType.AGENTIC:
            graph.add_edge("format_answer", "deep_rag")
            graph.add_conditional_edges(
            "deep_rag",
            # Assess LLM decision (call `retriever_tool` tool or respond to the user)
            tools_condition,
            {
                # Translate the condition outputs to nodes in our graph
                "tools": "deep_retrieve",
                END: END,
            },
        )
            graph.add_edge("deep_retrieve", "filter_additional_documents")     
            graph.add_edge("filter_additional_documents", "complement_answer")     
            graph.add_edge("complement_answer", "deep_rag")    
        else:
            graph.add_edge("format_answer", END)     

        return graph
    
    def chat(self, query: str, knowledge_base_id: int = 1) -> Generator[Dict[str, Any], None, None]:
        """
        Chat with the agent.
        """

        knowledge_base_item = KnowledgeBaseReader().get_knowledge_base_item(knowledge_base_id)
        logger.info(f"Knowledge base: {knowledge_base_item.path}")

        initial_state = {
            "query": query,
            "messages": [{"role": "user", "content": query}],
            "knowledge_base_item": knowledge_base_item,
        }

        config = {"configurable": {"thread_id": 1}}

        # Streaming mode: yield chunks as they become available                
        for mode, chunk in self.graph.stream(initial_state, 
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


        

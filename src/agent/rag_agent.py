from enum import Enum
import logging
from typing import Annotated, Any, Dict, Generator, List, Tuple, TypedDict

from langchain_core.documents import Document
from langchain_core.messages import SystemMessage
from langchain_community.document_compressors import FlashrankRerank
from langchain.agents import create_agent
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from src.agent.prompts import classify_intent_prompt, format_answer_prompt, handle_chat_prompt, refine_query_prompt
from src.rag.rag_flow import RAGFlow
from src.agent.llm import LLMRunner
from src.utils.knowledge_base_reader import KnowledgeBaseItem, KnowledgeBaseReader

logger = logging.getLogger(__name__)

class RAGType(Enum):
    """
    Type of the RAG.
    """
    SIMPLE = "simple"
    PROMPT_REFINED = "prompt_refined"
    HYBRID = "hybrid"

class AgentState(TypedDict):
    """
    State of the agent.
    """
    query: str
    intent: str = None
    refined_query: str = None
    messages: Annotated[List[Dict[str, str]], add_messages]
    documents: list[Document] = None
    ranked_documents: list[Document] | List[Tuple[Document, float]] = None
    answer: str
    error_context: str = None
    knowledge_base_item: KnowledgeBaseItem = None

class RAGAgent:
    def __init__(self, rag_type: RAGType = RAGType.SIMPLE, rag_k: int = 10, on_langgraph_server: bool = False):
        """
        Initialize the agent.
        """
        self.rag_type = rag_type
        self.llm_runner = LLMRunner()
        self.rag_k = rag_k
        self.on_langgraph_server = on_langgraph_server
        
        self.graph = self._build_graph(rag_type)

        self.update_dict = {
            "classify_intent": "User intent classified",
            "handle_rag": "Retrieved documents from knowledge base.",
        }

    def _build_graph(self, rag_type: RAGType):
        """
        Build the graph for the agent.
        """
        match rag_type:
            case RAGType.SIMPLE:
                graph = self._build_base_graph()
            case RAGType.PROMPT_REFINED:
                graph = self._build_base_graph()
            case RAGType.HYBRID:
                graph = self._build_base_graph()
            case _:
                raise ValueError(f"Unknown RAG type: {rag_type}")

        logger.info(f"graph: {graph}")
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
        if self.rag_type == RAGType.HYBRID:
            results = rag_flow.hybrid_retrieve(refined_query, k=self.rag_k)
            return {
                "refined_query": refined_query,
                "ranked_documents": results,
            }
        else:
            results = rag_flow.retrieve(refined_query, k=self.rag_k)
            return {
                "refined_query": refined_query,
                "documents": results,
            }

    def _format_answer(self, state: AgentState) -> str:
        """
        Format the answer.
        """
        prompt = format_answer_prompt(state)
        response = self.llm_runner.invoke([SystemMessage(content=prompt)])
        
        return {
            "answer": response.content.strip(),
            "messages": [response],
        }

    def _build_base_graph(self) -> StateGraph:
        """
        Build the base graph for the agent.
        """
        graph = StateGraph(AgentState)

        graph.add_node("classify_intent", self._classify_intent)
        graph.add_node("handle_rag", self._handle_rag)
        graph.add_node("handle_chat", self._handle_chat)
        graph.add_node("format_answer", self._format_answer)

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
        graph.add_edge("handle_rag", "format_answer")
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
        for mode, chunk in self.graph.stream(initial_state, config=config, stream_mode=["updates", "messages"]):
            if mode == "updates":
                for node, state in chunk.items():
                    if node in self.update_dict:
                        yield {
                            "stage": self.update_dict[node],
                        }
            elif mode == "messages":
                message, meta = chunk
                if message.content and meta["langgraph_node"] in ["handle_chat", "format_answer"]:
                    last_assistant_message = message.content   
                    yield {
                        "response": last_assistant_message,
                    }


        

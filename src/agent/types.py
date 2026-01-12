from dataclasses import dataclass
import operator
from typing import Annotated, Dict, Generator, List, Tuple, TypedDict
from pydantic import BaseModel
from langchain_core.documents import Document
from langgraph.graph.message import add_messages

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

class RAGResult(BaseModel):
    """
    Result of the RAG agent.
    """
    aspect: str
    documents: list[Document] = []
    answer: str = ""
    is_done: bool = False

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
    aspects_to_explore: List[str]
    searched_aspects: Annotated[
        List[RAGResult], operator.add
    ]

class DeepSearchState(AgentState):
    """
    State of the deep search sub-agent.
    """
    aspect: str
    knowledge_base_item: KnowledgeBaseItem
    searched_aspects: Annotated[
        List[RAGResult], operator.add
    ]  # All researchers write to this key in parallel
from typing import List, Tuple
from langchain.tools import tool, ToolRuntime
from langchain_core.documents import Document

from src.rag.rag_flow import RAGFlow

@tool
def rag_search(runtime: ToolRuntime) -> List[Tuple[Document, float]]:
    """
    Search the local knowledge base for the given query based on similarity score.

    Returns:
        A list of tuples, where each tuple contains a Document and its L2 distance.
    """

    query = runtime.state["query"]

    rag_flow = RAGFlow("./Docs/VNA_Help_MD")
    results = rag_flow.retrieve(query)
    return results
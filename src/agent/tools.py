import logging
from typing import List, Tuple
from langchain.tools import tool, ToolRuntime
from langchain_core.documents import Document

from src.rag.rag_flow import RAGFlow

logger = logging.getLogger(__name__)

@tool("retrieve")
def retrieve_tool(query: str, search_path: str, runtime: ToolRuntime) -> str:
    """
    Retrieve documents within certain search path for the RAG.
    Args:
        query (str): The query to retrieve documents.
        search_path (str): The search path to filter documents.
    Returns:
        The documents retrieved.
    """
    # parse search_path to filters
    filters = {}
    if search_path:
        # if search_path is a folder
        if search_path.endswith("/") or "." not in search_path.split("/")[-1]:
            # 1. if search_path is a folder, split folder structure into categories
            # e.g. "folder1/folder2" -> {"category_level_1": "folder1", "category_level_2": "folder2"}
            categories = search_path.split("/")
            for i, category in enumerate(categories):
                filters[f"category_level_{i+1}"] = category.strip()
        else:
            # 2. if search_path is a file, split file path into categories and file_path
            # e.g. "folder1/folder2/file.md" -> {"category_level_1": "folder1", "category_level_2": "folder2", "file_path": "file.md"}
            sections = search_path.split("/")
            if len(sections) > 1:
                for i, category in enumerate(sections[:-1]):
                    filters[f"category_level_{i+1}"] = category.strip()
            else:
                filters["category_level_0"] = "root"
            filters["file_path"] = search_path.split("/")[-1]

    logger.info(f"Retriever Filters: {filters}")

    rag_flow = RAGFlow(runtime.state["knowledge_base_item"].path)
    results = rag_flow.filtered_retrieve(query, filters)
    return f"Documents retrieved {results}"
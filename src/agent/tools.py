import json
import logging
import re
from typing import Annotated, Dict, List, Tuple
from langchain.tools import InjectedToolCallId, tool, ToolRuntime
from langchain_core.documents import Document
from langchain_core.messages import ToolMessage, SystemMessage
from langgraph.types import Command

from src.agent.prompts import filter_documents_prompt, complement_answer_prompt, review_answer_prompt
from src.agent.api_llm import get_active_llm_runner
from src.memory.memory import MemoryManager
from src.rag.rag_flow import RAGFlow
from src.utils.merger import merge_documents
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

@tool("retrieve", response_format="content_and_artifact")
def retrieve_tool(query: str, search_path: str, k: int, runtime: ToolRuntime) -> Tuple[str, dict]:
    """
    Retrieve documents within certain search path for the RAG.
    Args:
        query (str): The query to retrieve documents.
        search_path (str): The search path to filter documents.
        k (int): The number of documents to retrieve. max 10.
    Returns:
        A tuple of (content, artifact) where artifact is the documents retrieved.
    """
    # parse search_path to filters
    filters = {}
    if search_path:
        # if search_path is a folder
        if search_path.endswith("/") or "." not in search_path.split("/")[-1]:
            # 1. if search_path is a folder, split folder structure into categories
            # e.g. "folder1/folder2" -> {"category_level_1": "folder1", "category_level_2": "folder2"}
            categories = search_path.rstrip("/").split("/")
            for i, category in enumerate(categories):
                filters[f"category_level_{i+1}"] = category.strip()
        else:
            # 2. if search_path is a file, split file path into categories and file_path
            # e.g. "folder1/folder2/file.md" -> {"category_level_1": "folder1", "category_level_2": "folder2", "file_path": "folder1/folder2/file.md"}
            sections = search_path.split("/")
            if len(sections) > 1:
                for i, category in enumerate(sections[:-1]):
                    filters[f"category_level_{i+1}"] = category.strip()
            else:
                filters["category_level_0"] = "root"
            filters["file_path"] = search_path

    logger.info(f"[retrieve_tool] Query: {query}")
    logger.info(f"[retrieve_tool] Retriever Filters: {filters}")

    rag_flow = RAGFlow(runtime.state["knowledge_base_item"].path)
    results = rag_flow.filtered_fusion_retrieve(query, filters, k=k)

    return ("Documents retrieved", 
        {   "query": query,
            "search_path": search_path,
            "retrieved_documents": results
        })

@tool("list_children")
def list_children_tool(parent_folder: str, runtime: ToolRuntime, tool_call_id: Annotated[str, InjectedToolCallId]) -> Command:
    """
    List folders and files within certain parent folder.
    Args:
        parent_folder (str): The parent folder to filter items.
    Returns:
        Children folders and files with description.
    """
    logger.info(f"[list_children_tool] Parent Folder: {parent_folder}")

    kb_id = runtime.state["knowledge_base_item"].id
    knowledgebase_manager = MemoryManager().knowledgebase_manager
    children_items = knowledgebase_manager.get_files_by_parent(kb_id, parent_folder)
    
    logger.info(f"[list_children_tool] {children_items} Children Items Listed")

    message = f"\nChildren listed in {parent_folder}:\n"
    for item in children_items:
        filename = item[1]  # filename is at index 1
        description = item[4]  # description is at index 4
        type = item[5]  # type is at index 5
        if description:
            message += f"[{type}] {filename}: {description}\n"
        else:
            message += f"[{type}] {filename}\n"

    return Command(
        update={
            # update the message history
            "messages": [ToolMessage(message, tool_call_id=tool_call_id)],
            "display": message
        }
    )

@tool("rag_search")
def rag_search_tool(query: str, search_path: str, k: int, runtime: ToolRuntime, tool_call_id: Annotated[str, InjectedToolCallId]) -> Command:
    """
    Search documents within the search path for the RAG.
    Args:
        query (str): The query to retrieve documents.
        search_path (str): The search path to filter documents.
        k (int): The number of documents to retrieve. max 10.
    Returns:
        A new answer based on the original answer and the new retrieved documents.
    """
    # parse search_path to filters
    filters = {}
    if search_path:
        retrieve_tries = runtime.state["retrieve_tries"] if "retrieve_tries" in runtime.state else 0
        logger.info(f"[rag_search_tool] Query: {query} on path: {search_path}")
        searched_path = runtime.state["searched_path"] if "searched_path" in runtime.state else {}
        if query not in searched_path:
            searched_path[query] = set()
        searched_path[query].add(search_path)
        rag_flow = RAGFlow(runtime.state["knowledge_base_item"].index_path)
        # if search_path is a folder
        if search_path.endswith("/") or "." not in search_path.split("/")[-1]:
            # 1. if search_path is a folder, split folder structure into categories
            # e.g. "folder1/folder2" -> {"category_level_1": "folder1", "category_level_2": "folder2"}               
            knowledgebase_manager = MemoryManager().knowledgebase_manager
            file_ids = knowledgebase_manager.get_files_by_path_prefix(search_path) 
            logger.info(f"[rag_search_tool] Search {len(file_ids)} Files under path: {search_path}")   
            docs = rag_flow.files_fusion_retrieve(query, file_ids, k=k)  
        else:
            filters["file_path"] = search_path
            logger.info(f"[rag_search_tool] Search Filters: {filters}")     
            docs = rag_flow.filtered_fusion_retrieve(query, filters, k=k)
        
        logger.info(f"[rag_search_tool] Retrieved {len(docs)} documents for query: {query} on path: {search_path}")
        if not docs:
            return Command(
                update={
                    "searched_path": searched_path,
                    "messages": [ToolMessage(content="No documents found", tool_call_id=tool_call_id)],
                    "retrieve_tries": retrieve_tries + 1
                }
            )
        filtered_docs = filter_documents(query, docs)
        if not filtered_docs:
            return Command(
                update={
                    "searched_path": searched_path,
                    "messages": [ToolMessage(content="No documents found", tool_call_id=tool_call_id)],
                    "retrieve_tries": retrieve_tries + 1
                }
            )
        documents = runtime.state["documents"] if "documents" in runtime.state else []
        new_documents = [doc for sublist in filtered_docs.values() for doc in sublist]
        if documents and isinstance(documents[0], tuple):
            documents = [doc for doc, _ in documents]
        merged_documents = merge_documents(documents + new_documents)
        
        answer = runtime.state["answer"] if "answer" in runtime.state else ""
        answer = complement_answer(query, answer, filtered_docs)

        review = review_answer(query, answer)       
        is_done = "done" in review

        message = f"{len(new_documents)} documents found. Answer Review: {review}"
        
        return Command(
            update={
                "searched_path": searched_path,
                "documents": merged_documents,
                "answer": answer,
                "review": review,
                "is_done": is_done,
                "messages": [ToolMessage(content=message, tool_call_id=tool_call_id)],
                "retrieve_tries": retrieve_tries + 1,
                "display": f"Found {len(new_documents)} documents for query: {query} on path: {search_path}:\n{"\n".join([doc.metadata["file_path"] for doc in new_documents])}"
            }
        )

def filter_documents(query: str, docs: List[Document]) -> List[Document]:
    prompt = filter_documents_prompt(query, docs)
    response = get_active_llm_runner().invoke([SystemMessage(content=prompt)])
    try:
        filtered_document_indices = list(map(int, response.content.strip().split(",")))
    except ValueError:
        filtered_document_indices = list(range(len(docs)))
    if len(filtered_document_indices) > 0:
        return {
            query: [docs[i] for i in filtered_document_indices],
        }
    else:
        return {
            query: [],
        }

def complement_answer(query: str, answer: str, additional_docs: Dict[str, List[Document]]) -> str:
    """
    Complement the answer with the documents.
    """       
    prompt = complement_answer_prompt(query, answer, additional_docs)
    response = get_active_llm_runner().invoke([SystemMessage(content=prompt)])
    
    return response.content.strip()

def review_answer(query: str, answer: str) -> str:
    """
    Review the answer.
    """
    prompt = review_answer_prompt(query, answer)     
    response = get_active_llm_runner().invoke([SystemMessage(content=prompt)])
    answer_review = response.content.strip().lower()
    logger.info(f"[review_answer] Review: {answer_review}")

    return answer_review

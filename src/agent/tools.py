import hashlib
import json
import logging
import os
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from typing import Annotated, Dict, List, Tuple
from langchain.tools import InjectedToolCallId, tool, ToolRuntime
from langchain_core.documents import Document
from langchain_core.messages import ToolMessage, SystemMessage
from langgraph.types import Command

from src.agent.prompts import review_answer_prompt, summarize_single_document_prompt
from src.agent.api_llm import get_active_llm_runner
from src.memory.memory import MemoryManager
from src.rag.rag_flow import RAGFlow
from src.utils.merger import merge_documents
from src.utils.logging_config import get_logger
from src.utils.paths import get_relative_path_from_origin

logger = get_logger(__name__)


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _append_agent_event(runtime: ToolRuntime, event: Dict[str, object]) -> List[Dict[str, object]]:
    existing = runtime.state["agent_events"] if "agent_events" in runtime.state and runtime.state["agent_events"] else []
    return [*existing, event]


def _doc_summary_state_key(doc: Document) -> str:
    return doc.metadata.get("chunk_id", "")

def _summarize_one_doc_for_query(doc: Document, query: str) -> Tuple[Document, str]:
    prompt = summarize_single_document_prompt(doc, query)
    response = get_active_llm_runner().invoke([SystemMessage(content=prompt)])
    text = (response.content or "").strip()
    return (doc, text)


def summarize_documents(query: str, docs: List[Document]) -> Tuple[List[Document], Dict[str, str]]:
    """
    Summarize each document in order, one at a time (focus = query). Drop docs with empty summary.
    Same return shape as summarize_documents_parallel_focus.
    """
    if not docs:
        return [], {}
    summaries: Dict[str, str] = {}
    kept: List[Document] = []
    for doc in docs:
        d, text = _summarize_one_doc_for_query(doc, query)
        if text:
            summaries[_doc_summary_state_key(d)] = text
            kept.append(d)
    return kept, summaries


def summarize_documents_parallel_focus(query: str, docs: List[Document]) -> Tuple[List[Document], Dict[str, str]]:
    """
    Summarize each document in parallel (focus = query). Drop docs with empty summary.
    Returns (kept_documents, summaries_dict, formatted_message_body).
    """
    if not docs:
        return [], {}, ""
    max_workers = min(len(docs), 10)
    pairs: List[Tuple[Document, str]] = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_doc = {executor.submit(_summarize_one_doc_for_query, d, query): d for d in docs}
        for fut in as_completed(future_to_doc):
            doc, text = fut.result()
            if text:
                pairs.append((doc, text))
    summaries: Dict[str, str] = {}
    kept: List[Document] = []
    for doc, text in pairs:
        key = _doc_summary_state_key(doc)
        summaries[key] = text
        kept.append(doc)
    return kept, summaries


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

    rag_flow = RAGFlow(runtime.state["knowledge_base_item"].index_path)
    results = rag_flow.filtered_fusion_retrieve(query, filters, k=k)
    event = {
        "timestamp": _utc_now_iso(),
        "tool": "retrieve",
        "query": query,
        "search_path": search_path,
        "retrieved_count": len(results),
        "filters": filters,
    }

    return ("Documents retrieved", 
        {   "query": query,
            "search_path": search_path,
            "retrieved_documents": results,
            "agent_event": event,
        })

@tool("list_children")
def list_children_tool(parent_folder: str, runtime: ToolRuntime, tool_call_id: Annotated[str, InjectedToolCallId]) -> Command:
    """
    List folders and files within certain parent folder.
    Args:
        parent_folder (str): The parent folder to filter items.
    Returns:
        Children folders and files with description, e.g.
        [folder] folder1 *Description: An examaple folder*
        [file] file1.pdf *Description: An example file*
    """
    logger.info(f"[list_children_tool] Parent Folder: {parent_folder}")

    kb_id = runtime.state["knowledge_base_item"].id
    knowledgebase_manager = MemoryManager().knowledgebase_manager
    children_items = knowledgebase_manager.get_files_by_parent(kb_id, parent_folder)
    
    
    logger.info(f"[list_children_tool] len({children_items}) Children Items Listed")
    agent_events = _append_agent_event(runtime, {
        "timestamp": _utc_now_iso(),
        "tool": "list_children",
        "parent_folder": parent_folder,
        "children_count": len(children_items),
    })

    display_folder = get_relative_path_from_origin(parent_folder)
    message = f"\nChildren listed in {display_folder}:\n"
    for item in children_items:
        filename = item[1]  # filename is at index 1
        description = item[4]  # description is at index 4
        type = item[5]  # type is at index 5
        if description:
            message += f"[{type}] {filename} *Description: {description}*\n"
        else:
            message += f"[{type}] {filename}\n"

    return Command(
        update={
            # update the message history
            "messages": [ToolMessage(message, tool_call_id=tool_call_id)],
            "display": message,
            "agent_events": agent_events,
        }
    )

@tool("file_toc")
def file_toc(filepath: str, runtime: ToolRuntime, tool_call_id: Annotated[str, InjectedToolCallId]) -> str:
    """
    Get the table of contents of a file.
    Args:
        filepath (str): The filepath to get the table of contents.
    Returns:
        The table of contents of the file.
    """

    # Normalize filepath to use consistent path separators
    normalized_filepath = filepath.replace("/", os.sep).replace("\\", os.sep)
    
    knowledgebase_manager = MemoryManager().knowledgebase_manager
    toc = knowledgebase_manager.get_toc(normalized_filepath)
    if toc is None:
        message = f"No ToC found for {filepath}."
    else:
        message = f"ToC for {filepath}:\n{toc}"
    agent_events = _append_agent_event(runtime, {
        "timestamp": _utc_now_iso(),
        "tool": "file_toc",
        "filepath": filepath,
        "has_toc": toc is not None,
    })
    return Command(
        update={
            "messages": [ToolMessage(content=message, tool_call_id=tool_call_id)],
            "display": message,
            "agent_events": agent_events,
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

        display_folder = get_relative_path_from_origin(search_path)
        base_event = {
            "timestamp": _utc_now_iso(),
            "tool": "rag_search",
            "query": query,
            "search_path": search_path,
            "display_path": display_folder,
            "k": k,
        }
        if not docs:
            agent_events = _append_agent_event(runtime, {
                **base_event,
                "status": "no_documents",
                "retrieved_count": 0,
            })
            return Command(
                update={
                    "searched_path": searched_path,
                    "messages": [ToolMessage(content=f"No documents found for query: '{query}' on path: {display_folder}", tool_call_id=tool_call_id)],
                    "retrieve_tries": retrieve_tries + 1,
                    "is_done": False,
                    "agent_events": agent_events,
                }
            )

        # new_documents, new_summaries = summarize_documents_parallel_focus(query, docs)
        new_documents, new_summaries = summarize_documents(query, docs)
        if not new_documents:
            agent_events = _append_agent_event(runtime, {
                **base_event,
                "status": "no_relevant_documents",
                "retrieved_count": len(docs),
            })
            return Command(
                update={
                    "searched_path": searched_path,
                    "messages": [ToolMessage(
                        content=f"No relevant excerpts for query: '{query}' on path: {display_folder} (retrieved {len(docs)} chunks; all summaries empty or off-focus).",
                        tool_call_id=tool_call_id,
                    )],
                    "retrieve_tries": retrieve_tries + 1,
                    "agent_events": agent_events,
                }
            )

        documents = runtime.state["documents"] if "documents" in runtime.state else []
        if documents and isinstance(documents[0], tuple):
            documents = [doc for doc, _ in documents]
        merged_documents = merge_documents(documents + new_documents)

        summaries = runtime.state["summaries"] if "summaries" in runtime.state else {}
        summaries.update(new_summaries)

        review = review_answer(query, "\n\n".join(summaries.values()))

        message = (
            f"\n{len(new_documents)} relevant document(s) for query: '{query}' on path: {display_folder}\n"
            f"Answer Review: {review['status']} - {review['reason']}\n"
        )
        agent_events = _append_agent_event(runtime, {
            **base_event,
            "status": "ok",
            "retrieved_count": len(docs),
            "selected_count": len(new_documents),
            "review_status": review["status"],
            "review_reason": review["reason"],
        })

        return Command(
            update={
                "searched_path": searched_path,
                "documents": merged_documents,
                "summaries": summaries,
                "review": review,
                "messages": [ToolMessage(content=message, tool_call_id=tool_call_id)],
                "retrieve_tries": retrieve_tries + 1,
                "display": message,
                "agent_events": agent_events,
            }
        )

def review_answer(query: str, answer: str) -> Dict[str, str]:
    """
    Review the answer.
    """
    prompt = review_answer_prompt(query, answer)     
    response = get_active_llm_runner().invoke([SystemMessage(content=prompt)])
    try:
        answer_review = json.loads(response.content.strip())
    except json.JSONDecodeError:
        answer_review = {
            "status": "error",
            "reason": "Invalid JSON response",
        }
    logger.info(f"[review_answer] Review: {answer_review}")

    return answer_review

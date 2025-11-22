import logging
from typing import TypedDict
from langchain_core.messages.utils import (  
    trim_messages,  
    count_tokens_approximately  
)

from src.utils.document_handler import format_documents  

logger = logging.getLogger(__name__)

TOKEN_LIMIT = 2000

def classify_intent_prompt(state: TypedDict) -> str:
    """
    Classify the intent of the user query.
    """
    query = state["query"]
    # Trim messages to fit within token limit
    messages_history = trim_messages(  
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=TOKEN_LIMIT,
        start_on="human",
        end_on="human",
    )

    return f"""
    You are a helpful assistant. Based on the following context, classify the intent of the user input.
    The intent can be one of the following:
    - rag: Retrieve information from the knowledge base.
    - chat: Engage in a normal conversation.
    Return the intent in a single word.

    Context: {messages_history}
    User: {query}
    Intent:
    """

def handle_chat_prompt(state: TypedDict) -> str:
    """
    Handle the chat prompt.
    """
    query = state["query"]
    # Trim messages to fit within token limit
    messages_history = trim_messages(  
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=TOKEN_LIMIT,
        start_on="human",
        end_on="human",
    )

    return f"""
    You are a helpful assistant. Based on the conversation history, provide a response to the user.
    The response should be friendly, concise, and relevant to the user's query.
    If the user is asking for information that you don't know,
    politely inform them that you do not have that information.

    Conversation History: {messages_history}
    User: {query}

    Assistant:
    """

def refine_query_prompt(state: TypedDict) -> str:
    """
    Refine the user query.
    """
    query = state["query"]
    # Trim messages to fit within token limit
    messages_history = trim_messages(  
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=TOKEN_LIMIT,
        start_on="human",
        end_on="human",
    )               
    knowledge_base_item = state["knowledge_base_item"]

    return f"""
    You are a helpful assistant to help users refine their queries about the knowledge base.   
    Based on the conversation history, refine the user query.
    The refined query should be clear, concise, relevant to the user's intent and best for the RAG purpose.
    Only return the refined query, without any additional explanations.

    Knowledge Base: {knowledge_base_item.description}

    Conversation History: {messages_history}
    User: {query}

    Refined Query:
    """

def filter_documents_prompt(state: TypedDict) -> str:
    """
    Filter the documents.
    """
    documents = state["documents"]
    query = state["refined_query"]
    doc_contents = format_documents(documents, with_index=True)  

    return f"""
    You are a helpful assistant to help users filter the documents retrieved from the knowledge base.   
    Find out the documents that are relevant to the user's query.
    Only return the filtered document indices in a comma-separated list, without any additional explanations.

    Documents: {doc_contents}

    User Query: {query}

    Filtered Documents Indices:
    """

def format_answer_prompt(state: TypedDict) -> str:
    """
    Format the answer.
    """
    documents = state["documents"]
    doc_contents = format_documents(documents, with_index=False)  
    query = state["refined_query"]

    return f"""
    You are a helpful assistant. Based on the following documents, provide a response to the user.
    Find out the most relevant information from the documents to answer the user's query.
    The response should be friendly, concise, and relevant to the user's query.
    If the documents do not contain the information needed,
    politely inform them that you do not have that information.

    Documents: {doc_contents}
    User: {query}

    Assistant:
    """

def complement_answer_prompt(state: TypedDict) -> str:
    """
    Complement the answer.
    """
    answer = state["answer"]
    documents = state["documents"]
    # Handle both list[tuple] and list[Document] formats
    doc_contents = format_documents(documents, with_index=False)  
    query = state["refined_query"] if "refined_query" in state else state["query"]

    return f"""
    You are a helpful assistant to complement the answer based on new documents. 
    To address the user's query, find out the most relevant information from the documents to complement the current answer.
    The response should be friendly, concise, and relevant to the user's query.
    If the new documents do not contain the information needed, just keep the current answer.

    Current Answer: {answer}
    New Documents: {doc_contents}
    User: {query}

    Assistant:
    """

def deep_rag_prompt(state: TypedDict) -> str:
    """
    Deep RAG prompt.
    """
    query = state["refined_query"] if "refined_query" in state else state["query"]
    answer = state["answer"]
    knowledge_base_index_path = state["knowledge_base_item"].index_path
    # read the markdown index file
    with open(knowledge_base_index_path, 'r') as f:
        index = f.read()

    return f"""
    You are a helpful assistant to help retrieve the most relevant information from the knowledge base.   
    Based on the user query and the current answer to the query, you decide whether additional information should be retrieved from the knowledge base.
    You have access to the knowledge base index. The index contains the knowledge base structure and description of each folder.
    You also have a retrieval tool to find relevant documents in a specific folder in the knowledge base.
    You need to decide what additional information to retrieve and use the retrieval tool to search certain information from a specific folder.
    If the current answer to the query is sufficient, return "end" to stop the RAG process.

    Knowledge Base Index: {index}

    User: {query}
    User Current Answer: {answer}
    """
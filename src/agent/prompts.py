from typing import TypedDict
from langchain_core.messages.utils import (  
    trim_messages,  
    count_tokens_approximately  
)  

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

def format_answer_prompt(state: TypedDict) -> str:
    """
    Format the answer.
    """
    documents = state["ranked_documents"] if "ranked_documents" in state else state["documents"]
    # Handle both list[tuple] and list[Document] formats
    if documents and isinstance(documents[0], tuple):
        # Tuple structure: (doc, score)
        doc_contents = "\n".join([
            f"{doc[0].page_content}\n['Source: '{doc[0].metadata['file_path']}]"
            for doc in documents
        ])
    else:
        # Regular Document list
        doc_contents = "\n".join([
            f"{doc.page_content}\n['Source: '{doc.metadata['file_path']}]"
            for doc in documents
        ])
    query = state["refined_query"] if "refined_query" in state else state["query"]

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

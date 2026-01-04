import logging
from typing import Dict, List, Tuple, TypedDict
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage
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

def filter_documents_prompt(query: str, documents: List[Document] | List[Tuple[Document, float]]) -> str:
    """
    Filter the documents.
    """
    
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

def complement_answer_prompt(base_query: str, answer: str, documents: Dict[str, List[Document]]) -> str:
    """
    Complement the answer.
    """
    additional_info = "\n"
    for query, docs in documents.items():
        # Handle both list[tuple] and list[Document] formats
        doc_contents = format_documents(docs, with_index=False)  
        additional_info += f"Documents about {query}:\n{doc_contents}\n"

    return f"""
    You are a helpful assistant to generate an answer based on the original answer and additional documents. 
    You've already provided an answer to the user's query.
    The additional documents are related to additional aspects to the user's query.
    rewrite a new answer based on the original answer and the additional information.
    The answer should be friendly, concise, and relevant to the user's query.

    Constraints:
    - You can only use the facts in the original answer or the additional documents.
    - Do not make up any information based on your own knowledge or assumptions.

    Original Query: {base_query}
    Original Answer: {answer}
    Additional Documents: {additional_info}
    
    Assistant:
    """

def review_answer_prompt(query: str, answer: str, searched_path: Dict[str, set[str]]) -> str:
    """
    Review the answer.
    """

    explored_aspects = "\n".join([f"- {aspect}" for aspect in searched_path.keys()])

    return f"""
    You are an evaluator that reviews whether an assistant’s answer fully satisfies the user’s query.
    The current answer is based on the query results in the knowledge base to some aspects.
    Task:
    1. Carefully read the user’s query and identify the explicit and implicit requirements (sub-questions, constraints, context, and expected level of detail).​
    2. Read the assistant’s answer and assess it along these dimensions, focusing only on content, not style:​
        - Relevance: Does the answer directly address all parts of the user’s query without going off-topic?
        - Completeness: Does the answer cover all essential aspects of the query, including important edge cases, assumptions, or follow-up details a reasonable user would expect?
        - Accuracy/Correctness: Does the answer contain any clear errors, contradictions, or misleading statements relative to the question context?
        - Clarity: Is the answer understandable for the intended audience, with concepts explained at an appropriate level?
    3. Based on this assessment, decide if the answer is sufficient:
        - “Sufficient”: The answer is relevant, correct, and complete enough that a typical user would not need more information.
        - “Insufficient”: The answer fails to address key parts of the question, is largely incorrect, or is too vague to be useful.​
    4. If the answer is “Sufficient”, return "None".
       If the answer is “Insufficient”, return a new list of aspects that the assistant should query in the knowledge base to provide a sufficient answer.
       - The list should contain 1~3 new aspects.
       - Each new aspect should be brief and within 10 words.

    User Query: {query}
    User Current Answer: {answer}
    Explored Aspects: {explored_aspects}
    """

def deep_rag_prompt(state: TypedDict) -> str:
    """
    Deep RAG prompt.
    """
    query = state["refined_query"]
    new_aspects_to_explore = state["new_aspects_to_explore"]

    rag_messages = []
    for i in range(len(state["messages"]) - 1, -1, -1):
        if not isinstance(state["messages"][i], HumanMessage):
            rag_messages.append(state["messages"][i])
        else:
            break

    knowledgebase_description = state["knowledge_base_item"].description
    knowledgebase_root_path = state["knowledge_base_item"].root_path

    return f"""
    You are a helpful assistant to help retrieve the most relevant information from the knowledge base.   
    Based on the user query and the RAG history, you decide how additional information should be retrieved from the knowledge base.
    You have a list_children tool to list all children with description of a folder in the knowledge base.
    You also have a retrieval tool to find relevant documents in a specific folder in the knowledge base.
    You need to decide what additional information to retrieve and use the retrieval tool to search certain information from a specific folder.
    You can use the list_children tool to decide where to search. Use relative path to specify the search_path.

    If no additional information is needed, return "end".
    generate new queries for the tools based on the new aspects to explore.

    Constraints:
    - The search_path must include the knowledge base root folder.
    - Base on the RAG history, don't repeat the aspects and search paths that have been explored.

    Knowledge Base Description: {knowledgebase_description}
    Knowledge Base Root Folder: {knowledgebase_root_path}
    New Aspects to Explore: {new_aspects_to_explore}

    User Query: {query}
    RAG History: {rag_messages}
    """

def reference_check_prompt(state: TypedDict) -> str:
    """
    Reference check prompt.
    """
    query = state["refined_query"]
    answer = state["answer"] if "answer" in state else ""
    documents = state["documents"]
    doc_contents = format_documents(documents, with_index=True, index_offset=1)  

    return f"""
    You are an assistant that reviews an existing answer against a set of reference documents and adds precise reference markers.
    Task:
    Carefully read the user’s query, the existing answer, and all provided reference documents.
    Verify each factual statement in the answer against the documents.
    For every sentence, paragraph or specific claim that is supported by a document, add an inline reference marker in square brackets, using the format [Document Index].
    If multiple documents support the same sentence or paragraph, include multiple markers, for example: [1][3].
    If a sentence is not clearly supported by any document, leave it unmarked and do not invent or guess references. If a major claim is unsupported or contradicted, briefly flag it in a short note after the sentence, e.g. (unsupported by the provided documents).
    Do not change any word of the original answer. Only:
        Insert or adjust reference markers.
    Verify the accuracy of the information in the answer against the documents.
    If the answer contradicts the documents, flag it with a note.
    At the end, add a short “Sources used” list that maps each marker (e.g. DocA:FilePath) to the corresponding document name/identifier.

    Output:
    The answer with inline reference markers inserted in the text exactly where the supporting information is used.
    Keep the structure, headings, and formatting of the original answer as much as possible.
    I will provide:
        The original query
        The original answer
        A list of reference documents with their index and any available metadata (file path), e.g.
            [1]: File Path 1
            [2]: File Path 2
    Use only these documents as evidence and do not rely on external knowledge.

    User Query: {query}
    Original Answer: {answer}
    Reference Documents: {doc_contents}
    """
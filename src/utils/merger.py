from typing import List
from langchain_core.documents import Document

def merge_documents(documents: List[Document]) -> List[Document]:
    """
    Merge documents with the same file_path and Headers (Header 1, Header 2).
    """
    merged_docs = {}
    for doc in documents:
        doc_id = doc.metadata.get("file_path")
        for key in doc.metadata.keys():
            if isinstance(key, str) and key.startswith("Header"):
                doc_id += f" {key}-{doc.metadata[key]}"
        if doc_id not in merged_docs:
            merged_docs[doc_id] = doc

    return list(merged_docs.values())
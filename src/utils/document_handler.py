from typing import List, Tuple
from langchain_core.documents import Document


def format_documents(documents: list[Document] | List[Tuple[Document, float]], with_index: bool = True) -> str:
    """
    Format a list of documents for display.
    """
    if documents and isinstance(documents[0], tuple):
        # Tuple structure: (doc, score)
        if with_index:
            doc_contents = "\n".join([
                f"Document Index: {idx}\n{doc[0].page_content}\n['Source: '{doc[0].metadata['file_path']}]"
                for idx, doc in enumerate(documents)
            ])
        else:
            doc_contents = "\n".join([
                f"{doc[0].page_content}\n['Source: '{doc[0].metadata['file_path']}]"
                for doc in documents
            ])
    else:
        # Regular Document list
        if with_index:
            doc_contents = "\n".join([
                f"Document Index: {idx}\n{doc.page_content}\n['Source: '{doc.metadata['file_path']}]"
                for idx, doc in enumerate(documents)
            ])
        else:
            doc_contents = "\n".join([
                f"{doc.page_content}\n['Source: '{doc.metadata['file_path']}]"
                for doc in documents
            ])

    return doc_contents

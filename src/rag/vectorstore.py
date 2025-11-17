from typing import Any, Dict, List, Optional, Tuple
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_community.vectorstores import FAISS

class VectorStore:
    def __init__(self, embedding: Embeddings):       
        self.embedding = embedding
        self.vectorstore = None

    def add_documents(self, documents: List[Document]):
        """Add documents to the vectorstore."""
        if not self.vectorstore:
            self.vectorstore = FAISS.from_documents(documents, self.embedding)
        else:
            self.vectorstore.add_documents(documents)

    def as_retriever(self, search_kwargs: Dict[str, Any] = {}):
        """Return the vectorstore as a retriever."""
        return self.vectorstore.as_retriever(search_kwargs=search_kwargs)

    def search(self, query: str, k: int = 5, filter: Optional[Dict[str, Any]] = None, return_scores: bool = False) -> List[Document] | List[Tuple[Document, float]]:
        """Query the vectorstore for documents similar to the query."""
        if return_scores:
            results = self.vectorstore.similarity_search_with_score(query, k=k, filter=filter)
        else:
            results = self.vectorstore.similarity_search(query, k=k, filter=filter)
        return results

    def save_local(self, index_path: str):
        """Save the vectorstore to a local file."""
        self.vectorstore.save_local(index_path)

    def load_local(self, index_path: str, allow_dangerous_deserialization: bool = True):
        """Load the vectorstore from a local file."""
        self.vectorstore = FAISS.load_local(index_path, self.embedding, allow_dangerous_deserialization=allow_dangerous_deserialization)

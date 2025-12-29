import os
import faiss
from langchain_core.documents import Document
import numpy as np
from typing import Any, Dict, List
from langchain_community.vectorstores import FAISS
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_ollama import OllamaEmbeddings
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

# index file chunks into faiss index
class Indexer:
    def __init__(self, index_path: str):
        self.embedding_model_name = os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text:latest")
        self.base_url = os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
        self._embeddings = OllamaEmbeddings(
                model=self.embedding_model_name,
                base_url=self.base_url,
            )
        self.index_path = index_path
        if os.path.exists(index_path):
            self.vectorstore = FAISS.load_local(index_path, self._embeddings, allow_dangerous_deserialization=True)
            self.all_docs = self.get_all_docs()
        else:
            index = faiss.IndexFlatL2(len(self._embeddings.embed_query("test")))
            self.vectorstore = FAISS(self._embeddings, index, 
                docstore= InMemoryDocstore(),
                index_to_docstore_id={})   
            self.all_docs = []
    
    def index_chunks(self, chunks: Dict[int, List[Document]]) -> FAISS:
        """Index file chunks into faiss index.
        
        Args:
            chunks: Dict of file chunks to index, keyed by file_id
        """
        file_ids = list(chunks.keys())
        self.delete_file_chunks(file_ids)

        all_chunks = [chunk for chunk_list in chunks.values() for chunk in chunk_list]
        chunk_ids = [chunk.metadata['chunk_id'] for chunk in all_chunks]
        self.vectorstore.add_documents(documents=all_chunks, ids=chunk_ids)
        self.all_docs.extend(all_chunks)
        self.vectorstore.save_local(self.index_path)
        logger.info(f"Index {len(all_chunks)} chunks for {len(file_ids)} files")
        logger.info(f"Total {len(self.all_docs)} chunks in vectorstore")
        return self.vectorstore

    def delete_file_chunks(self, file_ids: List[int]) -> None:
        """Delete all chunks for a file from the index.
        
        Args:
            file_ids: List of file IDs to delete chunks for
        """
        if self.all_docs:
            existing_chunks_ids = [doc.metadata['chunk_id'] for doc in self.all_docs if doc.metadata.get("file_id") in file_ids]
            if existing_chunks_ids:
                self.vectorstore.delete(ids=existing_chunks_ids)
                logger.info(f"Delete {len(existing_chunks_ids)} chunks for file_ids: {file_ids}")
                self.all_docs = [doc for doc in self.all_docs if doc.metadata.get("file_id") not in file_ids]
                logger.info(f"{len(self.all_docs)} chunks left in vectorstore")
        self.vectorstore.save_local(self.index_path)

    def get_all_docs(self) -> List[Document]:
        """Get all documents in the index.
        
        Returns:
            List of all documents in the index
        """
        if self.vectorstore.index.ntotal == 0:
            return []
        all_docs_with_scores = self.vectorstore.similarity_search_with_relevance_scores("", k=self.vectorstore.index.ntotal)
        return [doc for doc, _ in all_docs_with_scores]

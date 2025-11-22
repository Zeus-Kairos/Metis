from enum import Enum
import logging
import os
from typing import Any, Dict, List, Tuple
from venv import logger
import numpy as np
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from src.rag.bm25_scores import BM25Scorer
from src.rag.embeddings import EmbeddingRunner
from src.rag.md_splitter import MarkdownSplitter
from src.utils.reranker import JinaAPIReranker, JinaReRanker, BgeReRanker

logger = logging.getLogger(__name__)

class RAGType(Enum):
    """
    Type of the RAG.
    """
    SIMPLE = "simple"
    QUERY_REFINED = "query_refined"
    FUSION = "fusion"
    RERANK = "rerank"
    AGENTIC = "agentic"

class RAGFlow:
    def __init__(self, file_path: str, index_path: str=None):
        self.file_path = file_path
        self.embeddings = EmbeddingRunner().embedding_model      
        self.index_path = index_path if index_path else f"./index/{file_path.split('/')[-1].split('.')[0]}"
        self.split_results = None
        self.vectorstore = None

        self.preprocess()

    def preprocess(self):
        """
        Preprocess the file and add documents to the vectorstore.
        Args:
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        """
        if not os.path.exists(self.index_path):
            markdown_splitter = MarkdownSplitter()
            split_results = markdown_splitter.split_all_markdown_files(self.file_path, include_filepath=True)
            for doc in split_results:
                sections = doc.metadata["file_path"].split("/")
                if len(sections) == 1:
                    doc.metadata["category_level_0"] = "root"
                else:
                    doc_categories = sections[:-1]
                    for i, category in enumerate(doc_categories):
                        doc.metadata[f"category_level_{i+1}"] = category

            self.split_results = split_results
            self.vectorstore = FAISS.from_documents(split_results, self.embeddings)
            self.vectorstore.save_local(self.index_path)
        
        if not self.vectorstore:
            self.vectorstore = FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)

    def retrieve(self, rag_type: RAGType, query: str, k: int=5, return_scores: bool=False) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query.

        Args:
            rag_type (RAGType): The type of RAG.
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
            return_scores (bool, optional): Whether to return the scores of the documents. Defaults to False.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        match rag_type:
            case RAGType.SIMPLE:
                results = self.simple_retrieve(query, k=k, return_scores=return_scores)
            case RAGType.QUERY_REFINED:
                results = self.simple_retrieve(query, k=k, return_scores=return_scores)
            case RAGType.FUSION:
                results = self.fusion_retrieve(query, k=k, return_scores=return_scores)
            case RAGType.RERANK:
                results = self.rerank_retrieve(query, k=k, return_scores=return_scores)
            case RAGType.AGENTIC:
                results = self.fusion_retrieve(query, k=k, return_scores=return_scores)
        return results

    def simple_retrieve(self, query: str, k: int=5, return_scores: bool=False) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query.

        Args:
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
            return_scores (bool, optional): Whether to return the scores of the documents. Defaults to False.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if return_scores:
            results = self.vectorstore.similarity_search_with_relevance_scores(query, k=k)
        else:
            results = self.vectorstore.similarity_search(query, k=k)
        return results

    def fusion_retrieve(self, query: str, k: int=5, return_scores: bool=True) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query using fusion retriever.

        Args:
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if not self.vectorstore:
            self.preprocess()

        all_docs_with_scores = self.vectorstore.similarity_search_with_relevance_scores("", k=self.vectorstore.index.ntotal)
        all_docs = [doc for doc, _ in all_docs_with_scores]
        vector_scores = [score for _, score in all_docs_with_scores]
        bm25_scorer = BM25Scorer.from_documents(all_docs)
        bm25_scores = bm25_scorer.get_scores(query)
             
        # Nomalize scores
        epsilon = 1e-6
        alpha = 0.5
        
        vector_scores = 1 - (vector_scores - np.min(vector_scores)) / (np.max(vector_scores) - np.min(vector_scores) + epsilon)
        bm25_scores = (bm25_scores - np.min(bm25_scores)) / (np.max(bm25_scores) -  np.min(bm25_scores) + epsilon)
        combined_scores = alpha * vector_scores + (1 - alpha) * bm25_scores  
        sorted_indices = np.argsort(combined_scores)[::-1]
        if return_scores:
            sorted_results = [(all_docs[i], float(combined_scores[i])) for i in sorted_indices[:k]]
        else:
            sorted_results = [all_docs[i] for i in sorted_indices[:k]]
        return sorted_results

    def rerank_retrieve(self, query: str, k: int=5, return_scores: bool=True) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query using reranked retriever.

        Args:
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if not self.vectorstore:
            self.preprocess()

        results = self.vectorstore.similarity_search(query, k=k*2)

        reranker = JinaReRanker()
        reranked_results = reranker.rerank(query, results)
        reranked_results = reranked_results[:k]
        if return_scores:
            return reranked_results
        else:
            return [doc for doc, _ in reranked_results]

    def filtered_retrieve(self, query: str, filter: Dict[str, Any], k: int=5, return_scores: bool=True) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query using filtered vectorstore.

        Args:
            query (str): The query string.
            filter (Dict[str, Any]): The filter to apply to the vectorstore.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        results = self.vectorstore.similarity_search(query, k=k, filter=filter)
        return results

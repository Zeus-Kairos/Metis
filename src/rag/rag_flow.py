from enum import Enum
import logging
import os
from typing import Any, Dict, List, Tuple
from venv import logger
import numpy as np
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from src.rag.bm25_scores import BM25Scorer
from src.utils.embeddings import EmbeddingRunner, get_active_embedding_runner
from src.utils.reranker import JinaAPIReranker, JinaReRanker, BgeReRanker
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

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
    def __init__(self, index_path: str, embedding_runner: EmbeddingRunner=None):
        self.index_path = index_path
        self.embeddings = embedding_runner.embedding_model if embedding_runner else get_active_embedding_runner().embedding_model      
        self.vectorstore = None

        logger.info(f"RAGFlow initialized with index_path: {self.index_path}")

        self.preprocess()

    def preprocess(self):
        """
        Preprocess the file and add documents to the vectorstore.
        Args:
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        """
        if not os.path.exists(self.index_path):
            raise FileNotFoundError(f"Index path {self.index_path} does not exist.")
        
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
        results = self.vectorstore.similarity_search(query, k=k*2)

        reranker = JinaReRanker()
        reranked_results = reranker.rerank(query, results)
        reranked_results = reranked_results[:k]
        if return_scores:
            return reranked_results
        else:
            return [doc for doc, _ in reranked_results]

    def filtered_retrieve(self, query: str, filter: Dict[str, Any], k: int=5, return_scores: bool=False) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query using filtered vectorstore.

        Args:
            query (str): The query string.
            filter (Dict[str, Any]): The filter to apply to the vectorstore.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if return_scores:
            results = self.vectorstore.similarity_search_with_score(query, k=k, filter=filter)
        else:
            results = self.vectorstore.similarity_search(query, k=k, filter=filter)
        return results

    def filtered_ensemble_retrieve(self, query: str, filter: Dict[str, Any], k: int=5) -> List[Document]:
        """
        Retrieve the top k documents for the query using filtered ensemble retriever.

        Args:
            query (str): The query string.
            filter (Dict[str, Any]): The filter to apply to the vectorstore.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document]: The list of documents.
        """                 
        results = self.vectorstore.similarity_search(query, k=k, filter=filter)
        if len(results) < k:
            all_docs_with_scores = self.vectorstore.similarity_search_with_relevance_scores("", k=self.vectorstore.index.ntotal)
            all_docs = [doc for doc, _ in all_docs_with_scores if all(doc.metadata.get(k) == v for k, v in filter.items())]
            logger.info(f"There are {len(all_docs)} docs with filter: {filter}")
            if len(all_docs) > 0:
                bm25_scorer = BM25Scorer.from_documents(all_docs)
                bm25_scores = bm25_scorer.get_scores(query)
                sorted_indices = np.argsort(bm25_scores)[::-1]
                sorted_results = [all_docs[i] for i in sorted_indices[:k-len(results)]]
                results += sorted_results
        return results

    def filtered_fusion_retrieve(self, query: str, filter: Dict[str, Any], k: int=5) -> List[Document]:
        """
        Retrieve the top k documents for the query using filtered fusion retriever.

        Args:
            query (str): The query string.
            filter (Dict[str, Any]): The filter to apply to the vectorstore.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document]: The list of documents.
        """                 
        all_docs_with_scores = self.vectorstore.similarity_search_with_relevance_scores("", k=self.vectorstore.index.ntotal)
        filtered = [(doc, score) for doc, score in all_docs_with_scores if all(doc.metadata.get(k) == v for k, v in filter.items())]
        filtered_docs = [doc for doc, _ in filtered]
        logger.info(f"There are {len(filtered_docs)} docs with filter: {filter}")
       
        if len(filtered_docs) > k:
            vector_scores = [score for _, score in filtered]
            bm25_scorer = BM25Scorer.from_documents(filtered_docs)
            bm25_scores = bm25_scorer.get_scores(query)

            # Nomalize scores
            epsilon = 1e-6
            alpha = 0.5
        
            vector_scores = 1 - (vector_scores - np.min(vector_scores)) / (np.max(vector_scores) - np.min(vector_scores) + epsilon)
            bm25_scores = (bm25_scores - np.min(bm25_scores)) / (np.max(bm25_scores) -  np.min(bm25_scores) + epsilon)
            combined_scores = alpha * vector_scores + (1 - alpha) * bm25_scores  
            sorted_indices = np.argsort(combined_scores)[::-1]
            sorted_results = [filtered_docs[i] for i in sorted_indices[:k]]           
            return sorted_results
        else:
            return filtered_docs

    def files_fusion_retrieve(self, query: str, file_ids: List[int], k: int=5) -> List[Document]:
        """
        Retrieve the top k documents for the query using filtered fusion retriever.

        Args:
            query (str): The query string.
            file_ids (List[int]): The list of file ids to filter.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document]: The list of documents.
        """                 
        all_docs_with_scores = self.vectorstore.similarity_search_with_relevance_scores("", k=self.vectorstore.index.ntotal)
        filtered = [(doc, score) for doc, score in all_docs_with_scores if doc.metadata.get("file_id") in file_ids]
        filtered_docs = [doc for doc, _ in filtered]
        logger.info(f"There are {len(filtered_docs)} docs with file_ids")
       
        if len(filtered_docs) > k:
            vector_scores = [score for _, score in filtered]
            bm25_scorer = BM25Scorer.from_documents(filtered_docs)
            bm25_scores = bm25_scorer.get_scores(query)

            # Nomalize scores
            epsilon = 1e-6
            alpha = 0.5
        
            vector_scores = 1 - (vector_scores - np.min(vector_scores)) / (np.max(vector_scores) - np.min(vector_scores) + epsilon)
            bm25_scores = (bm25_scores - np.min(bm25_scores)) / (np.max(bm25_scores) -  np.min(bm25_scores) + epsilon)
            combined_scores = alpha * vector_scores + (1 - alpha) * bm25_scores  
            sorted_indices = np.argsort(combined_scores)[::-1]
            sorted_results = [filtered_docs[i] for i in sorted_indices[:k]]           
            return sorted_results
        else:
            return filtered_docs

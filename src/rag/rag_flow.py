import os
from typing import List, Tuple
from langchain_core.documents import Document
from langchain_community.retrievers import BM25Retriever
from src.rag.embeddings import EmbeddingRunner
from src.rag.md_splitter import MarkdownSplitter
from src.rag.vectorstore import VectorStore
from src.utils.reranker import JinaAPIReranker, JinaReRanker, BgeReRanker
from src.utils.merger import merge_documents

class RAGFlow:
    def __init__(self, file_path: str, index_path: str=None):
        self.file_path = file_path
        self.embeddings = EmbeddingRunner().embedding_model
        self.vectorstore = VectorStore(self.embeddings)
        self.index_path = index_path if index_path else f"./index/{file_path.split('/')[-1].split('.')[0]}"
        self.split_results = None
        self.vector_retriever = None

    def preprocess(self, k: int=5):
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
            self.vectorstore.add_documents(split_results)
            self.vectorstore.save_local(self.index_path)
        
        self.vectorstore.load_local(self.index_path, allow_dangerous_deserialization=True)
        self.vector_retriever = self.vectorstore.as_retriever(search_kwargs={"k": k})

    def retrieve(self, query: str, k: int=5, return_scores: bool=False) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query.

        Args:
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
            return_scores (bool, optional): Whether to return the scores of the documents. Defaults to False.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if not self.vector_retriever:
            self.preprocess(k=k)

        results = self.vector_retriever.invoke(query)
        return results

    def fusion_retrieve(self, query: str, k: int=5, return_scores: bool=True) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query using ensemble retriever.

        Args:
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if not self.vector_retriever:
            self.preprocess(k=(k+1)//2)

        results_vector = self.vector_retriever.invoke(query)
        bm25_retriever = BM25Retriever.from_documents(self.split_results, k=k//2)
        results_bm25 = bm25_retriever.invoke(query)
        combined_results = results_vector + results_bm25
        merged_results = merge_documents(combined_results)
        return merged_results

    def reranked_retrieve(self, query: str, k: int=5, return_scores: bool=True) -> List[Document] | List[Tuple[Document, float]]:
        """
        Retrieve the top k documents for the query using reranked retriever.

        Args:
            query (str): The query string.
            k (int, optional): The number of documents to retrieve. Defaults to 5.
        
        Returns:
            List[Document] | List[Tuple[Document, float]]: The list of documents or tuples of documents and scores.
        """
        if not self.vector_retriever:
            self.preprocess(k=k)

        results_vector = self.vector_retriever.invoke(query)
        bm25_retriever = BM25Retriever.from_documents(self.split_results, k=k)
        results_bm25 = bm25_retriever.invoke(query)
        combined_results = results_vector + results_bm25
        merged_results = merge_documents(combined_results)

        re_ranker = JinaReRanker()
        reranked_results = re_ranker.rerank(query, merged_results)
        reranked_results = reranked_results[:k]
        if return_scores:
            return reranked_results
        else:
            return [doc for doc, _ in reranked_results]

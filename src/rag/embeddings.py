import logging
import os
from typing import List
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import requests

load_dotenv()

logger = logging.getLogger(__name__)

class EmbeddingRunner:
    """
    A class to manage and hold instances of embedding models from Ollama.
    
    This class provides a centralized way to initialize, access, and manage LLM models
    for embeddings generation.
    """
    
    def __init__(self, 
                 embedding_model_name: str = None, 
                 base_url: str = None):
        """
        Initialize the EmbeddingRunner with specified model configurations.
        
        Args:
            embedding_model_name: Name of the embedding model to use (default: "nomic-embed-text:latest")
            base_url: Base URL for the Ollama API (default: "http://localhost:11434")
        """
        self.embedding_model_name = embedding_model_name or os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text:latest")
        self.base_url = base_url or os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
        
        # Initialize model instances
        self._embedding_model = None
        
        # Initialize models on instantiation
        self._initialize_embedding_model()
        
    def _initialize_embedding_model(self):
        """
        Initialize the embedding model instance.
        """

        if not self.base_url.startswith("http://localhost") and not self.base_url.startswith("https://ollama.com"):
            self._embedding_model = None
            return

        try:
            self._embedding_model = OllamaEmbeddings(
                model=self.embedding_model_name,
                base_url=self.base_url,
            )
        except Exception as e:
            logger.error(f"Error initializing Ollama Embeddings Model: {e}")
            self._embedding_model = None
    
    @property
    def embedding_model(self) -> OllamaEmbeddings:
        """
        Get the initialized embedding model instance.
        
        Returns:
            An instance of OllamaEmbeddings or None if initialization failed
        """
        # Re-initialize if not already initialized
        if self._embedding_model is None:
            self._initialize_embedding_model()
        return self._embedding_model
    
    def get_embedding(self, text) -> List[float]:
        """
        Convenience method to get embeddings for text directly.
        
        Args:
            text: Text to embed
            
        Returns:
            The embedding vector or None if the model is not available
        """
        if self.embedding_model:
            try:
                return self.embedding_model.embed_query(text)
            except Exception as e:
                logger.error(f"Error generating embedding: {e}")
                raise Exception(f"Error generating embedding: {e}")
        else:
            r = requests.post(f"{self.base_url}/api/embeddings", json={
                "model": self.embedding_model_name,
                "prompt": text
            })
            return r.json()['embedding']
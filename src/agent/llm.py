import logging
import os
import inspect
from typing import List, Sequence
from langchain.tools import BaseTool
import requests
from langchain_core.messages import AIMessage
from langchain_ollama import ChatOllama, OllamaEmbeddings

logger = logging.getLogger(__name__)


class LLMRunner:
    """
    A class to manage and hold instances of both chat and embedding models from Ollama.
    
    This class provides a centralized way to initialize, access, and manage LLM models
    for both chat completion and embeddings generation.
    """
    
    def __init__(self, 
                 chat_model_name: str = None, 
                 embedding_model_name: str = None, 
                 base_url: str = None,
                 chat_temperature: float = 0.0):
        """
        Initialize the LLMRunner with specified model configurations.
        
        Args:
            chat_model_name: Name of the chat model to use (default: "llama3.1:latest")
            embedding_model_name: Name of the embedding model to use (default: "mxbai-embed-large:latest")
            base_url: Base URL for the Ollama API (default: "http://localhost:11434")
            chat_temperature: Temperature setting for the chat model (default: 0.0)
        """
        self.chat_model_name = chat_model_name or os.environ.get("OLLAMA_MODEL", "qwen3:8b")
        self.embedding_model_name = embedding_model_name or os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text:latest")
        self.base_url = base_url or os.environ.get("OLLAMA_BASE_URL", "http://localhost:11434")
        self.chat_temperature = chat_temperature
        
        # Initialize model instances
        self._chat_model = None
        self._embedding_model = None
        self.tokens = {}
        
        # Initialize models on instantiation
        self.initialize_models()
    
    def initialize_models(self):
        """
        Initialize both the chat model and embedding model instances.
        """
        self._initialize_chat_model()
        self._initialize_embedding_model()
    
    def _initialize_chat_model(self):
        """
        Initialize the chat model instance.
        """

        if not self.base_url.startswith("http://localhost"):
            self._chat_model = None
            return

        try:
            self._chat_model = ChatOllama(
                model=self.chat_model_name,
                base_url=self.base_url,
                temperature=self.chat_temperature,
            )
        except Exception as e:
            logger.error(f"Error initializing Ollama Chat Model: {e}")
            self._chat_model = None
    
    def _initialize_embedding_model(self):
        """
        Initialize the embedding model instance.
        """

        if not self.base_url.startswith("http://localhost"):
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
    def chat_model(self) -> ChatOllama:
        """
        Get the initialized chat model instance.
        
        Returns:
            An instance of ChatOllama or None if initialization failed
        """
        # Re-initialize if not already initialized
        if self._chat_model is None:
            self._initialize_chat_model()
        return self._chat_model

    def chat_model_with_tools(self, tools: Sequence[BaseTool]):
        """
        Get the initialized chat model instance with tools bound.
        
        Args:
            tools: Sequence of BaseTool instances to bind to the chat model
        
        Returns:
            An instance of ChatOllama or None if initialization failed
        """
        # Re-initialize if not already initialized
        if self._chat_model is None:
            self._initialize_chat_model()
        return self._chat_model.bind_tools(tools)
    
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

    def reset(self):
        """
        Reset the LLMRunner by re-initializing both models.
        """
        self.tokens = {}
    
    def invoke(self, messages, tools: Sequence[BaseTool] = None, **kwargs):
        """
        Convenience method to invoke the chat model directly.
        
        Args:
            messages: Messages to pass to the chat model
            tools: Sequence of BaseTool instances to bind to the chat model
            **kwargs: Additional parameters to pass to the chat model
            
        Returns:
            The response from the chat model or None if the model is not available
        """

        if self.chat_model:
            try:
                if tools:
                    logger.info(f"Invoked chat model {self.chat_model.model} with tools [{', '.join([tool.name for tool in tools])}]")
                    response = self.chat_model_with_tools(tools).invoke(messages, **kwargs)              
                    if hasattr(response, 'tool_calls') and response.tool_calls:
                        for tool_call in response.tool_calls:
                            logger.info(tool_call)
                else:
                    response = self.chat_model.invoke(messages, **kwargs)
                frame = inspect.currentframe().f_back
                caller_name = frame.f_code.co_name.lstrip("_") if frame else "unknown"
                logger.info(f"Metadata for {caller_name}: {response.usage_metadata}")
                if "total" not in self.tokens:
                    self.tokens["total"] = response.usage_metadata.copy()
                else:
                    for key, value in response.usage_metadata.items():
                        self.tokens["total"][key] += value             
                self.tokens[caller_name] = response.usage_metadata
                return response
            except Exception as e:
                logger.error(f"Error invoking chat model: {e}")
                raise Exception(f"Error invoking chat model: {e}")
        else:
            r = requests.post(f"{self.base_url}/api/generate", json={
                "model": self.chat_model_name,
                "prompt": messages[0].content,
                "stream": False
            })
            response = AIMessage(r.json()['response'])
            return response
    
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
                "model": "mxbai-embed-large:latest",
                "prompt": text
            })
            return r.json()['embedding']

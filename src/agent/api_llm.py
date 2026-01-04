import logging
import os
import inspect
from typing import List, Sequence, Optional, Union
from langchain.tools import BaseTool
import requests
from langchain.chat_models import init_chat_model
from src.memory.memory import MemoryManager
from src.agent.llm import LLMRunner

logger = logging.getLogger(__name__)

class ApiLLMRunner(LLMRunner):
    """
    A class to manage and hold instances of both chat and embedding models
    using user-specific API configurations from different providers.
    
    This class extends LLMRunner to support API-based models from providers
    like OpenAI, Anthropic, Cohere, Mistral, etc., using user-configured
    API keys and settings.
    """
    
    def __init__(self, user_id: int):
        """
        Initialize the ApiLLMRunner with the user's API configuration.
        
        Args:
            user_id: User's ID to retrieve the API configuration
        """
        # Initialize memory manager to fetch user config
        self.memory_manager = MemoryManager()
        self.user_id = user_id
        
        # Get user configuration from memory manager
        self.user_config = self.memory_manager.get_user_configuration(user_id)
        
        # Set default values if no config is found
        if not self.user_config:
            logger.warning(f"No API configuration found for user {user_id}, using default Ollama settings")
            super().__init__()
            return
        
        # Extract configuration values
        self.api_key = self.user_config.get("api_key")
        self.model_provider = self.user_config.get("model_provider", "openai").lower()
        self.llm_model = self.user_config.get("llm_model")
        self.embedding_model_name = self.user_config.get("embedding_model")
        self.api_base_url = self.user_config.get("api_base_url")
        
        # Initialize base class with None values (we'll override models later)
        super().__init__()
        
        # Initialize models based on user configuration
        self.initialize_models()
    
    def initialize_models(self):
        """
        Initialize both the chat model and embedding model instances
        based on the user's API configuration.
        """
        self._initialize_chat_model()
        self._initialize_embedding_model()
    
    def _initialize_chat_model(self):
        """
        Initialize the chat model instance based on the user's provider.
        """
        if not self.user_config or not self.api_key:
            super()._initialize_chat_model()
            return
        
        try:
            self._chat_model = init_chat_model(
                model_provider=self.model_provider,
                model=self.llm_model,
                api_key=self.api_key,
                base_url=self.api_base_url,
                temperature=self.chat_temperature,
            )
        except Exception as e:
            logger.error(f"Error initializing {self.model_provider} Chat Model: {e}")
            self._chat_model = None

# Create a dictionary to store ApiLLMRunner instances per user
api_llm_runners = {}
active_LLMRunner = LLMRunner()

def get_api_llm_runner(user_id: int) -> ApiLLMRunner:
    """
    Get or create an ApiLLMRunner instance for the specified user.
    
    Args:
        user_id: User's ID
        
    Returns:
        ApiLLMRunner instance for the user
    """
    global active_LLMRunner
    if user_id not in api_llm_runners:
        # Create a new ApiLLMRunner instance for this user with their ID
        api_llm_runners[user_id] = ApiLLMRunner(user_id=user_id)
    active_LLMRunner = api_llm_runners[user_id]
    return api_llm_runners[user_id]

def get_active_llm_runner() -> Union[LLMRunner, ApiLLMRunner]:
    """
    Get the currently active LLM runner instance.
    This function provides a reliable way to access the most recent active runner
    from outside this module, without needing a user ID.
    
    Returns:
        The currently active LLM runner instance (either LLMRunner or ApiLLMRunner)
    """
    global active_LLMRunner
    return active_LLMRunner
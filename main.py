import os
import sys
import threading
import warnings

import uvicorn
from src.agent.rag_agent import RAGAgent, RAGType
from src.utils.logging_config import setup_logging
from dotenv import load_dotenv

load_dotenv()

log_level = setup_logging()

# Ignore all UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

try:
    rag_type_str = os.getenv("RAG_TYPE", "simple").lower()
    rag_type = RAGType(rag_type_str)
except ValueError:
    rag_type = RAGType.SIMPLE
    
rag_k = int(os.getenv("RAG_K", 10))

# API server configuration
API_HOST = os.getenv("API_HOST", "127.0.0.1")
API_PORT = int(os.getenv("API_PORT", "8000"))

# Start the API server in a separate thread
def start_api_server():
    """Start the FastAPI server"""
    uvicorn.run(
        "src.api.main:app",
        host=API_HOST,
        port=API_PORT,
        log_level=log_level.lower(),
        reload=False
    )

try:   
    api_thread = threading.Thread(target=start_api_server, daemon=True)
    api_thread.start()
    
    print(f"API server started at http://{API_HOST}:{API_PORT}")
    print(f"Welcome to the Metis Agent with {rag_type.name} RAG!")
    print("Please ask anything you like. Type 'q' to quit.")
    
    # Keep the main thread running to prevent daemon thread from exiting
    while True:
        user_input = input()
        if user_input.strip().lower() == 'q':
            print("Shutting down...")
            break

except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
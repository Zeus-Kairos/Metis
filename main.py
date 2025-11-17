import os
import sys
import warnings
from src.agent.rag_agent import RAGAgent, RAGType
from dotenv import load_dotenv

load_dotenv()

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

try:   
    agent = RAGAgent(rag_type, rag_k)

    print(f"Welcome to the Metis Agent with {rag_type.name} RAG!")
    print("Please ask anything you like (or 'q' to quit)")
    while True:       
        query = input("You: ")      
        if query.lower() == 'q':
            break

        print("Metis:")

        for chunk in agent.chat(query, knowledge_base_id=1):
            for key, value in chunk.items():
                if key == "stage":
                    print(f"{value}\n")
                elif key == "response":
                    print(value, end="", flush=True)
        print(f"\n")     

except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
import os
from dotenv import load_dotenv
from src.agent.rag_agent import RAGAgent, RAGType

load_dotenv()

try:
    rag_type_str = os.getenv("RAG_TYPE", "simple").lower()
    rag_type = RAGType(rag_type_str)
except ValueError:
    rag_type = RAGType.SIMPLE
    
rag_k = int(os.getenv("RAG_K", 10))
# Create the agent instance that will be exported for LangGraph
agent = RAGAgent(rag_type=rag_type, rag_k=rag_k, on_langgraph_server=True)

# Export the graph for LangGraph
# This allows LangGraph to visualize and interact with our agent's workflow
graph = agent.graph

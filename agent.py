import os
from dotenv import load_dotenv
from src.agent.rag_agent import RAGAgent

load_dotenv()

# Create the agent instance that will be exported for LangGraph
agent = RAGAgent(on_langgraph_server=True)

# Export the graph for LangGraph
# This allows LangGraph to visualize and interact with our agent's workflow
graph = agent.builder.compile()

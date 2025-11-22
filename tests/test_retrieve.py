import sys
import os

# Add the parent directory to sys.path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_flow import RAGFlow

query = "how to measure gain compression?"
filters = {"category_level_1": "Applications", "file_path": "Applications/Gain_Compression_Application.md"}
rag_flow = RAGFlow("Docs/VNA_Help_MD")
results = rag_flow.filtered_retrieve(query, filters)
print(results)
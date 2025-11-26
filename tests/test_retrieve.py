import sys
import os

# Add the parent directory to sys.path so we can import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.rag.rag_flow import RAGFlow

test_case_1 = {
    "query": "how to measure gain compression?",
    "filters": {"category_level_1": "Applications", "file_path": "Applications/Gain_Compression_Application.md"},
}
test_case_2 = {
    "query": "gain compression measurement steps",
    "filters": {'category_level_1': 'Applications', 'file_path': 'Applications/Gain_Compression_Application.md'},
}
test_case_3 = {
    "query": "noise",
    "filters": {'category_level_1': 'Programming', 'category_level_2': 'GP-IB_Command_Finder'},
}
test_case_4 = {
    "query": "IF bandwidth SCPI commands",
    "filters": {'category_level_1': 'Programming', 'category_level_2': 'GPIB_Command_Finder'},
}
test_cases = [test_case_1, test_case_2, test_case_3, test_case_4]
rag_flow = RAGFlow("Docs/VNA_Help_MD")
# for test_case in test_cases:
#     results = rag_flow.filtered_retrieve(test_case["query"], test_case["filters"])
#     print(f"Retrieve {len(results)} results for query: {test_case['query']}")
#     print("\n")

for test_case in test_cases:
    results = rag_flow.filtered_ensemble_retrieve(test_case["query"], test_case["filters"])
    print(f"Retrieve {len(results)} results for query: {test_case['query']}")
    print("\n")

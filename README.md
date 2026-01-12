# Metis: RAG Application for VNA Help Documentation

## Project Overview
Metis is a Retrieval-Augmented Generation (RAG) application designed to provide intelligent query responses. The system leverages Large Language Models (LLMs) with vector search capabilities to deliver accurate and contextually relevant answers to user queries.

### Key Features
- Natural language query processing and refinement
- Semantic search over VNA documentation
- Document chunking and embedding for efficient retrieval
- Response generation with source attribution
- Support for different reranking strategies (local models and API-based)
- Knowledge base indexing and management
- Configurable logging and error handling

## Installation

### Prerequisites
- Python 3.10 or higher
- Conda package manager

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd Metis
   ```

2. **Create and Activate Conda Environment**
   ```bash
   conda create -n metis python=3.13
   conda activate metis
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Environment Variables
The application uses environment variables for configuration. A template file `.env.example` is provided with all required variables:

1. **Copy the example environment file**
   ```bash
   copy .env.example .env  # On Windows
   # OR
   cp .env.example .env    # On Linux/Mac
   ```

2. **Edit the `.env` file** to add your personal API keys and configure settings according to your needs.

### Environment Variables Reference

- **LLM Configuration**
  - `LLM_API_KEY` - Required for LLM cloud model access
  - `LLM_MODEL` - Model to use (default: qwen3:8b)
  - `EMBED_MODEL` - Embedding model to use (default: nomic-embed-text:latest)
  - `LLM_BASE_URL` - LLM API base URL (default: http://localhost:11434)

- **Logging Configuration**
  - `LOG_LEVEL` - Logging verbosity (INFO, DEBUG, WARNING, ERROR)

- **RAG Configuration**
  - `RAG_TYPE` - Type of RAG approach to use (fusion, simple, query_refined, rerank)
  - `RAG_K` - Number of documents to retrieve during search

- **LangSmith Configuration**
  - `LANGSMITH_TRACING` - Enable/disable LangSmith tracing (true/false)
  - `LANGSMITH_API_KEY` - Your LangSmith API key
  - `LANGSMITH_ENDPOINT` - LangSmith API endpoint
  - `LANGSMITH_PROJECT` - Name of your LangSmith project

- **Reranking Configuration**
  - `JINA_API_KEY` - Required if using Jina API reranker

### Configuration Files
- **`langgraph.json`** - Contains LangGraph server configuration
- **`src/utils/logging_config.py`** - Defines logging behavior and verbosity levels

## File Structure

```
Metis/
├── Docs/                      # Documentation directory
│   ├── VNA_Help_MD/           # VNA help documentation files
│   │   ├── Applications/      # Application-specific documentation
│   │   ├── Tutorials/         # Tutorial documentation
│   │   └── ...                # Other documentation sections
│   ├── knowledge_base_index.json  # Index of knowledge base entries
│   └── vna_help_folder_structure.md  # Documentation structure description
├── src/                       # Source code directory
│   ├── agent/                 # Agent components
│   │   ├── llm.py             # LLM integration and configuration
│   │   ├── prompts.py         # Prompt templates
│   │   ├── rag_agent.py       # RAG agent implementation
│   │   └── tools.py           # Agent tools
│   ├── rag/                   # RAG components
│   │   ├── embeddings.py      # Text embedding functionality
│   │   ├── md_splitter.py     # Markdown document chunking
│   │   ├── rag_flow.py        # RAG workflow implementation
│   │   └── vectorstore.py     # Vector database integration
│   └── utils/                 # Utility functions
│       ├── html_parser.py     # HTML parsing utilities
│       ├── knowledge_base_reader.py  # Knowledge base index reader
│       ├── logging_config.py  # Logging configuration
│       ├── merger.py          # Document merging utilities
│       └── reranker.py        # Reranking implementations
├── agent.py                   # LangGraph server agent entry point
├── main.py                    # Application main entry point
├── langgraph.json             # LangGraph server configuration
├── requirements.txt           # Python dependencies
└── .gitignore                 # Git ignore file
```

## Usage

### Starting the Application in console
```bash
python main.py
```

### Starting the Application in local LangGraph server
```bash
langgraph dev
```

## Components

### RAG Flow
The RAG (Retrieval-Augmented Generation) flow handles the core functionality of retrieving relevant information from the knowledge base and generating responses.

### Agent
The agent orchestrates the workflow, manages state, and decides on appropriate actions based on user queries.

### Reranking
The system supports multiple reranking strategies:
- BGE Reranker
- Jina Local Model Reranker
- Jina API Reranker

### Knowledge Base
The knowledge base consists of indexed VNA documentation that is used for information retrieval.
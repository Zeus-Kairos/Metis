# Metis

## Project Overview

Metis is an advanced Retrieval-Augmented Generation (RAG) application that enables users to interact with AI using their own knowledge bases and documents. It provides a seamless interface for uploading documents, configuring AI models, and engaging in intelligent conversations powered by state-of-the-art language models.

### Key Features

- **Document Management**: Upload, process, and index various document types (PDF, DOCX, PPTX, TXT, MD, HTML, CSV, XLSX)
- **Configurable AI Models**: Support for multiple LLM and embedding providers with customizable settings
- **Intelligent RAG System**: Advanced retrieval with agentic RAG workflow
- **User-Friendly Interface**: Modern React-based UI with chat interface and knowledgebase browser
- **Secure Authentication**: JWT-based user authentication system
- **Knowledgebase Organization**: Browse and manage your uploaded documents in customized knowledgebases
- **Conversation History**: Persistent conversation threads with knowledgebase context

## Installation

### Prerequisites

- Python 3.10+ with conda environment
- Node.js 18+ for frontend development
- PostgreSQL database 
- Ollama or other LLM provider access

### Backend Setup

1. **Create and activate conda environment**:
   ```bash
   conda create -n metis python=3.13
   conda activate metis
   ```

2. **Install dependencies**:
   ```bash
   cd c:\Apps\Metis
   pip install -r requirements.txt
   ```

3. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

4. **Run the backend server**:
   ```bash
   python main.py
   ```

### Frontend Setup

1. **Install npm dependencies**:
   ```bash
   cd c:\Apps\Metis\
   npm install
   ```

2. **Build and run the frontend**:
   ```bash
   npm run dev
   ```

## Configuration

### Environment Variables

The following environment variables are required for the application to function properly:

| Variable | Description | Default |
|----------|-------------|---------|
| `DB_URI` | PostgreSQL database connection string | - |
| `SECRET_KEY` | Secret key for JWT token generation | - |
| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | `INFO` |
| `RAG_TYPE` | RAG retrieval type (simple, query_refined, fusion, rerank) | `fusion` |
| `RAG_K` | Number of documents to retrieve | `10` |

### AI Model Configuration

Metis allows you to configure different AI models for both LLM and embedding services:

1. **Access the API Configuration dialog** from the main application
2. Enter your model provider information
3. Set API keys and model names for both LLM and embedding services
4. Configure API base URLs if needed
5. Save your configuration

### File Upload Configuration

Customize file upload settings in the `.env` file:

- `BASE_UPLOAD_DIR`: Directory for storing uploaded files
- `SUPPORTED_FORMATS`: Comma-separated list of supported file formats
- `MAX_FILE_SIZE`: Maximum file size in bytes (default: 100MB)
- `MAX_FILES_PER_UPLOAD`: Maximum number of files per upload

## Basic Usage

### 1. User Registration and Login

- Register a new user account or log in with existing credentials
- Authentication is handled via JWT tokens

### 2. Knowledgebase Management and Document Processing

- Switch to the knowledgebase browser
- Select or create a knowledgebase
- Create folder hierarchies within the knowledgebase
- Upload one or more supported documents
- Documents will be uploaded, parsed, chunked, and indexed for retrieval

### 3. Configure AI Models

- Click on the user icon in the top left corner
- Enter your LLM and embedding provider details
- Save the configuration

### 4. Start a Conversation

- Select an existing conversation or create a new one
- Type your question in the message input field and send
- Metis will retrieve relevant information from your documents and generate a response

### 5. Explore Conversation History

- Switch between conversation threads using the sidebar
- View previous messages and responses
- Continue conversations from where you left off


## Tech Stack

- **Python 3.10+**: Core programming language
- **FastAPI**: Web framework for building APIs
- **LangChain**: Framework for developing LLM applications
- **LangGraph**: For building stateful, multi-actor applications
- **PostgreSQL**: Database for storing user data and configurations
- **React 18+**: UI framework

## Project Structure

```
src/
├── agent/              # AI agent components
│   ├── api_llm.py      # API-based LLM implementation
│   ├── llm.py          # Core LLM functionality
│   ├── prompts.py      # Prompt templates
│   ├── rag_agent.py    # RAG agent implementation
│   ├── researcher.py   # Researcher agent
│   └── tools.py        # Agent tools
├── api/                # Backend API
│   └── main.py         # FastAPI application
├── file_process/       # File handling
│   ├── file_parser.py  # Document parsing
│   ├── file_splitter.py # Document splitting
│   └── indexer.py      # Document indexing
├── memory/             # Data storage
│   ├── knowledgebase.py # Knowledgebase management
│   ├── memory.py       # Main memory manager
│   └── thread.py       # Conversation thread management
├── rag/                # RAG flow
│   └── rag_flow.py     # RAG pipeline implementation
├── ui/                 # Frontend UI
│   ├── App.jsx         # Main React component
│   └── main.jsx        # React entry point
└── utils/              # Utility functions
    ├── embeddings.py   # Embedding utilities
    └── logging_config.py # Logging configuration
```

## Development

### Running Backend Tests

```bash
pytest
```

### Running Frontend Tests

```bash
cd src/ui
npm test
```

### Linting and Formatting

```bash
# Backend
pylint src/
black src/

# Frontend
cd src/ui
npm run lint
```

## Deployment

For production deployment, refer to the `DEPLOYMENT_GUIDE.md` file for detailed instructions on setting up the application in a production environment.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Run the tests
5. Submit a pull request

## License

[MIT License](LICENSE)

## Support

For issues, questions, or feature requests, please open an issue on the GitHub repository.

## Acknowledgements

- Built with FastAPI, React, and LangChain
- Supports various LLM and embedding providers
- Document processing powered by multiple open-source libraries

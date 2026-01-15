# Metis

## Project Overview

Metis is an advanced Retrieval-Augmented Generation (RAG) application that enables users to interact with AI using their own knowledge bases and documents. It provides a seamless interface for uploading documents, configuring AI models, and engaging in intelligent conversations powered by state-of-the-art language models.

### Key Features

- **Document Management**: Upload, process, and index various document types (PDF, DOCX, PPTX, TXT, MD, HTML, CSV, XLSX)
- **Configurable AI Models**: Support for multiple LLM and embedding providers with customizable settings
- **Intelligent RAG System**: Advanced retrieval with agentic RAG workflow
- **User-Friendly Interface**: Modern React-based UI with chat interface and knowledgebase browser
- **Knowledgebase Organization**: Browse and manage your uploaded documents in customized knowledgebases
- **Secure Authentication**: JWT-based user authentication system
- **Conversation History**: Persistent conversation threads with knowledgebase context

## Installation

### Prerequisites

- [MiniConda](https://www.anaconda.com/docs/getting-started/miniconda/install)
- [Node.js 18+](https://nodejs.org/en/download)
- [PostgreSQL database](https://www.postgresql.org/download/)
- [Ollama](https://ollama.com/download) or other LLM provider access
- Git (for cloning the repository)

### Windows (PowerShell) One-Command Install (Recommended)

Download the latest installer script:

- **`install.ps1`**: [`https://raw.githubusercontent.com/Zeus-Kairos/Metis/main/install.ps1`](https://raw.githubusercontent.com/Zeus-Kairos/Metis/main/install.ps1)

Save it into the folder where you want to install or manage Metis (for example, `c:\Apps\Metis`), then from that folder run:

```powershell
# If you encounter execution policy issues, run this first in an elevated PowerShell:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

.\install.ps1 -DbUser postgres -PromptDbPassword -DatabaseName metis_db
```

Customizing the Conda env name:

```powershell
.\install.ps1 -EnvName metis-dev -DbUser postgres -PromptDbPassword -DatabaseName metis_db
```

Installing into a custom path (repo root):

```powershell
# Run the script from anywhere, but point it at your repo root folder:
.\install.ps1 -InstallPath C:\Apps\Metis -DbUser postgres -PromptDbPassword -DatabaseName metis_db
```

What it does:
- Installs backend deps (via Conda + `pip install -r requirements.txt`, or system Python if `-SkipConda`)
- Installs frontend deps (`npm install`, unless `-SkipFrontend` is used)
- Sets up the PostgreSQL database + `vector` extension (using `psql` directly, unless `-SkipDb` is used)
- Creates a local `.env` file if missing (with a generated `SECRET_KEY` and a `DB_URI` based on your DB args)

#### `install.ps1` flags (full list)

- **Repository / path**
  - **`-InstallPath <path>`**: Target Metis repo root. If it doesn’t exist, the folder is created; if it isn’t a repo yet, the script will clone into it.
  - **`-RepoUrl <url>`**: Git URL to clone when `InstallPath` is not already a repo. Default: `https://github.com/Zeus-Kairos/Metis.git`.
  - **`-SkipClone`**: Do not clone even if `InstallPath` doesn’t look like a repo; instead, fail with an error.

- **Conda / Python**
  - **`-EnvName <name>`**: Conda environment name to create/use (default: `metis`).
  - **`-PythonVersion <version>`**: Python version for the Conda env (default: `3.13`).
  - **`-SkipConda`**: Skip Conda entirely and use the system `python` + `pip`.

- **Database (PostgreSQL)**
  - **`-SkipDb`**: Skip database creation and `vector` extension setup.
  - **`-DbHost <host>`**: Database host (default: `localhost`).
  - **`-DbPort <port>`**: Database port (default: `5432`).
  - **`-DbUser <user>`**: Database user (default: `postgres`).
  - **`-DbPassword <password>`**: Database password (optional; if omitted, use `-PromptDbPassword`).
  - **`-DatabaseName <name>`**: Database name to create/use (default: `metis_db`).
  - **`-PromptDbPassword`**: Prompt interactively for the PostgreSQL password.

- **Frontend**
  - **`-SkipFrontend`**: Skip `npm install`.

- **Environment file**
  - **`-ForceEnvOverwrite`**: Overwrite an existing `.env` instead of leaving it untouched.

- **Verbosity**
  - **`-Verbose`**: PowerShell common parameter; when supplied, `pip` runs with `-v` for more detailed install logs.

### Step-by-Step Installation (Advanced / Cross-Platform)

#### Clone the Repository

1. **Create project directory and clone the code**:
   ```bash
   mkdir -p c:\Apps\Metis
   cd c:\Apps
   git clone https://github.com/Zeus-Kairos/Metis.git
   ```

#### Backend Setup (Manual)

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

3. **Set up PostgreSQL database**:
   
   ##### On Linux/macOS
   ```bash
   # Make the script executable
   chmod +x setup_db.sh
   
   # Run the database setup script
   ./setup_db.sh -U postgres -W -d metis_db
   ```
   
   ##### On Windows
   
   **Option 1: Using Git Bash** (recommended if you have Git installed)
   ```bash
   # Run the script directly in Git Bash
   ./setup_db.sh -U postgres -W -d metis_db
   ```
   
   **Option 2: Using Windows Subsystem for Linux (WSL)**
   ```bash
   # Run from WSL terminal
   ./setup_db.sh -U postgres -W -d metis_db
   ```
   
   **Option 3: Using PowerShell (Recommended)**
   ```powershell
   # If you encounter execution policy issues, run this first in an elevated PowerShell:
   # Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   
   # Run the PowerShell setup script with password prompt
   .\setup_db.ps1 -User postgres -PromptPassword -DatabaseName metis_db
   
   # Optional: Specify host and port explicitly
   # .\setup_db.ps1 -DbHost localhost -Port 5432 -User postgres -PromptPassword -DatabaseName metis_db
   ```
   
   **Option 4: Manual PowerShell Commands**
   ```powershell
   # Add PostgreSQL bin directory to PATH (adjust version as needed)
   $env:PATH += ";C:\Program Files\PostgreSQL\16\bin"
   
   # Create database and enable vector extension
   psql -h localhost -p 5432 -U postgres -c "CREATE DATABASE metis_db"
   psql -h localhost -p 5432 -U postgres -d metis_db -c "CREATE EXTENSION IF NOT EXISTS vector"
   ```
   
   **Note**: Ensure PostgreSQL is installed and `psql` is in your PATH. For Windows, PostgreSQL usually installs to `C:\Program Files\PostgreSQL\<version>\bin`.

4. **Configure environment variables**:
   ```bash
   # Create a .env file (the installer script can do this for you)
   # Edit .env file with your configuration, including the DB_URI from the database setup
   ```

5. **Run the backend server**:
   ```bash
   python main.py
   ```

#### Frontend Setup (Manual)

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

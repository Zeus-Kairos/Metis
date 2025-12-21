import os
import dotenv

# Load environment variables
dotenv.load_dotenv()

# Define supported file formats from environment or use defaults
SUPPORTED_FORMATS = set(os.getenv("SUPPORTED_FORMATS", ".txt,.pdf,.md,.docx,.pptx,.xlsx,.html,.htm,.csv").split(","))

# Define maximum file size from environment or use default (100MB)
MAX_FILE_SIZE = int(os.getenv("MAX_FILE_SIZE", str(100 * 1024 * 1024)))

MAX_FILES_PER_UPLOAD = int(os.getenv("MAX_FILES_PER_UPLOAD", "20"))

# Base upload directory from environment or use default
BASE_UPLOAD_DIR = os.getenv("BASE_UPLOAD_DIR", "uploads")

def get_upload_dir(user_id: int, knowledge_base: str, directory: str) -> str:
    """Generate a unique upload directory for the given user_id.
    
    Args:
        user_id: User ID
        knowledge_base: Knowledgebase name
        directory: Directory name
        
    Returns:
        Unique upload directory as a string
    """
    return os.path.join(BASE_UPLOAD_DIR, str(user_id), knowledge_base, "origin", directory)

def get_index_path(user_id: int, knowledgebase_name: str) -> str:
    """Generate a unique index path for the given user_id and knowledgebase_name.
    
    Args:
        user_id: User ID
        knowledgebase_name: Knowledgebase name
        
    Returns:
        Unique index path as a string
    """
    return f"./index/{user_id}/{knowledgebase_name}"

import os
import sys
import json
import glob
import shutil

from datetime import datetime, timezone, timedelta
from typing import Annotated, List, Optional, Dict, Any

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Body, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from contextlib import asynccontextmanager
from fastapi.responses import StreamingResponse

from src.file_process.utils import get_upload_dir, get_parsed_path
from src.agent.rag_agent import RAGAgent, RAGType
from src.file_process.pipeline import FileProcessingPipeline
from src.memory.memory import MemoryManager
from src.memory.thread import ThreadManager
from src.utils.logging_config import get_logger
from src.api.thread import router as thread_router

logger = get_logger(__name__)

# Authentication settings
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable must be set")

# Password hashing context
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

# Pydantic models for authentication
class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    id: int
    username: str
    email: str
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

app = FastAPI(title="Metis API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include thread-related endpoints
app.include_router(thread_router)

# Initialize MemoryManager
memory_manager = MemoryManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Clean up resources when the application shuts down."""
    import logging
    logger = logging.getLogger(__name__)
    yield
    logger.info("Shutting down MemoryManager...")
    if hasattr(memory_manager, 'connection_pool'):
        try:
            memory_manager.connection_pool.close()
            logger.info("Database connection pool closed successfully")
        except Exception as e:
            logger.error(f"Error closing database connection pool: {e}")

# Authentication helper functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user_by_username(username: str):
    """Get user from database by username."""
    if not memory_manager.conn_str:
        raise ValueError("Cannot get user in in-memory mode")
    
    with memory_manager.connection_pool.connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, username, email, password FROM users WHERE username = %s",
                (username,)
            )
            result = cur.fetchone()
            if result:
                return UserInDB(
                    id=result[0],
                    username=result[1],
                    email=result[2],
                    hashed_password=result[3],
                    disabled=False  # Default to enabled
                )
            return None

def authenticate_user(username: str, password: str):
    """Authenticate a user with username and password."""
    user = get_user_by_username(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """Create a JWT access token."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """Get the current user from the token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user_by_username(username)
    if user is None:
        raise credentials_exception
    
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    """Get the current active user."""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/api/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    """Login endpoint to get JWT access token."""
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "user_id": user.id},
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

# API endpoint for creating users
@app.post("/api/users")
async def create_user(
    user_data: UserCreate
):
    """Create a new user account."""
    try:
        # Call the create_user method
        user_id = memory_manager.create_user(user_data.username, user_data.email, user_data.password)
        return {
            "success": True,
            "user_id": user_id,
            "message": "User created successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint for getting current user
@app.get("/api/users/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    """Get current user information."""
    return current_user

# API endpoint for deleting a user
@app.delete("/api/users/me")
async def delete_user(current_user: Annotated[User, Depends(get_current_active_user)]):
    """Delete the current user account."""
    try:
        # Call the delete_user method
        deleted = memory_manager.delete_user(current_user.id)
        if not deleted:
            raise HTTPException(status_code=404, detail="User not found")
        return {
            "success": True,
            "message": "User deleted successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint for creating a knowledge base
@app.post("/api/knowledgebase")
async def create_knowledgebase(
    current_user: Annotated[User, Depends(get_current_active_user)],
    name: str = Body(..., description="Knowledge base name"),
    description: Optional[str] = Body(None, description="Knowledge base description"),
    navigation: Optional[Dict[str, Any]] = Body(None, description="Knowledge base navigation structure")
):
    """Create a new knowledge base for the user."""
    try:
        # Call the create_knowledgebase method
        knowledgebase_id = memory_manager.create_knowledgebase(current_user.id, name, description, navigation)
        return {
            "success": True,
            "knowledgebase_id": knowledgebase_id,
            "message": "Knowledge base created successfully"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint to list all knowledgebases for the current user
@app.get("/api/knowledgebase")
async def list_knowledgebases(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """List all knowledgebases for the current user."""
    try:
        knowledgebases = memory_manager.get_all_knowledgebases(current_user.id)
            
        return {
            "success": True,
            "knowledgebases": knowledgebases
        }
    except Exception as e:
        logger.error(f"Error listing knowledgebases: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint to rename a knowledgebase
@app.put("/api/knowledgebase/{kb_id}/rename")
async def rename_knowledgebase(
    kb_id: int,
    rename_data: dict,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Rename a knowledgebase."""
    try:
        if "name" not in rename_data:
            return {
                "success": False,
                "message": "Name field is required"
            }
        
        new_name = rename_data["name"]
        
        # Use the MemoryManager method to rename the knowledgebase
        success = memory_manager.rename_knowledgebase(current_user.id, kb_id, new_name)
        if success:
            return {
                "success": True,
                "message": "Knowledgebase renamed successfully"
            }
        return {
            "success": False,
            "message": "Failed to rename knowledgebase"
        }
    except ValueError as e:
        # Handle unique constraint violations
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error renaming knowledgebase: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint to set a knowledgebase as active
@app.patch("/api/knowledgebase/{kb_id}/active")
async def set_active_knowledgebase(
    kb_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Set a knowledgebase as active, deactivating all other knowledgebases for the user."""
    try:
        # Use the MemoryManager method to set the knowledgebase as active
        success = memory_manager.set_active_knowledgebase(current_user.id, kb_id)
        if success:
            return {
                "success": True,
                "message": "Knowledgebase set as active successfully"
            }
        return {
            "success": False,
            "message": "Failed to set knowledgebase as active"
        }
    except Exception as e:
        logger.error(f"Error setting active knowledgebase: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# Knowledgebase endpoints
@app.get("/api/knowledgebase/list")
async def list_directory(
    current_user: Annotated[User, Depends(get_current_active_user)],
    path: str = "",
    knowledge_base: str = "default"
):
    """List directory contents for a knowledgebase"""
    try:       
        # Get the upload directory path
        upload_dir = get_upload_dir(current_user.id, knowledge_base, path)
        
        # Check if directory exists
        if not os.path.exists(upload_dir):
            return {
                "success": True,
                "folders": [],
                "files": []
            }
        
        # Get directory contents
        items = os.listdir(upload_dir)
        
        folders = []
        files = []
        
        for item in items:
            item_path = os.path.join(upload_dir, item)
            if os.path.isdir(item_path):
                folders.append(item)
            else:
                files.append(item)
        
        return {
            "success": True,
            "folders": folders,
            "files": files
        }
    except Exception as e:
        logger.error(f"Error listing directory: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/knowledgebase/folder")
async def create_folder(
    current_user: Annotated[User, Depends(get_current_active_user)],
    name: str = Body(..., description="Folder name"),
    parentPath: str = Body("", description="Parent path"),
    knowledge_base: str = Body("default", description="Knowledge base name")
):
    """Create a new folder in knowledgebase"""
    try:
        from src.file_process.utils import get_upload_dir
        import os
        
        # Validate folder name
        if not name or name.strip() == "":
            raise HTTPException(status_code=400, detail="Folder name cannot be empty")
        
        # Get the parent directory path
        parent_dir = get_upload_dir(current_user.id, knowledge_base, parentPath)
        
        # Create the new folder path
        new_folder_path = os.path.join(parent_dir, name)
        
        # Create the folder if it doesn't exist
        if os.path.exists(new_folder_path):
            raise HTTPException(status_code=400, detail=f"Folder '{name}' already exists")
        
        os.makedirs(new_folder_path, exist_ok=True)
        
        return {
            "success": True,
            "message": f"Folder '{name}' created successfully",
            "path": f"{parentPath}/{name}"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error creating folder: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/knowledgebase/folder")
async def delete_folder(
    current_user: Annotated[User, Depends(get_current_active_user)],
    path: str = Body(..., description="Folder path"),
    knowledge_base: str = Body("default", description="Knowledge base name")
):
    """Delete a folder from knowledgebase"""
    try:        
        # Normalize path by removing leading slashes to handle root directory paths correctly
        normalized_path = path.lstrip('/')
        
        # Get the folder path
        folder_path = get_upload_dir(current_user.id, knowledge_base, normalized_path)
        
        # Check if folder exists
        if not os.path.exists(folder_path):
            raise HTTPException(status_code=404, detail=f"Folder '{path}' not found")
        
        # Delete the folder and its contents
        shutil.rmtree(folder_path)
        parsed_folder_path, folder_name = get_parsed_path(folder_path)
        parsed_folder_path = os.path.join(parsed_folder_path, folder_name)
        logger.info(f"Deleting parsed folder: {parsed_folder_path}")
        if os.path.exists(parsed_folder_path):
            shutil.rmtree(parsed_folder_path)
        
        # Delete all database records for files under this folder
        deleted_count = memory_manager.delete_files_by_path_prefix(folder_path)
        logger.info(f"Deleted {deleted_count} database records for files under folder: {folder_path}")
        
        return {
            "success": True,
            "message": f"Folder '{path}' deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting folder: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/knowledgebase/file")
async def delete_file(
    current_user: Annotated[User, Depends(get_current_active_user)],
    path: str = Body(..., description="File path"),
    knowledge_base: str = Body("default", description="Knowledge base name")
):
    """Delete a file from knowledgebase"""
    try:
        from src.file_process.utils import get_upload_dir
        import os
        
        # Normalize path by removing leading slashes
        normalized_path = path.lstrip('/')
        
        # Split the path into directory and filename
        directory = os.path.dirname(normalized_path)
        filename = os.path.basename(normalized_path)
        
        # Get the file path
        file_path = get_upload_dir(current_user.id, knowledge_base, directory)
        full_file_path = os.path.join(file_path, filename)
        
        # Check if file exists
        if not os.path.exists(full_file_path):
            raise HTTPException(status_code=404, detail=f"File '{path}' not found")
        
        # Delete the file from filesystem
        os.remove(full_file_path)
        parsed_file_path, filename = get_parsed_path(full_file_path)
        if parsed_file_path:
            for item in glob.glob(os.path.join(parsed_file_path, filename + "*")):
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
        
        memory_manager.delete_file_by_path(full_file_path)
        
        return {
            "success": True,
            "message": f"File '{path}' deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting file: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint to delete a knowledgebase
@app.delete("/api/knowledgebase/{kb_id}")
async def delete_knowledgebase(
    kb_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Delete a knowledgebase."""
    try:
        # Use the MemoryManager method to delete the knowledgebase
        success = memory_manager.delete_knowledgebase(current_user.id, kb_id)
        if success:
            return {
                "success": True,
                "message": "Knowledgebase deleted successfully"
            }
        return {
            "success": False,
            "message": "Failed to delete knowledgebase"
        }
    except Exception as e:
        logger.error(f"Error deleting knowledgebase: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint for file uploads
@app.post("/api/upload")
async def upload_files(
    current_user: Annotated[User, Depends(get_current_active_user)],
    knowledge_base: str = Form(...),
    directory: str = Form(""),
    files: List[UploadFile] = File(...)
):
    """Upload one or more files to a knowledge base."""
    try:
        # Call the upload handler
        pipeline = FileProcessingPipeline()
        result = await pipeline.process_files(current_user.id, knowledge_base, files, directory)
        return result
    except Exception as e:
        logger.error(f"Error processing upload: {e}")
        # Return an error response with status code 400
        raise HTTPException(status_code=400, detail=str(e))


class ChatRequest(BaseModel):
    message: str
    user_id: int
    thread_id: str

# Replace the chat_endpoint with this updated version
@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    """Chat endpoint that processes user messages and returns streaming responses."""
    message = request.message
    user_id = request.user_id
    thread_id = request.thread_id
    
    logger.debug(f"Received chat request from user {user_id}, thread {thread_id}: {message}")
    
    try:
        # Get RAG settings from environment variables
        try:
            rag_type_str = os.getenv("RAG_TYPE", "simple").lower()
            rag_type = RAGType(rag_type_str)
        except ValueError:
            rag_type = RAGType.SIMPLE
            
        rag_k = int(os.getenv("RAG_K", 10))
        
        # Create RAGAgent instance
        rag_agent = RAGAgent(rag_type, rag_k)
        
        # Process the message
        def generate_stream():
            try:
                for chunk in rag_agent.chat(message, knowledge_base_id=1):
                    for key, value in chunk.items():
                        if key == "stage":
                            # Send stage information
                            yield f"data: {json.dumps({key: value})}\n\n"
                        elif key == "response":
                            # Send response chunk
                            yield f"data: {json.dumps({key: value})}\n\n"
                
                # Send done signal
                yield f"data: {json.dumps({"done": True})}\n\n"
                
            except Exception as e:
                logger.error(f"Error processing chat message: {str(e)}")
                yield f"data: {json.dumps({"error": str(e)})}\n\n"
        
        return StreamingResponse(
            generate_stream(),
            media_type="text/event-stream"
        )
        
    except Exception as e:
        logger.error(f"Chat endpoint error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running."""
    return {"status": "ok", "message": "File Upload API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
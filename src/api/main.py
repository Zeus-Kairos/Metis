import os
import sys
import json
import glob
import shutil
from datetime import datetime, timedelta, timezone

from typing import Annotated, List, Optional, Dict, Any

from fastapi import FastAPI, File, UploadFile, Form, HTTPException, Body, Depends, status, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from contextlib import asynccontextmanager

from src.file_process.indexer import Indexer
from src.utils.paths import get_index_path, get_upload_dir, get_parsed_path
from src.file_process.pipeline import FileProcessingPipeline
from src.file_process.parallel_pipeline import ParallelFileProcessingPipeline
from src.memory.memory import MemoryManager
from src.utils.logging_config import get_logger
from src.api.thread import router as thread_router
from src.api.thread import rag_agents
from src.agent.api_llm import api_llm_runners

logger = get_logger(__name__)

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

# Pydantic model for user configuration update
class UserConfigUpdate(BaseModel):
    api_key: Optional[str] = None
    llm_model: Optional[str] = None
    embedding_model: Optional[str] = None
    model_provider: Optional[str] = None
    api_base_url: Optional[str] = None

app = FastAPI(title="Metis API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add security headers middleware
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    # Security headers to prevent various attacks and improve Chrome security
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval'; style-src 'self' 'unsafe-inline'"
    return response

# Middleware to refresh tokens on user activity
@app.middleware("http")
async def refresh_token_middleware(request, call_next):
    # Skip token refresh for login endpoints
    if request.url.path == "/api/token" or request.url.path == "/api/users":
        return await call_next(request)
    
    # Get token from cookie
    token = request.cookies.get("access_token")
    if token:
        # Decode and validate token
        payload = memory_manager.decode_token(token)
        if payload:
            username = payload.get("sub")
            user_id = payload.get("user_id")
            exp = payload.get("exp")
            
            if username and user_id and exp:
                # Check if token needs refresh
                current_time = datetime.now(timezone.utc)
                expiration_time = datetime.fromtimestamp(exp, timezone.utc)
                time_remaining = expiration_time - current_time
                
                # If token is expiring in less than 15 minutes, refresh it
                if time_remaining < timedelta(minutes=15):
                    # Generate new token
                    new_token = memory_manager.create_access_token(
                        data={"sub": username, "user_id": user_id}
                    )
                    
                    # Create a response early to set the new cookie
                    response = await call_next(request)
                    
                    # Update cookie with new token
                    response.set_cookie(
                        key="access_token",
                        value=new_token,
                        httponly=True,
                        secure=False,  # Set to True in production with HTTPS
                        samesite="strict",
                        max_age=3600,  # 1 hour
                        path="/"
                    )
                    return response
    
    # Proceed with normal request handling
    return await call_next(request)

# Include thread-related endpoints
app.include_router(thread_router)

# Initialize MemoryManager
memory_manager = MemoryManager()

indexers = {}

def get_indexer(user_id: int, knowledge_base: str) -> Indexer:
    """Get or create an Indexer for the given user and knowledge base."""
    indexer_key = f"{user_id}_{knowledge_base}"
    if indexer_key not in indexers:
        indexers[indexer_key] = Indexer(get_index_path(user_id, knowledge_base))
    return indexers[indexer_key]

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

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """Get the current user from the token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    payload = memory_manager.decode_token(token)
    if payload is None:
        raise credentials_exception
    
    username: str = payload.get("sub")
    if username is None:
        raise credentials_exception
    
    # Get user with password from memory manager
    user_dict = memory_manager.get_user_by_username_with_password(username)
    if user_dict:
        return UserInDB(
            id=user_dict["id"],
            username=user_dict["username"],
            email=user_dict["email"],
            hashed_password=user_dict["password"],
            disabled=False  # Default to enabled
        )
    return None

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    """Get the current active user."""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# Authentication endpoints
@app.post("/api/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], response: Response):
    """Login endpoint to get JWT access token."""
    # Authenticate user using memory manager
    user_dict = memory_manager.authenticate_user(form_data.username, form_data.password)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token using memory manager   
    access_token = memory_manager.create_access_token(
        data={"sub": user_dict["username"], "user_id": user_dict["id"]},     
    )
    
    # Return token in both JSON response and secure cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,  # Prevent JavaScript access
        secure=False,  # Set to True in production with HTTPS
        samesite="strict",  # Prevent CSRF attacks
        max_age=3600,  # 1 hour
        path="/"
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

# API endpoint for updating user configuration
@app.patch("/api/users/config")
async def update_user_configuration(
    config_data: UserConfigUpdate,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Update user configuration settings."""
    try:
        # Call the update_user_configuration method from memory_manager
        updated_config = memory_manager.update_user_configuration(
            user_id=current_user.id,
            api_key=config_data.api_key,
            llm_model=config_data.llm_model,
            embedding_model=config_data.embedding_model,
            model_provider=config_data.model_provider,
            api_base_url=config_data.api_base_url
        )       
        
        # If there's an existing RAGAgent instance for this user, remove it
        # so a new one will be created with updated configuration on next request
        if current_user.id in rag_agents:
            del rag_agents[current_user.id]
            logger.info(f"Removed existing RAGAgent for user {current_user.id} to apply updated configuration")
        
        # Remove the existing ApiLLMRunner instance for this user
        if current_user.id in api_llm_runners:
            del api_llm_runners[current_user.id]
            logger.info(f"Removed existing ApiLLMRunner for user {current_user.id} to apply updated configuration")
        
        return {
            "success": True,
            "message": "User configuration updated successfully",
            "config": updated_config
        }
    except Exception as e:
        logger.error(f"Error updating user configuration: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint for getting user configuration
@app.get("/api/users/config")
async def get_user_configuration(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Get user configuration settings."""
    try:
        # Call the get_user_configuration method from memory_manager
        config = memory_manager.get_user_configuration(user_id=current_user.id)
        if config:
            return {
                "success": True,
                "config": config
            }
        return {
            "success": True,
            "config": None,
            "message": "No configuration found for user"
        }
    except Exception as e:
        logger.error(f"Error getting user configuration: {e}")
        raise HTTPException(status_code=400, detail=str(e))

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
):
    """Create a new knowledge base for the user."""
    try:
        root_path = get_upload_dir(current_user.id, name, "")
        # Call the create_knowledgebase method
        knowledgebase_id = memory_manager.knowledgebase_manager.create_knowledgebase(current_user.id, name, root_path, description)
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
        knowledgebases = memory_manager.knowledgebase_manager.get_all_knowledgebases(current_user.id)
            
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
        
        # Use the KnowledgebaseManager method to rename the knowledgebase
        success = memory_manager.knowledgebase_manager.rename_knowledgebase(current_user.id, kb_id, new_name)
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

# API endpoint to update knowledgebase description
@app.put("/api/knowledgebase/{kb_id}/description")
async def update_knowledgebase_description(
    kb_id: int,
    description_data: dict,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Update knowledgebase description."""
    try:
        if "description" not in description_data:
            return {
                "success": False,
                "message": "Description field is required"
            }
        
        new_description = description_data["description"]
        
        # Use the KnowledgebaseManager method to update the knowledgebase description
        success = memory_manager.knowledgebase_manager.update_knowledgebase_description(current_user.id, kb_id, new_description)
        if success:
            return {
                "success": True,
                "message": "Knowledgebase description updated successfully"
            }
        return {
            "success": False,
            "message": "Failed to update knowledgebase description"
        }
    except Exception as e:
        logger.error(f"Error updating knowledgebase description: {e}")
        raise HTTPException(status_code=400, detail=str(e))

# API endpoint to set a knowledgebase as active
@app.patch("/api/knowledgebase/{kb_id}/active")
async def set_active_knowledgebase(
    kb_id: int,
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    """Set a knowledgebase as active, deactivating all other knowledgebases for the user."""
    try:
        # Use the KnowledgebaseManager method to set the knowledgebase as active
        success = memory_manager.knowledgebase_manager.set_active_knowledgebase(current_user.id, kb_id)
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
@app.get("/api/knowledgebase/{kb_id}/list")
async def list_directory(
    current_user: Annotated[User, Depends(get_current_active_user)],
    kb_id: int,
    path: str = "",
    knowledge_base: str = "default"
):
    """List directory contents for a knowledgebase"""
    try:                
        # Get the upload directory path using the knowledgebase name
        parent_folder = get_upload_dir(current_user.id, knowledge_base, path)
        
        # Use get_files_by_parent to get the items from database
        items = memory_manager.knowledgebase_manager.get_files_by_parent(kb_id, parent_folder)
        
        folders = []
        files = []
        
        # Process the files and folders
        for item in items:
            file_id = item[0]  # file_id is at index 0
            filename = item[1]  # filename is at index 1
            uploaded_time = item[2]  # uploaded_time is at index 2
            file_size = item[3]  # file_size is at index 3
            description = item[4]  # description is at index 4
            type = item[5]  # type is at index 5
            
            if type == 'folder':
                folders.append({
                    "id": file_id,
                    "name": filename,
                    "uploaded_time": uploaded_time.isoformat() if uploaded_time else None,
                    "description": description
                })
            else:
                files.append({
                    "id": file_id,
                    "name": filename,
                    "uploaded_time": uploaded_time.isoformat() if uploaded_time else None,
                    "file_size": file_size,
                    "description": description
                })
        
        return {
            "success": True,
            "folders": folders,
            "files": files
        }
    except Exception as e:
        logger.error(f"Error listing directory: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/knowledgebase/{kb_id}/folder")
async def create_folder(
    current_user: Annotated[User, Depends(get_current_active_user)],
    kb_id: int,
    name: str = Body(..., description="Folder name"),
    parentPath: str = Body("", description="Parent path"),
    knowledge_base: str = Body("default", description="Knowledge base name")
):
    """Create a new folder in knowledgebase"""
    try:       
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
        parsed_folder_path, folder_name = get_parsed_path(new_folder_path)
        parsed_folder_path = os.path.join(parsed_folder_path, folder_name)

        memory_manager.knowledgebase_manager.add_file_by_knowledgebase_name(
            name, new_folder_path, parsed_folder_path, current_user.id, knowledge_base, type="folder", parentFolder=parent_dir)
        
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

@app.delete("/api/knowledgebase/{kb_id}/folder")
async def delete_folder(
    current_user: Annotated[User, Depends(get_current_active_user)],
    kb_id: int,
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
        
        # Get all file IDs under this folder path before files are deleted from database
        file_ids = memory_manager.knowledgebase_manager.get_files_by_path_prefix(folder_path)
        indexer = get_indexer(current_user.id, knowledge_base)
        indexer.delete_file_chunks(file_ids, save=True)
        # Delete all database records for files under this folder
        memory_manager.knowledgebase_manager.delete_file_by_path(folder_path)
        
        return {
            "success": True,
            "message": f"Folder '{path}' deleted successfully"
        }
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error deleting folder: {e}")
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/api/knowledgebase/{kb_id}/file")
async def delete_file(
    current_user: Annotated[User, Depends(get_current_active_user)],
    kb_id: int,
    path: str = Body(..., description="File path"),
    knowledge_base: str = Body("default", description="Knowledge base name")
):
    """Delete a file from knowledgebase"""
    try:        
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
        
        file_id = memory_manager.knowledgebase_manager.delete_file_by_path(full_file_path)
        indexer = get_indexer(current_user.id, knowledge_base)
        indexer.delete_file_chunks([file_id], save=True)
        
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
        # Use the KnowledgebaseManager method to delete the knowledgebase
        success = memory_manager.knowledgebase_manager.delete_knowledgebase(current_user.id, kb_id)
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

# API endpoint to update multiple file/folder descriptions
@app.put("/api/knowledgebase/{kb_id}/descriptions")
async def update_multiple_descriptions(
    kb_id: int,  
    current_user: Annotated[User, Depends(get_current_active_user)],
    updates: List[Dict[str, Any]] = Body(...),
):
    """Update descriptions for multiple files and folders in a knowledgebase."""
    try:
        # Use the KnowledgebaseManager method to update multiple descriptions
        success = memory_manager.knowledgebase_manager.update_multiple_descriptions(kb_id, updates)
        if success:
            return {
                "success": True,
                "message": "Descriptions updated successfully"
            }
        return {
            "success": False,
            "message": "Failed to update descriptions"
        }
    except Exception as e:
        logger.error(f"Error updating multiple descriptions: {e}")
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
        indexer = get_indexer(current_user.id, knowledge_base)
        pipeline = FileProcessingPipeline(indexer, memory_manager)
        result = await pipeline.process_files(current_user.id, knowledge_base, files, directory)
        return result
    except Exception as e:
        logger.error(f"Error processing upload: {e}")
        # Return an error response with status code 400
        raise HTTPException(status_code=400, detail=str(e))


# API endpoint for streaming file uploads
@app.post("/api/stream-upload")
async def stream_upload_files(
    current_user: Annotated[User, Depends(get_current_active_user)],
    knowledge_base: str = Form(...),
    directory: str = Form(""),
    files: List[UploadFile] = File(...)
):
    """Upload one or more files to a knowledge base and stream results as they complete."""
    try:
        from fastapi.responses import StreamingResponse
        import json
        
        # Call the parallel processing pipeline
        indexer = get_indexer(current_user.id, knowledge_base)
        pipeline = ParallelFileProcessingPipeline(indexer, memory_manager)
        
        # Helper function to generate JSON lines
        async def generate():
            async for result in pipeline.process_files(current_user.id, knowledge_base, files, directory):
                yield json.dumps(result) + "\n"
        
        return StreamingResponse(generate(), media_type="application/x-ndjson")
    except Exception as e:
        logger.error(f"Error in stream upload: {e}")
        # Return an error response with status code 400
        raise HTTPException(status_code=400, detail=str(e))

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint to verify API is running."""
    return {"status": "ok", "message": "File Upload API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
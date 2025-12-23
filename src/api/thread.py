from typing import Optional
from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from src.memory.thread import ThreadManager
from src.utils.logging_config import get_logger

logger = get_logger(__name__)

# Create a thread manager instance
thread_manager = ThreadManager()

# Create a router for thread-related endpoints
router = APIRouter(prefix="/api", tags=["threads"])

# Pydantic models for thread operations
class ThreadTitleUpdate(BaseModel):
    user_id: int
    thread_id: str
    title: str

# Thread-related endpoints
@router.delete("/thread/{user_id}/{thread_id}")
def delete_thread(user_id: int, thread_id: str):
    """Delete a specific thread for a user"""
    logger.debug(f"Deleting thread {thread_id} for user {user_id}")
    thread_manager.remove_thread(user_id, thread_id)
    logger.debug(f"Thread {thread_id} deleted successfully for user {user_id}")
    return {"status": "success", "message": f"Thread {thread_id} deleted successfully"}

@router.delete("/threads/{user_id}")
def delete_all_threads(user_id: int):
    """Delete all threads for a user"""
    logger.debug(f"Deleting all threads for user {user_id}")
    thread_manager.remove_thread(user_id, None)
    logger.debug(f"All threads deleted successfully for user {user_id}")
    return {"status": "success", "message": f"All threads of user {user_id} deleted successfully"}

@router.post("/thread/create")
def create_thread(user_id: int, title: Optional[str] = None):
    """Create a new conversation thread for a user"""
    logger.debug(f"Creating new thread for user {user_id} with title {title}")
    thread_id = thread_manager.create_thread(user_id, title)
    logger.debug(f"Created thread {thread_id} for user {user_id}")
    return {"status": "success", "thread_id": thread_id, "title": title or f"Thread {thread_id[:8]}"}

@router.get("/threads/{user_id}")
def get_user_threads(user_id: int):
    """Get all conversation threads for a user"""
    logger.debug(f"Fetching threads for user {user_id}")
    threads = thread_manager.get_threads_for_user(user_id)
    logger.debug(f"Found {len(threads)} threads for user {user_id}")
    return {"status": "success", "threads": threads}

@router.post("/thread/set-active")
def set_active_thread(user_id: int, thread_id: str):
    """Set the active thread for a user"""
    logger.debug(f"Setting active thread {thread_id} for user {user_id}")
    success = thread_manager.set_active_thread(user_id, thread_id)
    if success:
        logger.debug(f"Thread {thread_id} set as active for user {user_id}")
        return {"status": "success", "message": "Thread set as active successfully"}
    else:
        logger.error(f"Failed to set active thread {thread_id} for user {user_id}")
        raise HTTPException(status_code=404, detail=f"Thread {thread_id} not found or does not belong to user {user_id}")

@router.post("/thread/title")
def update_thread_title_endpoint(update_data: ThreadTitleUpdate):
    """Update the title of a specific thread"""
    user_id = update_data.user_id
    thread_id = update_data.thread_id
    title = update_data.title
    
    try:
        logger.debug(f"Updating title for thread {thread_id} of user {user_id} to: {title}")
        success = thread_manager.update_thread_title(user_id, thread_id, title)
        if success:
            logger.debug(f"Successfully updated title for thread {thread_id} of user {user_id}")
            return {"status": "success", "message": "Thread title updated successfully"}
        else:
            logger.error(f"Failed to update title for thread {thread_id} of user {user_id}")
            raise HTTPException(status_code=404, detail=f"Thread {thread_id} not found or does not belong to user {user_id}")
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error updating thread title: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/thread/history")
def get_thread_history(user_id: int, thread_id: str): 
    """Get a specific thread by ID"""
    logger.debug(f"Fetching thread history for thread {thread_id} of user {user_id}")
    history = thread_manager.get_conversation_history(user_id, thread_id)
    if history:
        logger.debug(f"Found {len(history)} messages in thread {thread_id} for user {user_id}")
        return {"status": "success", "history": history}
    else:
        logger.error(f"Message history not found for thread {thread_id} of user {user_id}")
        raise HTTPException(status_code=404, detail=f"Message history not found for thread {thread_id} of user {user_id}") 

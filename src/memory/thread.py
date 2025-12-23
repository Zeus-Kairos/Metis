from datetime import datetime
import os
from typing import List, Dict, Any, Optional, Tuple, Union
from psycopg_pool import ConnectionPool
import logging

from src.memory.memory import MemoryManager

logger = logging.getLogger(__name__)

DEFAULT_THREAD_TITLE = "New Chat"

class ThreadManager:
    """Manages user threads and conversation history"""

    def __init__(self):
        """
        Initialize the thread manager.
        
        Args:
            memory_manager: MemoryManager instance
        """
        self.conn_str = os.getenv("DB_URI")

        if not self.conn_str:
            logger.error("No DB_URI found in environment. Fallback to in-memory storage.")
            # self.checkpointer = PostgresSaver(self.connection_pool)
            # try:
            #     self.checkpointer.setup()
            # except Exception as e:
            #     logger.error(f"Error setting up checkpointer: {e}")
            #     # If setup fails, we might already have the tables
        
            # In-memory fallback stores for when DB is not available
            self.user_thread_map = {}
            self.user_threads = {}
            self.thread_metadata = {}
        else:
            self.connection_pool = ConnectionPool(self.conn_str)
            

    # Helper method to get the active thread_id for a user or create a new thread_id for a new user
    def _get_thread_id_for_user(self, user_id: int) -> str:
        """
        Get the active thread ID for a user. If no thread exists, create one.
        
        Args:
            user_id: User identifier
            
        Returns:
            Thread ID string
        """
        if self.connection_pool:
            # Use database
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # raise an error if the user doesn't exist
                    cur.execute(
                        "SELECT id FROM users WHERE id = %s",
                        (user_id,)
                    )
                    if not cur.fetchone():
                        raise ValueError(f"User ID {user_id} does not exist")
                        
                    # Check if user has an active thread
                    cur.execute(
                        "SELECT thread_id FROM threads WHERE user_id = %s AND is_active = true",
                        (user_id,)
                    )
                    result = cur.fetchone()
                    
                    if result:
                        return result[0]
                    
                    # If no active thread, get the most recent one
                    cur.execute(
                        "SELECT thread_id FROM threads WHERE user_id = %s ORDER BY created_at DESC LIMIT 1",
                        (user_id,)
                    )
                    result = cur.fetchone()
                    
                    if result:
                        thread_id = result[0]
                        # Set this thread as active
                        cur.execute(
                            "UPDATE threads SET is_active = true, updated_at = CURRENT_TIMESTAMP WHERE thread_id = %s",
                            (thread_id,)
                        )
                        conn.commit()
                        return thread_id
                    
                    # If no threads exist, create one
                    thread_id = f"thread_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
                    cur.execute(
                        "INSERT INTO threads (thread_id, user_id, title, is_active) VALUES (%s, %s, %s, %s)",
                        (thread_id, user_id, DEFAULT_THREAD_TITLE, True)
                    )
                    conn.commit()
                    return thread_id
        else:
            # Fallback to in-memory storage
            if user_id in self.user_thread_map:
                return self.user_thread_map[user_id]
            
            # Create a new thread for the user if none exists
            thread_id = f"thread_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
            self._init_thread(user_id, DEFAULT_THREAD_TITLE)
            return thread_id
        
    def _init_thread(self, user_id: int, title: str = DEFAULT_THREAD_TITLE):
        """
        Initialize a new thread for a user.
        
        Args:
            user_id: User identifier
            title: Thread title
        """
        
        # Fallback for in-memory mode
        thread_id = f"thread_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
        if user_id not in self.user_threads:
            self.user_threads[user_id] = []
        self.user_threads[user_id].append(thread_id)
        self.user_thread_map[user_id] = thread_id
        self.thread_metadata[thread_id] = {
            "title": title,
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat()
        }

    def create_thread(self, user_id: int, thread_title: Optional[str] = None) -> str:
        """
        Create a new thread for the user.
        
        Args:
            user_id: User identifier
            thread_title: Optional thread title
            
        Returns:
            Newly created thread_id
        """
        if self.connection_pool:
            # Use database to create new thread
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Generate thread_id
                    thread_id = f"thread_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"

                    # raise an error if the user doesn't exist
                    cur.execute(
                        "SELECT id FROM users WHERE id = %s",
                        (user_id,)
                    )
                    if not cur.fetchone():
                        raise ValueError(f"User ID {user_id} does not exist")
                    
                    # Set the old active thread as inactive
                    cur.execute(
                        "UPDATE threads SET is_active = false, updated_at = CURRENT_TIMESTAMP WHERE user_id = %s AND is_active = true",
                        (user_id,)
                    )
                    
                    # Insert new thread
                    cur.execute(
                        "INSERT INTO threads (thread_id, user_id, title, is_active) VALUES (%s, %s, %s, %s)",
                        (thread_id, user_id, thread_title or DEFAULT_THREAD_TITLE, True)
                    )
                    conn.commit()
                    return thread_id
        else:
            # Fallback for in-memory mode
            thread_id = f"thread_{user_id}_{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}"
            
            # Initialize user threads if needed
            if user_id not in self.user_threads:
                self.user_threads[user_id] = []
            
            # Add the new thread to user threads
            self.user_threads[user_id].append(thread_id)
            
            # Set this thread as active
            self.user_thread_map[user_id] = thread_id
            
            # Create thread metadata
            self.thread_metadata[thread_id] = {
                "title": thread_title or "New Chat",
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }
            
            return thread_id

    def get_threads_for_user(self, user_id: int) -> List[Dict[str, Any]]:
        """
        Get all threads for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            List of threads with metadata
        """
        if self.connection_pool:
            # Use database to get threads
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT thread_id, title, is_active, created_at, updated_at FROM threads WHERE user_id = %s ORDER BY created_at DESC",
                        (user_id,)
                    )
                    threads = []
                    for row in cur.fetchall():
                        threads.append({
                            "thread_id": row[0],
                            "title": row[1],
                            "is_active": row[2],
                            "created_at": row[3].isoformat(),
                            "updated_at": row[4].isoformat()
                        })
                    return threads
        else:
            # Fallback for in-memory mode
            # Return empty list if user has no threads
            if user_id not in self.user_threads:
                return []
            
            # Get all threads for the user
            threads = []
            for thread_id in self.user_threads[user_id]:
                if thread_id in self.thread_metadata:
                    thread_info = self.thread_metadata[thread_id].copy()
                    thread_info["thread_id"] = thread_id
                    thread_info["is_active"] = self.user_thread_map.get(user_id) == thread_id
                    threads.append(thread_info)
            
            return threads

    def set_active_thread(self, user_id: int, thread_id: str) -> bool:
        """
        Set the active thread for a user.
        
        Args:
            user_id: User identifier
            thread_id: Thread identifier
            
        Returns:
            True if thread was set as active, False otherwise
        """
        if self.connection_pool:
            # Use database to set active thread
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Check if thread belongs to user
                    cur.execute(
                        "SELECT thread_id FROM threads WHERE thread_id = %s AND user_id = %s",
                        (thread_id, user_id)
                    )
                    if not cur.fetchone():
                        return False
                    
                    # Set the old active thread as inactive
                    cur.execute(
                        "UPDATE threads SET is_active = false, updated_at = CURRENT_TIMESTAMP WHERE user_id = %s AND is_active = true", 
                        (user_id,)
                    )
                    
                    # Set the specified thread to active
                    cur.execute(
                        "UPDATE threads SET is_active = true, updated_at = CURRENT_TIMESTAMP WHERE thread_id = %s",
                        (thread_id,)
                    )
                    conn.commit()
                    return True
        else:
            # Fallback for in-memory mode
            # Check if the thread belongs to the user
            if (user_id in self.user_threads and
                thread_id in self.user_threads[user_id] and
                thread_id in self.thread_metadata):
                self.user_thread_map[user_id] = thread_id
                return True
            return False

    def update_thread_title(self, user_id: int, thread_id: str, title: str) -> bool:
        """
        Update the title of a thread.
        
        Args:
            user_id: User identifier
            thread_id: Thread identifier
            title: New thread title
            
        Returns:
            True if thread title was updated, False otherwise
        """
        if self.connection_pool:
            # Use database to update thread title
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Check if thread belongs to user
                    cur.execute(
                        "SELECT thread_id FROM threads WHERE thread_id = %s AND user_id = %s",
                        (thread_id, user_id)
                    )
                    if not cur.fetchone():
                        return False
                    
                    # Update thread title
                    cur.execute(
                        "UPDATE threads SET title = %s, updated_at = CURRENT_TIMESTAMP WHERE thread_id = %s",
                        (title, thread_id)
                    )
                    conn.commit()
                    return True
        else:
            # Fallback for in-memory mode
            # Check if the thread belongs to the user
            if (user_id in self.user_threads and
                thread_id in self.user_threads[user_id] and
                thread_id in self.thread_metadata):
                self.thread_metadata[thread_id]["title"] = title
                self.thread_metadata[thread_id]["updated_at"] = datetime.now().isoformat()
                return True
            return False

    def remove_thread(self, user_id: int, thread_id: Optional[str] = None):
        """
        Remove a thread for a user. If no thread_id is provided, remove all threads.
        
        Args:
            user_id: ID of the user
            thread_id: ID of the thread to remove (optional)
        """
        if self.connection_pool:
            # Use database to remove thread
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    if thread_id:
                        # Check if thread belongs to user
                        cur.execute(
                            "SELECT is_active FROM threads WHERE thread_id = %s AND user_id = %s",
                            (thread_id, user_id)
                        )
                        thread_info = cur.fetchone()
                        if not thread_info:
                            return
                        
                        is_active = thread_info[0]
                        
                        # Delete the thread
                        cur.execute(
                            "DELETE FROM threads WHERE thread_id = %s",
                            (thread_id,)
                        )
                        
                        # If the deleted thread was active, set another thread as active
                        if is_active:
                            cur.execute(
                                "SELECT thread_id FROM threads WHERE user_id = %s ORDER BY created_at DESC LIMIT 1",
                                (user_id,)
                            )
                            new_active_thread = cur.fetchone()
                            if new_active_thread:
                                cur.execute(
                                    "UPDATE threads SET is_active = true, updated_at = CURRENT_TIMESTAMP WHERE thread_id = %s",
                                    (new_active_thread[0],)
                                )
                    else:
                        # Remove all threads for the user
                        cur.execute(
                            "DELETE FROM threads WHERE user_id = %s",
                            (user_id,)
                        )
                    
                    conn.commit()
        else:
            # Fallback for in-memory mode
            if user_id in self.user_threads:
                if thread_id:
                    if thread_id in self.user_threads[user_id]:
                        self.user_threads[user_id].remove(thread_id)
                        
                    # Remove thread from metadata
                    if thread_id in self.thread_metadata:
                        del self.thread_metadata[thread_id]
                    
                    # Update active thread if needed
                    if self.user_thread_map.get(user_id) == thread_id:
                        del self.user_thread_map[user_id]
                else:
                    # Remove all threads for the user
                    for tid in self.user_threads[user_id]:
                        if tid in self.thread_metadata:
                            del self.thread_metadata[tid]
                            
                    # Remove user from all maps
                    del self.user_threads[user_id]
                    if user_id in self.user_thread_map:
                        del self.user_thread_map[user_id]

    def get_config_for_user(self, user_id: int, thread_id: str = None) -> Dict[str, Any]:
        """
        Get the configuration with thread_id for a specific user.
        
        Args:
            user_id: User identifier
            thread_id: Optional thread identifier, defaults to active thread
            
        Returns:
            Configuration dictionary with thread_id
        """
        # Use provided thread_id or get active thread
        if thread_id:
            # Verify thread belongs to user
            if (user_id in self.user_threads and 
                thread_id in self.user_threads[user_id]):
                return {"configurable": {"thread_id": thread_id}}
        
        # Get or create active thread
        thread_id = self._get_thread_id_for_user(user_id)
        return {"configurable": {"thread_id": thread_id}}

    def get_conversation_history(self, user_id: int, thread_id: str = None, graph=None) -> List[Dict[str, str]]:
        """
        Get conversation history for a specific user and thread.
        
        Args:
            user_id: User identifier
            thread_id: Optional thread identifier, defaults to active thread
            graph: Optional LangGraph instance
            
        Returns:
            List of conversation messages
        """
        if not thread_id:
            thread_id = self._get_thread_id_for_user(user_id)
        
        # Get state history
        state_history = self.get_state_history_for_user(user_id, thread_id, graph)
        
        # Extract conversation messages
        conversation = []
        for state in state_history:
            if hasattr(state, 'messages'):
                for msg in state.messages:
                    conversation.append({
                        "role": msg.role,
                        "content": msg.content
                    })
        
        return conversation

    def get_state_history_for_user(self, user_id: int, thread_id: str = None, graph=None) -> List[Any]:
        """
        Get state history for a specific user and thread.
        
        Args:
            user_id: User identifier
            thread_id: Optional thread identifier, defaults to active thread
            graph: Optional LangGraph instance
            
        Returns:
            List of LangGraph states
        """
        if not thread_id:
            thread_id = self._get_thread_id_for_user(user_id)
        
        try:
            config = self.get_config_for_user(user_id, thread_id)
            if graph and config:
                # Get state history from graph
                return list(graph.get_state_history(config))
        except Exception as e:
            logger.error(f"Error fetching state history for user {user_id}, thread {thread_id}: {e}")
        return []

    def get_user_namespace(self, user_id: int) -> Tuple[str, str]:
        """
        Get the namespace tuple for a user.
        
        Args:
            user_id: User identifier
            
        Returns:
            Namespace Tuple (user_id, thread_id)
        """
        thread_id = self._get_thread_id_for_user(user_id)
        return (user_id, thread_id)

    def update_conversation(self, user_id: int, thread_id: str = None):
        """
        Update thread updated_at timestamp.
        
        Args:
            user_id: User identifier
            thread_id: Optional thread identifier, defaults to active thread
        """
        if not thread_id:
            thread_id = self._get_thread_id_for_user(user_id)

        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Update thread updated_at timestamp
                    cur.execute(
                        "UPDATE threads SET updated_at = CURRENT_TIMESTAMP WHERE thread_id = %s AND user_id = %s",
                        (thread_id, user_id)
                    )
                    conn.commit()
        except Exception as e:
            logger.error(f"Error updating conversation for user {user_id}, thread {thread_id}: {e}")
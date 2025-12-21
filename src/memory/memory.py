import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple, Union
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore
from psycopg_pool import ConnectionPool
from passlib.context import CryptContext      

import logging
logger = logging.getLogger(__name__)

class MemoryManager:
    """Manages user memory and conversation history using LangGraph MemorySaver and MemoryStore"""

    def __init__(self):
        """
        Initialize the memory manager with LangGraph persistence components.
        """
        # Get connection string from environment
        self.conn_str = os.getenv("DB_URI")

        if not self.conn_str:
            logger.error("No DB_URI found in environment. Cannot initialize database.")
            raise ValueError("DB_URI environment variable is required")

        # Password hashing
        self.pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
        
        # Create connection pool with autocommit=True to handle CREATE INDEX CONCURRENTLY
        self.connection_pool = ConnectionPool(self.conn_str, kwargs={"autocommit": True})
        
        # Initialize database tables
        self._init_db_tables()

    # Method to return a ConnectionPool lifespan context manager
    def get_connection_pool(self) -> Optional[ConnectionPool]:
        """Return the connection pool for database operations."""
        return getattr(self, 'connection_pool', None)
        # return ConnectionPool(self.conn_str)    

    def __del__(self):
        """
        Clean up resources when the MemoryManager instance is destroyed.
        """
        if hasattr(self, 'connection_pool'):
            try:
                self.connection_pool.close()
            except Exception as e:
                logger.error(f"Error closing connection pool: {e}")

    def _init_db_tables(self):
        """
        Initialize database tables if they don't exist.
        """
        if not self.conn_str:
            return
            
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Create users table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS users (
                            id SERIAL PRIMARY KEY,
                            username VARCHAR(255) NOT NULL,
                            email VARCHAR(255) NOT NULL,
                            password VARCHAR(255) NOT NULL,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    
                    # Add unique constraints to username and email columns if they don't exist
                    cur.execute("""
                        ALTER TABLE users 
                        ADD CONSTRAINT users_username_key UNIQUE (username),
                        ADD CONSTRAINT users_email_key UNIQUE (email);
                    """)
                                        
                    # Create threads table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS threads (
                            thread_id VARCHAR(255) PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            title VARCHAR(255) NOT NULL DEFAULT 'New Chat',
                            is_active BOOLEAN NOT NULL DEFAULT true,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                        )
                    """)
                    
                    # Create index on threads.user_id
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_threads_user_id ON threads(user_id)
                    """)
                    
                    # Create knowledgebase table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS knowledgebase (
                            id SERIAL PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            name VARCHAR(255) NOT NULL,
                            description TEXT,
                            navigation JSONB,
                            is_active BOOLEAN NOT NULL DEFAULT true,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                        )
                    """)
                    
                    # Add unique constraint to knowledgebase (user_id, name) if it doesn't exist
                    cur.execute("""
                        ALTER TABLE knowledgebase 
                        ADD CONSTRAINT knowledgebase_user_id_name_key UNIQUE (user_id, name);
                    """)
                    
                    # Create kb_thread table for knowledgebase-thread mapping (one-to-many)
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS kb_thread (
                            knowledgebase_id INTEGER NOT NULL,
                            thread_id VARCHAR(255) NOT NULL,
                            PRIMARY KEY (knowledgebase_id, thread_id),
                            FOREIGN KEY (knowledgebase_id) REFERENCES knowledgebase(id) ON DELETE CASCADE,
                            FOREIGN KEY (thread_id) REFERENCES threads(thread_id) ON DELETE CASCADE,
                            UNIQUE (thread_id)  -- Ensure each thread maps to at most one knowledgebase
                        )
                    """)
                    
                    # Create index on kb_thread.knowledgebase_id for efficient queries
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_kb_thread_knowledgebase_id ON kb_thread(knowledgebase_id)
                    """)
                    
                    # Create index on kb_thread.thread_id for efficient queries
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_kb_thread_thread_id ON kb_thread(thread_id)
                    """)
                    
                    # Create files table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS files (
                            file_id SERIAL PRIMARY KEY,
                            filename VARCHAR(255) NOT NULL,
                            filepath VARCHAR(1024) NOT NULL UNIQUE,
                            parsed_path VARCHAR(1024) NOT NULL,
                            uploaded_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            file_size INTEGER,
                            knowledgebase_id INTEGER NOT NULL,
                            FOREIGN KEY (knowledgebase_id) REFERENCES knowledgebase(id) ON DELETE CASCADE
                        )
                    """)
                    
                    # Create indexes on files table for efficient queries                     
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_files_knowledgebase_id ON files(knowledgebase_id)
                    """)
                    
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_files_filename ON files(filename)
                    """)
                    
                    conn.commit()
        except Exception as e:
            logger.error(f"Error initializing database tables: {e}")
            return

    def create_knowledgebase(self, user_id: int, name: str, description: str = None, navigation: dict = None) -> int:
        """
        Create a new knowledge base for the user.
        
        Args:
            user_id: User identifier
            name: Knowledge base name
            description: Optional knowledge base description
            navigation: Optional knowledge base navigation structure
            
        Returns:
            The created knowledge base ID
        """
            
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Check if user exists
                    cur.execute(
                        "SELECT id FROM users WHERE id = %s",
                        (user_id,)
                    )
                    if not cur.fetchone():
                        raise ValueError(f"User ID {user_id} does not exist")
                    
                    # Serialize navigation to JSON string if provided
                    navigation_json = json.dumps(navigation) if navigation else None
                    
                    # Insert the new knowledgebase as active
                    cur.execute(
                        "INSERT INTO knowledgebase (user_id, name, description, navigation, is_active) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                        (user_id, name, description, navigation_json, True)
                    )
                    knowledgebase_id = cur.fetchone()[0]
                    
                    # Set all other knowledgebases for this user to inactive
                    cur.execute(
                        "UPDATE knowledgebase SET is_active = false WHERE user_id = %s AND is_active = true AND id != %s",
                        (user_id, knowledgebase_id)
                    )
                    
                    conn.commit()
                    return knowledgebase_id
        except Exception as e:
            # Check if this is a unique constraint violation
            error_message = str(e)
            if 'duplicate key value' in error_message:
                raise ValueError("Knowledgebase with this name already exists")
            # If it's not a unique constraint violation, re-raise the original exception
            raise

    def create_user(self, username: str, email: str, password: str) -> int:
        """
        Create a new user in the database.
        
        Args:
            username: User's username
            email: User's email
            password: User's password
            
        Returns:
            The created user's ID
        """              
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Hash password using argon2
                    hashed_password = self.pwd_context.hash(password)
                    
                    # Insert the user
                    cur.execute(
                        "INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id",
                        (username, email, hashed_password)
                    )
                    user_id = cur.fetchone()[0]
                    conn.commit()
                    return user_id
        except Exception as e:
            # Check if this is a unique constraint violation
            error_message = str(e)
            if 'unique_username' in error_message:
                raise ValueError("Username already exists")
            elif 'unique_email' in error_message:
                raise ValueError("Email already exists")
            elif 'duplicate key value' in error_message:
                raise ValueError("Username or email already exists")
            # If it's not a unique constraint violation, re-raise the original exception
            raise
    
    def delete_user(self, user_id: int) -> bool:
        """
        Delete a user from the database.
        
        Args:
            user_id: The ID of the user to delete
            
        Returns:
            True if the user was deleted successfully, False otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Delete the user - related records (threads, knowledgebase) will be deleted due to ON DELETE CASCADE
                    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting user {user_id}: {e}")
            raise

    def add_file_by_knowledgebase_name(self, filename: str, filepath: str, parsed_path: str, user_id: int, knowledgebase_name: str, file_size: int = None) -> int:
        """
        Add a new file record to the database using knowledgebase name and user ID.
        
        Args:
            filename: Name of the file
            filepath: Path to the uploaded file
            parsed_path: Path to the parsed file
            user_id: ID of the user who owns the knowledgebase
            knowledgebase_name: Name of the knowledgebase associated with the file
            file_size: Size of the file in bytes (optional)
            
        Returns:
            The created file ID
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Check if knowledgebase exists
                    cur.execute(
                        "SELECT id FROM knowledgebase WHERE user_id = %s AND name = %s",
                        (user_id, knowledgebase_name)
                    )
                    knowledgebase = cur.fetchone()
                    if not knowledgebase:
                        raise ValueError(f"Knowledgebase {knowledgebase_name} does not exist for user {user_id}")
                    knowledgebase_id = knowledgebase[0]
                    
                    # Call the main add_file method with knowledgebase_id
                    return self.add_file(filename, filepath, parsed_path, knowledgebase_id, file_size)

        except Exception as e:
            logger.error(f"Error adding file: {e}")
            raise

    def add_file(self, filename: str, filepath: str, parsed_path: str, knowledgebase_id: int, file_size: int = None) -> int:
        """
        Add a new file record to the database.
        
        Args:
            filename: Name of the file
            filepath: Path to the uploaded file
            parsed_path: Path to the parsed file
            knowledgebase_id: ID of the knowledgebase associated with the file
            file_size: Size of the file in bytes (optional)
            
        Returns:
            The created file ID
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    
                    # Check if knowledgebase exists
                    cur.execute(
                        "SELECT id FROM knowledgebase WHERE id = %s",
                        (knowledgebase_id,)
                    )
                    if not cur.fetchone():
                        raise ValueError(f"Knowledgebase ID {knowledgebase_id} does not exist")
                    
                    # Insert the file record with UPSERT (update if filepath exists)
                    cur.execute(
                        """
                        INSERT INTO files (filename, filepath, parsed_path, knowledgebase_id, file_size)
                        VALUES (%s, %s, %s, %s, %s)
                        ON CONFLICT (filepath) DO UPDATE
                        SET filename = EXCLUDED.filename,
                            parsed_path = EXCLUDED.parsed_path,
                            file_size = EXCLUDED.file_size,
                            uploaded_time = CURRENT_TIMESTAMP
                        RETURNING file_id
                        """,
                        (filename, filepath, parsed_path, knowledgebase_id, file_size)
                    )
                    file_id = cur.fetchone()[0]
                    conn.commit()
                    return file_id
        except Exception as e:
            logger.error(f"Error adding file: {e}")
            raise
    
    def get_files_by_knowledgebase_id(self, knowledgebase_id: int) -> list:
        """
        Get all files for a specific knowledgebase.
        
        Args:
            knowledgebase_id: ID of the knowledgebase
            
        Returns:
            List of file records
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT file_id, filename, filepath, parsed_path, uploaded_time, knowledgebase_id, file_size
                        FROM files
                        WHERE knowledgebase_id = %s
                        ORDER BY uploaded_time DESC
                        """,
                        (knowledgebase_id,)
                    )
                    files = cur.fetchall()
                    return files
        except Exception as e:
            logger.error(f"Error getting files by knowledgebase ID: {e}")
            raise
    
    def get_file_by_id(self, file_id: int) -> tuple:
        """
        Get a specific file by ID.
        
        Args:
            file_id: ID of the file
            
        Returns:
            File record if found, None otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT file_id, filename, filepath, parsed_path, uploaded_time, knowledgebase_id, file_size
                        FROM files
                        WHERE file_id = %s
                        """,
                        (file_id,)
                    )
                    file = cur.fetchone()
                    return file
        except Exception as e:
            logger.error(f"Error getting file by ID: {e}")
            raise
    
    def delete_file(self, file_id: int) -> bool:
        """
        Delete a file by ID.
        
        Args:
            file_id: ID of the file
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "DELETE FROM files WHERE file_id = %s",
                        (file_id,)
                    )
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting file: {e}")
            raise
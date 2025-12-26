import os
import json
from datetime import datetime, timezone, timedelta
from typing import List, Dict, Any, Optional, Tuple, Union
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore
from psycopg_pool import ConnectionPool
from passlib.context import CryptContext
from jose import JWTError, jwt      

from .knowledgebase import KnowledgebaseManager

import logging
logger = logging.getLogger(__name__)

# Authentication settings
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = os.getenv("SECRET_KEY")

def _get_secret_key() -> str:
    """Get and validate the secret key, raising an error if not set."""
    key = os.getenv("SECRET_KEY")
    if not key:
        raise RuntimeError("SECRET_KEY environment variable must be set")
    return key

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
        
        # Create connection pool
        self.connection_pool = ConnectionPool(self.conn_str)
        
        # Initialize database tables
        self._init_db_tables()
        
        # Initialize knowledgebase manager
        self.knowledgebase_manager = KnowledgebaseManager(self.connection_pool)

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
                    # Check if username constraint exists first
                    cur.execute("""
                        SELECT constraint_name 
                        FROM information_schema.table_constraints 
                        WHERE table_name = 'users' 
                        AND constraint_name = 'users_username_key';
                    """)
                    if not cur.fetchone():
                        cur.execute("""
                            ALTER TABLE users ADD CONSTRAINT users_username_key UNIQUE (username);
                        """)
                    
                    # Check if email constraint exists first
                    cur.execute("""
                        SELECT constraint_name 
                        FROM information_schema.table_constraints 
                        WHERE table_name = 'users' 
                        AND constraint_name = 'users_email_key';
                    """)
                    if not cur.fetchone():
                        cur.execute("""
                            ALTER TABLE users ADD CONSTRAINT users_email_key UNIQUE (email);
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
                    
                    # Create user_configure table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS user_configure (
                            user_id INTEGER PRIMARY KEY,
                            api_key VARCHAR(255),
                            llm_model VARCHAR(255),
                            embedding_model VARCHAR(255),
                            model_provider VARCHAR(255),
                            api_base_url VARCHAR(255),
                            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
                        )
                    """)
                    
                    conn.commit()
        except Exception as e:
            logger.error(f"Error initializing database tables: {e}")
            return

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

    def get_user_by_username(self, username: str) -> Optional[dict]:
        """
        Get a user by their username.
        
        Args:
            username: User's username
            
        Returns:
            User dictionary if found, None otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT id, username, email FROM users WHERE username = %s",
                        (username,)
                    )
                    user = cur.fetchone()
                    if user:
                        return {
                            "id": user[0],
                            "username": user[1],
                            "email": user[2]
                        }
                    return None
        except Exception as e:
            raise
            
    def update_user_configuration(self, user_id: int, api_key: Optional[str] = None, 
                                llm_model: Optional[str] = None, embedding_model: Optional[str] = None, 
                                model_provider: Optional[str] = None, api_base_url: Optional[str] = None) -> dict:
        """
        Update or insert user configuration.
        
        Args:
            user_id: User's ID
            api_key: API key
            llm_model: LLM model name
            embedding_model: Embedding model name
            model_provider: Model provider
            api_base_url: API base URL
            
        Returns:
            The updated user configuration
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Use UPSERT to handle both insert and update cases
                    cur.execute("""
                        INSERT INTO user_configure (
                            user_id, api_key, llm_model, embedding_model, model_provider, api_base_url
                        ) VALUES (%s, %s, %s, %s, %s, %s)
                        ON CONFLICT (user_id) DO UPDATE SET
                            api_key = EXCLUDED.api_key,
                            llm_model = EXCLUDED.llm_model,
                            embedding_model = EXCLUDED.embedding_model,
                            model_provider = EXCLUDED.model_provider,
                            api_base_url = EXCLUDED.api_base_url
                        RETURNING *
                    """, (user_id, api_key, llm_model, embedding_model, model_provider, api_base_url))
                    
                    updated_config = cur.fetchone()
                    conn.commit()
                    
                    return {
                        "user_id": updated_config[0],
                        "api_key": updated_config[1],
                        "llm_model": updated_config[2],
                        "embedding_model": updated_config[3],
                        "model_provider": updated_config[4],
                        "api_base_url": updated_config[5]
                    }
        except Exception as e:
            logger.error(f"Error updating user configuration: {e}")
            raise
            
    def get_user_configuration(self, user_id: int) -> Optional[dict]:
        """
        Get user configuration by user ID.
        
        Args:
            user_id: User's ID
            
        Returns:
            User configuration dictionary if found, None otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT * FROM user_configure WHERE user_id = %s",
                        (user_id,)
                    )
                    config = cur.fetchone()
                    if config:
                        return {
                            "user_id": config[0],
                            "api_key": config[1],
                            "llm_model": config[2],
                            "embedding_model": config[3],
                            "model_provider": config[4],
                            "api_base_url": config[5]
                        }
                    return None
        except Exception as e:
            logger.error(f"Error getting user configuration: {e}")
            raise
            
    def get_user_by_username_with_password(self, username: str) -> Optional[dict]:
        """
        Get a user by their username including password for authentication.
        
        Args:
            username: User's username
            
        Returns:
            User dictionary with password if found, None otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "SELECT id, username, email, password FROM users WHERE username = %s",
                        (username,)
                    )
                    user = cur.fetchone()
                    if user:
                        return {
                            "id": user[0],
                            "username": user[1],
                            "email": user[2],
                            "password": user[3]
                        }
                    return None
        except Exception as e:
            raise
            
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """
        Verify a password against a hashed password.
        
        Args:
            plain_password: Plain text password
            hashed_password: Hashed password
            
        Returns:
            True if password matches, False otherwise
        """
        return self.pwd_context.verify(plain_password, hashed_password)
        
    def authenticate_user(self, username: str, password: str) -> Optional[dict]:
        """
        Authenticate a user with username and password.
        
        Args:
            username: User's username
            password: User's password
            
        Returns:
            User dictionary if authenticated, None otherwise
        """
        user = self.get_user_by_username_with_password(username)
        if not user or not self.verify_password(password, user["password"]):
            return None
        # Remove password from the returned user data
        user.pop("password")
        return user
        
    def create_access_token(self, data: dict) -> str:
        """
        Create a JWT access token.
        
        Args:
            data: Data to encode in the token
            
        Returns:
            Encoded JWT token
        """
        to_encode = data.copy()
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.now(timezone.utc) + (access_token_expires or timedelta(minutes=15))
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, _get_secret_key(), algorithm=ALGORITHM)
    
    def decode_token(self, token: str) -> Optional[dict]:
        """
        Decode and validate a JWT token.
        
        Args:
            token: JWT token to decode
            
        Returns:
            Decoded token payload if valid, None otherwise
        """
        try:
            payload = jwt.decode(token, _get_secret_key(), algorithms=[ALGORITHM])
            return payload
        except JWTError:
            return None

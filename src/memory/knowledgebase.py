import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple, Union
from psycopg_pool import ConnectionPool

import logging
logger = logging.getLogger(__name__)

class KnowledgebaseManager:
    """
    Manages knowledgebase creation, updates, and file operations.
    """
    
    def __init__(self, connection_pool: ConnectionPool):
        """
        Initialize the KnowledgebaseManager with a database connection pool.
        
        Args:
            connection_pool: Database connection pool for database operations
        """
        self.connection_pool = connection_pool
        
    def _init_knowledgebase_tables(self):
        """
        Initialize knowledgebase-related database tables if they don't exist.
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Create knowledgebase table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS knowledgebase (
                            id SERIAL PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            name VARCHAR(255) NOT NULL,
                            description TEXT,
                            navigation JSON,
                            is_active BOOLEAN DEFAULT FALSE,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        )
                    """)
                    
                    # Add unique constraint to knowledgebase (user_id, name) if it doesn't exist
                    cur.execute("""
                        SELECT constraint_name 
                        FROM information_schema.table_constraints 
                        WHERE table_name = 'knowledgebase' 
                        AND constraint_name = 'knowledgebase_user_id_name_key';
                    """)
                    if not cur.fetchone():
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
                            FOREIGN KEY (thread_id) REFERENCES threads(id) ON DELETE CASCADE,
                            UNIQUE (thread_id)  -- Ensure each thread maps to at most one knowledgebase
                        )
                    """)
                    
                    # Create index on kb_thread.knowledgebase_id for efficient queries
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_kb_thread_knowledgebase_id ON kb_thread(knowledgebase_id)
                    """)
                    
                    # Create files table for storing document files
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS files (
                            file_id SERIAL PRIMARY KEY,
                            filename VARCHAR(255) NOT NULL,
                            filepath TEXT NOT NULL,
                            parsed_path TEXT NOT NULL,
                            uploaded_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            knowledgebase_id INTEGER NOT NULL,
                            file_size INTEGER,
                            FOREIGN KEY (knowledgebase_id) REFERENCES knowledgebase(id) ON DELETE CASCADE
                        )
                    """)
                    
                    # Create index on files.knowledgebase_id for efficient queries
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_files_knowledgebase_id ON files(knowledgebase_id)
                    """)
        except Exception as e:
            logger.error(f"Error initializing knowledgebase tables: {e}")
            raise
    
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
    
    def get_all_knowledgebases(self, user_id: int) -> list:
        """
        Get all knowledgebases for a specific user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            List of knowledgebase records
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, name, description, navigation, is_active, created_at, updated_at
                        FROM knowledgebase
                        WHERE user_id = %s
                        ORDER BY is_active DESC, updated_at DESC
                        """,
                        (user_id,)
                    )
                    # Get column names
                    columns = [desc[0] for desc in cur.description]
                    # Convert results to dictionaries
                    results = []
                    for row in cur.fetchall():
                        results.append(dict(zip(columns, row)))
                    return results
        except Exception as e:
            logger.error(f"Error getting knowledgebases for user {user_id}: {e}")
            raise
    
    def set_active_knowledgebase(self, user_id: int, knowledgebase_id: int) -> bool:
        """
        Set a specific knowledgebase as active for a user, deactivating all other knowledgebases.
        
        Args:
            user_id: ID of the user
            knowledgebase_id: ID of the knowledgebase to set as active
            
        Returns:
            True if the update was successful
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Update all knowledgebases for this user - set the specified one to active, others to inactive
                    cur.execute(
                        """
                        UPDATE knowledgebase
                        SET is_active = CASE 
                            WHEN id = %s THEN true 
                            ELSE false 
                        END
                        WHERE user_id = %s
                        """,
                        (knowledgebase_id, user_id)
                    )
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error setting active knowledgebase for user {user_id}: {e}")
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
                    
                    # Update the knowledgebase's updated_at timestamp
                    cur.execute(
                        "UPDATE knowledgebase SET updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                        (knowledgebase_id,)
                    )
                    
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
                    # Get the knowledgebase_id for the file before deleting it
                    cur.execute(
                        "SELECT knowledgebase_id FROM files WHERE file_id = %s",
                        (file_id,)
                    )
                    file = cur.fetchone()
                    if not file:
                        return False
                    
                    knowledgebase_id = file[0]
                    
                    # Delete the file
                    cur.execute(
                        "DELETE FROM files WHERE file_id = %s",
                        (file_id,)
                    )
                    
                    if cur.rowcount > 0:
                        # Update the knowledgebase's updated_at timestamp
                        cur.execute(
                            "UPDATE knowledgebase SET updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                            (knowledgebase_id,)
                        )
                    
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting file: {e}")
            raise
    
    def delete_files_by_path_prefix(self, path_prefix: str) -> int:
        """
        Delete all files with filepath starting with the given prefix.
        
        Args:
            path_prefix: The path prefix to match
            
        Returns:
            The number of files deleted
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    logger.debug(f"Path prefix: {path_prefix}")
                    
                    # Properly escape backslashes for SQL LIKE pattern
                    # Also handle both Windows and Unix path formats
                    path_prefix_windows = path_prefix.replace('\\', '\\\\')
                    path_prefix_unix = path_prefix.replace('\\', '/')
                    
                    # Get unique knowledgebase_ids for the files that will be deleted
                    cur.execute(
                        "SELECT DISTINCT knowledgebase_id FROM files WHERE filepath ILIKE %s OR filepath ILIKE %s",
                        (f"{path_prefix_windows}%", f"{path_prefix_unix}%")
                    )
                    knowledgebase_ids = [row[0] for row in cur.fetchall()]
                    
                    # Delete the files
                    cur.execute(
                        "DELETE FROM files WHERE filepath ILIKE %s OR filepath ILIKE %s",
                        (f"{path_prefix_windows}%", f"{path_prefix_unix}%")
                    )
                    deleted_count = cur.rowcount
                    
                    # Update the updated_at timestamp for all affected knowledgebases
                    if deleted_count > 0 and knowledgebase_ids:
                        for kb_id in knowledgebase_ids:
                            cur.execute(
                                "UPDATE knowledgebase SET updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                                (kb_id,)
                            )
                    
                    conn.commit()
                    return deleted_count
        except Exception as e:
            logger.error(f"Error deleting files by path prefix: {e}")
            raise
    
    def delete_file_by_path(self, filepath: str) -> bool:
        """
        Delete a file by filepath.
        
        Args:
            filepath: Path of the file
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Get the knowledgebase_id for the file before deleting it
                    cur.execute(
                        "SELECT knowledgebase_id FROM files WHERE filepath = %s",
                        (filepath,)
                    )
                    file = cur.fetchone()
                    if not file:
                        return False
                    
                    knowledgebase_id = file[0]
                    
                    # Delete the file
                    cur.execute(
                        "DELETE FROM files WHERE filepath = %s",
                        (filepath,)
                    )
                    
                    if cur.rowcount > 0:
                        # Update the knowledgebase's updated_at timestamp
                        cur.execute(
                            "UPDATE knowledgebase SET updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                            (knowledgebase_id,)
                        )
                    
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting file by path: {e}")
            raise
    
    def rename_knowledgebase(self, user_id: int, knowledgebase_id: int, new_name: str) -> bool:
        """
        Rename a knowledgebase for a user.
        
        Args:
            user_id: ID of the user
            knowledgebase_id: ID of the knowledgebase to rename
            new_name: New name for the knowledgebase
            
        Returns:
            True if renaming was successful, False otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Update the knowledgebase name
                    cur.execute(
                        "UPDATE knowledgebase SET name = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s AND user_id = %s",
                        (new_name, knowledgebase_id, user_id)
                    )
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            # Check if this is a unique constraint violation
            error_message = str(e)
            if 'duplicate key value' in error_message:
                raise ValueError("Knowledgebase with this name already exists")
            logger.error(f"Error renaming knowledgebase: {e}")
            raise
    
    def delete_knowledgebase(self, user_id: int, knowledgebase_id: int) -> bool:
        """
        Delete a knowledgebase for a user.
        
        Args:
            user_id: ID of the user
            knowledgebase_id: ID of the knowledgebase to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            logger.info(f"Attempting to delete knowledgebase: user_id={user_id}, knowledgebase_id={knowledgebase_id}")
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # First check if the knowledgebase exists and belongs to the user
                    cur.execute(
                        "SELECT id, name, is_active FROM knowledgebase WHERE id = %s AND user_id = %s",
                        (knowledgebase_id, user_id)
                    )
                    kb = cur.fetchone()
                    if not kb:
                        logger.warning(f"Knowledgebase not found or not owned by user: user_id={user_id}, knowledgebase_id={knowledgebase_id}")
                        return False
                    
                    # Check if this is the only knowledgebase for the user
                    cur.execute(
                        "SELECT COUNT(*) FROM knowledgebase WHERE user_id = %s",
                        (user_id,)
                    )
                    kb_count = cur.fetchone()[0]
                    if kb_count <= 1:
                        logger.warning(f"Cannot delete the only knowledgebase for user: user_id={user_id}, knowledgebase_id={knowledgebase_id}")
                        raise ValueError("Cannot delete the only knowledgebase.")
                    
                    logger.info(f"Found knowledgebase to delete: id={kb[0]}, name={kb[1]}, is_active={kb[2]}")
                    is_deleted_kb_active = kb[2]
                    
                    # Delete the knowledgebase - files will be deleted automatically due to ON DELETE CASCADE
                    cur.execute(
                        "DELETE FROM knowledgebase WHERE id = %s AND user_id = %s",
                        (knowledgebase_id, user_id)
                    )
                    conn.commit()
                    logger.info(f"Successfully deleted knowledgebase: affected rows={cur.rowcount}")
                    
                    # If the deleted knowledgebase was active, set the most recently updated one as active
                    if is_deleted_kb_active:
                        # Find the most recently updated knowledgebase for this user (excluding the deleted one)
                        cur.execute(
                            """
                            SELECT id FROM knowledgebase 
                            WHERE user_id = %s 
                            AND id != %s
                            ORDER BY updated_at DESC 
                            LIMIT 1
                            """,
                            (user_id, knowledgebase_id)
                        )
                        remaining_kb = cur.fetchone()
                        
                        if remaining_kb:
                            # Set the most recently updated knowledgebase as active
                            cur.execute(
                                """
                                UPDATE knowledgebase 
                                SET is_active = true 
                                WHERE id = %s AND user_id = %s
                                """,
                                (remaining_kb[0], user_id)
                            )
                            conn.commit()
                            logger.info(f"Set knowledgebase {remaining_kb[0]} as active after deleting active knowledgebase {knowledgebase_id}")
                        else:
                            logger.info(f"No remaining knowledgebases after deleting active knowledgebase {knowledgebase_id}")
                    
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error deleting knowledgebase: {e}", exc_info=True)
            raise

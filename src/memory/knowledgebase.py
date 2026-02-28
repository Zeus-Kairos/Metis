import os
import json
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple, Union
from psycopg_pool import ConnectionPool

from src.utils.logging_config import get_logger

logger = get_logger(__name__)

class KnowledgebaseManager:
    """
    Manages knowledgebase creation, updates, and file operations.
    """
    
    def __init__(self, connection_pool: ConnectionPool = None):
        """
        Initialize the KnowledgebaseManager with a database connection pool.
        
        Args:
            connection_pool: Database connection pool for database operations.
        """
        self.connection_pool = connection_pool if connection_pool else ConnectionPool(os.getenv("DB_URI"))
        self._init_knowledgebase_tables()
        
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
                            root_path VARCHAR(255) NOT NULL,
                            is_active BOOLEAN DEFAULT FALSE,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            CONSTRAINT knowledgebase_user_id_name_key UNIQUE (user_id, name)
                        )
                    """)

                    # Create threads table
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS threads (
                            thread_id VARCHAR(255) PRIMARY KEY,
                            user_id INTEGER NOT NULL,
                            knowledgebase_id INTEGER NOT NULL,
                            title VARCHAR(255) NOT NULL DEFAULT 'New Chat',
                            is_active BOOLEAN NOT NULL DEFAULT true,
                            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
                            FOREIGN KEY (knowledgebase_id) REFERENCES knowledgebase(id) ON DELETE CASCADE
                        )
                    """)
                    
                    # Create files table for storing document files
                    cur.execute("""
                        CREATE TABLE IF NOT EXISTS files (
                            file_id SERIAL PRIMARY KEY,
                            filename VARCHAR(255) NOT NULL,
                            filepath TEXT NOT NULL UNIQUE,
                            parsed_content TEXT NOT NULL,
                            uploaded_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                            knowledgebase_id INTEGER NOT NULL,
                            file_size INTEGER,
                            description TEXT,
                            type VARCHAR(10) NOT NULL CHECK (type IN ('file', 'folder')),
                            parent INTEGER,
                            FOREIGN KEY (knowledgebase_id) REFERENCES knowledgebase(id) ON DELETE CASCADE,
                            FOREIGN KEY (parent) REFERENCES files(file_id) ON DELETE CASCADE,
                            CHECK (type != 'file' OR file_size IS NOT NULL)
                        )
                    """)
                    
                    # Create index on files.knowledgebase_id for efficient queries
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_files_knowledgebase_id ON files(knowledgebase_id)
                    """)
                    
                    # Create index on files.filepath for efficient queries
                    cur.execute("""
                        CREATE INDEX IF NOT EXISTS idx_files_filepath ON files(filepath)
                    """)

                    conn.commit()
        except Exception as e:
            logger.error(f"Error initializing knowledgebase tables: {e}")
            raise
    
    def create_knowledgebase(self, user_id: int, name: str, root_path:str, description: str = None) -> int:
        """
        Create a new knowledge base for the user.
        
        Args:
            user_id: User identifier
            name: Knowledge base name
            root_path: Root folder path for the knowledge base
            description: Optional knowledge base description
            
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
                    
                    # Insert the new knowledgebase as active
                    cur.execute(
                        "INSERT INTO knowledgebase (user_id, name, description, root_path, is_active) VALUES (%s, %s, %s, %s, %s) RETURNING id",
                        (user_id, name, description, root_path, True)
                    )
                    knowledgebase_id = cur.fetchone()[0]

                    # Create root folder                    
                    cur.execute(
                        """
                        INSERT INTO files (filename, filepath, parsed_content, knowledgebase_id, file_size, description, type, parent)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING file_id
                        """,
                        ('root', root_path, '', knowledgebase_id, None, 'root folder for the knowledgebase', 'folder', None)
                    )
                    
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
                        SELECT id, name, description, root_path, is_active, created_at, updated_at
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
    
    def get_knowledgebase(self, knowledgebase_id: int) -> dict:
        """
        Get a specific knowledgebase by ID.
        
        Args:
            knowledgebase_id: ID of the knowledgebase
            
        Returns:
            Knowledgebase record if found, None otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id, name, description
                        FROM knowledgebase
                        WHERE id = %s
                        """,
                        (knowledgebase_id,)
                    )
                    # Get column names
                    columns = [desc[0] for desc in cur.description]
                    # Convert results to dictionaries
                    results = []
                    for row in cur.fetchall():
                        results.append(dict(zip(columns, row)))
                    return results[0] if results else None
        except Exception as e:
            logger.error(f"Error getting knowledgebase {knowledgebase_id}: {e}")
            raise


    def add_file_by_knowledgebase_name(self, filename: str, filepath: str, parsed_content: str, user_id: int, knowledgebase_name: str, file_size: int = None, description: str = None, type: str = 'file', parentFolder: str = "") -> int:
        """
        Add a new file record to the database using knowledgebase name and user ID.
        
        Args:
            filename: Name of the file
            filepath: Path to the uploaded file
            parsed_content: Content of the parsed file
            user_id: ID of the user who owns the knowledgebase
            knowledgebase_name: Name of the knowledgebase associated with the file
            file_size: Size of the file in bytes (required for file type)
            description: Description of the file or folder
            type: Type of the item (file or folder)
            parentFolder: Path to the parent folder
            
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
                    return self.add_file(filename, filepath, parsed_content, knowledgebase_id, file_size, description, type, parentFolder)

        except Exception as e:
            logger.error(f"Error adding file: {e}")
            raise
    
    def add_file(self, filename: str, filepath: str, parsed_content: str, knowledgebase_id: int, file_size: int = None, description: str = None, type: str = 'file', parentFolder: str = "") -> int:
        """
        Add a new file record to the database.
        
        Args:
            filename: Name of the file
            filepath: Path to the uploaded file
            parsed_content: Content of the parsed file
            knowledgebase_id: ID of the knowledgebase associated with the file
            file_size: Size of the file in bytes (required for file type)
            description: Description of the file or folder
            type: Type of the item (file or folder)
            parentFolder: Path to the parent folder
            
        Returns:
            The created file ID
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:                    
                    # Insert the file record with UPSERT (update if filepath exists), using subquery to get parent ID
                    cur.execute(
                        """
                        INSERT INTO files (filename, filepath, parsed_content, knowledgebase_id, file_size, description, type, parent)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, 
                            (SELECT file_id FROM files WHERE filepath = %s AND knowledgebase_id = %s AND type = 'folder')
                        )
                        ON CONFLICT (filepath) DO UPDATE
                        SET filename = EXCLUDED.filename,
                            parsed_content = EXCLUDED.parsed_content,
                            file_size = EXCLUDED.file_size,
                            description = EXCLUDED.description,     
                            type = EXCLUDED.type,
                            parent = EXCLUDED.parent,
                            uploaded_time = CURRENT_TIMESTAMP
                        RETURNING file_id
                        """,
                        (filename, filepath, parsed_content, knowledgebase_id, file_size, description, type, parentFolder, knowledgebase_id)
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
                        SELECT file_id, filename, filepath, parsed_content, uploaded_time, knowledgebase_id, file_size, description, type, parent
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

    def get_files_by_parent(self, knowledgebase_id: int, parentFolder: str):
        """
        Get all files for a specific parent folder.
        
        Args:
            knowledgebase_id: ID of the knowledgebase
            parentFolder: Path to the parent folder
            
        Returns:
            List of file records with file_id, filename, uploaded_time, file_size, description, and type
        """
        # Normalize path separators to match the database storage format
        normalized_path = parentFolder.replace('/', os.sep)
        
        with self.connection_pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT f.file_id, f.filename, f.uploaded_time, f.file_size, f.description, f.type
                    FROM files f
                    JOIN files parent_f ON parent_f.file_id = f.parent
                    WHERE f.knowledgebase_id = %s 
                    AND parent_f.knowledgebase_id = %s 
                    AND parent_f.filepath = %s
                    AND parent_f.type = 'folder'
                    ORDER BY f.uploaded_time DESC
                    """,
                    (knowledgebase_id, knowledgebase_id, normalized_path)
                )
                files = cur.fetchall()
                return files
    
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
                        SELECT file_id, filename, filepath, parsed_content, uploaded_time, knowledgebase_id, file_size, description, type, parent
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

    def get_files_by_path_prefix(self, path_prefix: str) -> List[int]:
        """
        Get all file IDs with filepath starting with the given prefix.
        
        Args:
            path_prefix: The path prefix to match
            
        Returns:
            List of file IDs that match the path prefix
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    logger.debug(f"Path prefix: {path_prefix}")
                    
                    # Properly escape backslashes for SQL LIKE pattern
                    # Also handle both Windows and Unix path formats
                    normalized_path_prefix = path_prefix.replace('/', os.sep)
                    path_prefix_windows = normalized_path_prefix.replace('\\', '\\\\')
                    path_prefix_unix = normalized_path_prefix.replace('\\', '/')
                    
                    # Get file IDs for both Windows and Unix path formats
                    cur.execute(
                        "SELECT file_id FROM files WHERE type = 'file' AND (filepath ILIKE %s OR filepath ILIKE %s)",
                        (f"{path_prefix_windows}%", f"{path_prefix_unix}%")
                    )
                    file_ids = [row[0] for row in cur.fetchall()]
                    logger.debug(f"File IDs: {file_ids}")
                    return file_ids
        except Exception as e:
            logger.error(f"Error getting files by path prefix: {e}")
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
    
    def delete_file_by_path(self, filepath: str) -> int:
        """
        Delete a file by filepath.
        
        Args:
            filepath: Path of the file
            
        Returns:
            file_id if deletion was successful, None otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Delete the file and return file_id and knowledgebase_id
                    cur.execute(
                        "DELETE FROM files WHERE filepath = %s RETURNING file_id, knowledgebase_id",
                        (filepath,)
                    )
                    deleted_file = cur.fetchone()
                    
                    if deleted_file:
                        file_id, knowledgebase_id = deleted_file
                        # Update the knowledgebase's updated_at timestamp
                        cur.execute(
                            "UPDATE knowledgebase SET updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                            (knowledgebase_id,)
                        )
                    
                    conn.commit()
                    return file_id
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
    
    def update_knowledgebase_description(self, user_id: int, knowledgebase_id: int, description: str) -> bool:
        """
        Update a knowledgebase description for a user.
        
        Args:
            user_id: ID of the user
            knowledgebase_id: ID of the knowledgebase to update
            description: New description for the knowledgebase
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            with self.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    # Update the knowledgebase description
                    cur.execute(
                        "UPDATE knowledgebase SET description = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s AND user_id = %s",
                        (description, knowledgebase_id, user_id)
                    )
                    conn.commit()
                    return cur.rowcount > 0
        except Exception as e:
            logger.error(f"Error updating knowledgebase description: {e}")
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
    
    def update_multiple_descriptions(self, knowledgebase_id: int, updates: List[Dict[str, Any]]) -> bool:
        """
        Update descriptions for multiple files and folders in a knowledgebase.
        
        Args:
            knowledgebase_id: ID of the knowledgebase
            updates: List of dictionaries containing file_id and description
                     Example: [{"file_id": 1, "description": "Updated description"}, ...]
            
        Returns:
            True if updates were successful
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
                    
                    # Prepare the SQL statement for batch update
                    update_sql = """
                        UPDATE files
                        SET description = %s
                        WHERE file_id = %s AND knowledgebase_id = %s
                    """
                    
                    # Prepare the data for batch execution
                    update_data = []
                    for update in updates:
                        file_id = update.get("file_id")
                        description = update.get("description")
                        if file_id is not None:
                            update_data.append((description, file_id, knowledgebase_id))
                    
                    # Execute the batch update
                    cur.executemany(update_sql, update_data)
                    
                    # Update the knowledgebase's updated_at timestamp
                    cur.execute(
                        "UPDATE knowledgebase SET updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                        (knowledgebase_id,)
                    )
                    
                    conn.commit()
                    logger.info(f"Successfully updated {cur.rowcount} descriptions")
                    return True
        except Exception as e:
            logger.error(f"Error updating multiple descriptions: {e}")
            raise

import os
import sys
import time
import pytest
import tempfile
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the project root to the path
sys.path.insert(0, r'c:\Apps\Metis')

from src.memory.memory import MemoryManager

def generate_random_string(length=10):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def test_files_table_operations():
    """
    Test that the files table and its operations work correctly.
    """
    # Initialize MemoryManager
    memory_manager = MemoryManager()
    
    # Create a test user
    username = f"test_user_{generate_random_string()}"
    email = f"{generate_random_string()}@example.com"
    password = "test_password"
    
    try:
        # Create user
        user_id = memory_manager.create_user(username, email, password)
        assert user_id is not None
        
        # Create a knowledgebase
        kb_name = f"Test KB {generate_random_string()}"
        kb_id = memory_manager.create_knowledgebase(user_id, kb_name, "Test knowledgebase")
        assert kb_id is not None
        
        # Create a test file
        test_filename = "test_document.txt"
        test_filepath = "uploads/test_document.txt"
        test_parsed_path = "parsed/test_document.json"
        
        # Test adding a file - use the correct method signature
        file_id = memory_manager.add_file(
            filename=test_filename,
            filepath=test_filepath,
            parsed_path=test_parsed_path,
            knowledgebase_id=kb_id,
            file_size=1024
        )
        assert file_id is not None
        assert isinstance(file_id, int)
        
        # Test getting file by ID
        file = memory_manager.get_file_by_id(file_id)
        assert file is not None
        assert file[0] == file_id  # file_id
        assert file[1] == test_filename  # filename
        assert file[2] == test_filepath  # filepath
        assert file[3] == test_parsed_path  # parsed_path
        assert file[5] == kb_id  # knowledgebase_id - index 5 now since user_id is removed
        assert isinstance(file[4], datetime)  # uploaded_time
        
        # Test getting files by knowledgebase ID (replace user_id with knowledgebase_id)
        kb_files = memory_manager.get_files_by_knowledgebase_id(kb_id)
        assert len(kb_files) > 0
        assert any(f[0] == file_id for f in kb_files)
        
        # Test deleting a file
        delete_result = memory_manager.delete_file(file_id)
        assert delete_result is True
        
        # Verify file was deleted
        deleted_file = memory_manager.get_file_by_id(file_id)
        assert deleted_file is None
        
        # Verify file count decreased
        updated_kb_files = memory_manager.get_files_by_knowledgebase_id(kb_id)
        assert len(updated_kb_files) == len(kb_files) - 1
        
        print("All file table operations tests passed!")
        
    finally:
        # Clean up
        try:
            memory_manager.delete_user(user_id)
        except:
            pass

if __name__ == "__main__":
    test_files_table_operations()
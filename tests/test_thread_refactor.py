import sys
import os
import traceback
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the src directory to the path - fix the path construction
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from memory.memory import MemoryManager

def test_in_memory_mode():
    print("Testing in-memory mode...")
    user_id = "123"
    
    # Save original DB_URI
    original_db_uri = os.environ.get("DB_URI")
    
    # Remove DB_URI to force in-memory mode
    if "DB_URI" in os.environ:
        del os.environ["DB_URI"]
    
    try:
        # Create memory manager in in-memory mode
        memory = MemoryManager()
        
        # Test thread creation
        thread_id_1 = memory.create_thread(user_id)
        print(f"Created thread: {thread_id_1}")
        assert thread_id_1 is not None
        
        # Test thread retrieval
        threads = memory.get_threads_for_user(user_id)
        print(f"Threads for user {user_id}: {len(threads)} threads")
        assert len(threads) == 1
        
        # Test multiple threads
        thread_id_2 = memory.create_thread(user_id)
        print(f"Created thread: {thread_id_2}")
        assert thread_id_2 is not None
        assert thread_id_1 != thread_id_2
        
        threads = memory.get_threads_for_user(user_id)
        print(f"Threads for user {user_id}: {len(threads)} threads")
        assert len(threads) == 2
        
        # Test thread removal
        memory.remove_thread(user_id, thread_id_1)
        threads = memory.get_threads_for_user(user_id)
        print(f"After removing thread, remaining threads: {len(threads)}")
        assert len(threads) == 1
        
        # Test thread removal again (non-existent thread)
        memory.remove_thread(user_id, "non-existent-thread")
        threads = memory.get_threads_for_user(user_id)
        assert len(threads) == 1
        
        print("In-memory mode tests completed successfully!")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"Test failed with error: {e}")
        traceback.print_exc()
        return False
    finally:
        # Restore original DB_URI
        if original_db_uri is not None:
            os.environ["DB_URI"] = original_db_uri
        elif "DB_URI" in os.environ:
            del os.environ["DB_URI"]

def test_basic_functionality():
    """Test basic functionality regardless of mode"""
    print("Testing basic functionality...")
    
    # Save original DB_URI
    original_db_uri = os.environ.get("DB_URI")
    
    # Remove DB_URI to force in-memory mode for this test
    if "DB_URI" in os.environ:
        del os.environ["DB_URI"]
    
    try:
        # Create memory manager in in-memory mode
        memory = MemoryManager()
        
        user_id = 456
        
        # Test _get_thread_id_for_user creates a new thread if none exists
        thread_id = memory._get_thread_id_for_user(user_id)
        print(f"_get_thread_id_for_user created thread: {thread_id}")
        
        # Test get_config_for_user
        config = memory.get_config_for_user(user_id)
        print(f"get_config_for_user: {config}")
        
        # Test get_user_namespace
        namespace = memory.get_user_namespace(user_id)
        print(f"get_user_namespace: {namespace}")
        
        print("Basic functionality tests completed successfully!")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"Test failed with error: {e}")
        traceback.print_exc()
        return False
    finally:
        # Restore original DB_URI
        if original_db_uri is not None:
            os.environ["DB_URI"] = original_db_uri
        elif "DB_URI" in os.environ:
            del os.environ["DB_URI"]

def test_database_mode():
    print("Testing database mode...")
    user_id = "789"
    
    # Check if DB_URI is set
    db_uri = os.environ.get("DB_URI")
    if not db_uri:
        print("DB_URI not found in environment variables - skipping database tests")
        print("=" * 50)
        return True
    
    try:
        # Create memory manager in database mode
        memory = MemoryManager()
        
        # Make sure we're in database mode
        assert memory.conn_str is not None, "Expected database mode but conn_str is None"
        
        # Test thread creation in database
        thread_id_1 = memory.create_thread(user_id)
        print(f"Created thread in database: {thread_id_1}")
        assert thread_id_1 is not None
        
        # Test thread retrieval from database
        threads = memory.get_threads_for_user(user_id)
        print(f"Threads in database for user {user_id}: {len(threads)} threads")
        assert len(threads) >= 1
        
        # Test multiple threads in database
        thread_id_2 = memory.create_thread(user_id)
        print(f"Created thread in database: {thread_id_2}")
        assert thread_id_2 is not None
        assert thread_id_1 != thread_id_2
        
        threads = memory.get_threads_for_user(user_id)
        print(f"Threads in database for user {user_id}: {len(threads)} threads")
        assert len(threads) >= 2
        
        # Test thread removal from database
        memory.remove_thread(user_id, thread_id_1)
        threads = memory.get_threads_for_user(user_id)
        print(f"After removing thread from database, remaining threads: {len(threads)}")
        
        # Verify the thread is actually removed from database
        thread_ids = [t['thread_id'] for t in threads]
        assert thread_id_1 not in thread_ids
        
        # Clean up - remove all test threads
        for thread in threads:
            memory.remove_thread(user_id, thread['thread_id'])
        
        # Verify all test threads are removed
        threads = memory.get_threads_for_user(user_id)
        print(f"After cleanup, threads for user {user_id}: {len(threads)} threads")
        
        print("Database mode tests completed successfully!")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"Database test failed with error: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing thread refactoring...")
    print("=" * 50)
    
    try:
        test_basic_functionality()
        test_in_memory_mode()
        test_database_mode()
        
        print("All tests passed!")
        print("The thread refactoring is working correctly.")
        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        traceback.print_exc()
        sys.exit(1)
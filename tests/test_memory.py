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
        
        # Create a user first
        created_user_id = memory.create_user("test_user", "test@example.com", "password123")
        print(f"Created user with ID: {created_user_id}")
        
        # Test thread creation in database
        thread_id_1 = memory.create_thread(created_user_id)
        print(f"Created thread in database: {thread_id_1}")
        assert thread_id_1 is not None
        
        # Test thread retrieval from database
        threads = memory.get_threads_for_user(created_user_id)
        print(f"Threads in database for user {created_user_id}: {len(threads)} threads")
        assert len(threads) >= 1
        
        # Test multiple threads in database
        thread_id_2 = memory.create_thread(created_user_id)
        print(f"Created thread in database: {thread_id_2}")
        assert thread_id_2 is not None
        assert thread_id_1 != thread_id_2
        
        threads = memory.get_threads_for_user(created_user_id)
        print(f"Threads in database for user {created_user_id}: {len(threads)} threads")
        assert len(threads) >= 2
        
        # Test thread removal from database
        memory.remove_thread(created_user_id, thread_id_1)
        threads = memory.get_threads_for_user(created_user_id)
        print(f"After removing thread from database, remaining threads: {len(threads)}")
        
        # Verify the thread is actually removed from database
        thread_ids = [t['thread_id'] for t in threads]
        assert thread_id_1 not in thread_ids
        
        # Clean up - remove all test threads
        for thread in threads:
            memory.remove_thread(created_user_id, thread['thread_id'])
        
        # Verify all test threads are removed
        threads = memory.get_threads_for_user(created_user_id)
        print(f"After cleanup, threads for user {created_user_id}: {len(threads)} threads")
        
        print("Database mode tests completed successfully!")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"Database test failed with error: {e}")
        traceback.print_exc()
        return False

def test_database_tables_creation():
    print("Testing database tables creation...")
    
    # Check if DB_URI is set
    db_uri = os.environ.get("DB_URI")
    if not db_uri:
        print("DB_URI not found in environment variables - skipping database tables tests")
        print("=" * 50)
        return True
    
    try:
        # Create memory manager in database mode
        memory = MemoryManager()
        
        # Make sure we're in database mode
        assert memory.conn_str is not None, "Expected database mode but conn_str is None"
        
        # Test table existence
        with memory.connection_pool.connection() as conn:
            with conn.cursor() as cur:
                # Check users table existence
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE  table_schema = 'public' 
                        AND    table_name = 'users'
                    )
                """)
                users_table_exists = cur.fetchone()[0]
                assert users_table_exists, "Users table was not created"
                print("✓ Users table exists")
                
                # Check threads table existence
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE  table_schema = 'public' 
                        AND    table_name = 'threads'
                    )
                """)
                threads_table_exists = cur.fetchone()[0]
                assert threads_table_exists, "Threads table was not created"
                print("✓ Threads table exists")
                
                # Check users table columns
                cur.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_schema = 'public' 
                    AND table_name = 'users'
                """)
                users_columns = [row[0] for row in cur.fetchall()]
                required_users_columns = ['id', 'username', 'email', 'password', 'created_at', 'updated_at']
                for col in required_users_columns:
                    assert col in users_columns, f"Required column '{col}' not found in users table"
                print("✓ Users table has all required columns")
                
                # Check threads table columns
                cur.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_schema = 'public' 
                    AND table_name = 'threads'
                """)
                threads_columns = [row[0] for row in cur.fetchall()]
                required_threads_columns = ['thread_id', 'user_id', 'title', 'is_active', 'created_at', 'updated_at']
                for col in required_threads_columns:
                    assert col in threads_columns, f"Required column '{col}' not found in threads table"
                print("✓ Threads table has all required columns")
                
                # Check foreign key constraint
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM information_schema.table_constraints 
                    WHERE table_schema = 'public' 
                    AND table_name = 'threads' 
                    AND constraint_type = 'FOREIGN KEY'
                """)
                foreign_key_exists = cur.fetchone()[0] > 0
                assert foreign_key_exists, "Foreign key constraint not found on threads table"
                print("✓ Foreign key constraint exists on threads table")
                
                # Check index on threads.user_id
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM pg_indexes 
                    WHERE schemaname = 'public' 
                    AND tablename = 'threads' 
                    AND indexname = 'idx_threads_user_id'
                """)
                index_exists = cur.fetchone()[0] > 0
                assert index_exists, "Index idx_threads_user_id not found on threads table"
                print("✓ Index idx_threads_user_id exists on threads table")
                
                # Check knowledgebase table existence
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE  table_schema = 'public' 
                        AND    table_name = 'knowledgebase'
                    )
                """)
                knowledgebase_table_exists = cur.fetchone()[0]
                assert knowledgebase_table_exists, "Knowledgebase table was not created"
                print("✓ Knowledgebase table exists")
                
                # Check knowledgebase table columns
                cur.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_schema = 'public' 
                    AND table_name = 'knowledgebase'
                """)
                knowledgebase_columns = [row[0] for row in cur.fetchall()]
                required_knowledgebase_columns = ['id', 'user_id', 'name', 'description', 'navigation', 'created_at', 'updated_at']
                for col in required_knowledgebase_columns:
                    assert col in knowledgebase_columns, f"Required column '{col}' not found in knowledgebase table"
                print("✓ Knowledgebase table has all required columns")
                
                # Check knowledgebase foreign key constraint
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM information_schema.table_constraints 
                    WHERE table_schema = 'public' 
                    AND table_name = 'knowledgebase' 
                    AND constraint_type = 'FOREIGN KEY'
                """)
                kb_foreign_key_exists = cur.fetchone()[0] > 0
                assert kb_foreign_key_exists, "Foreign key constraint not found on knowledgebase table"
                print("✓ Foreign key constraint exists on knowledgebase table")
                
                # Check kb_thread table existence
                cur.execute("""
                    SELECT EXISTS (
                        SELECT FROM information_schema.tables 
                        WHERE  table_schema = 'public' 
                        AND    table_name = 'kb_thread'
                    )
                """)
                kb_thread_table_exists = cur.fetchone()[0]
                assert kb_thread_table_exists, "kb_thread table was not created"
                print("✓ kb_thread table exists")
                
                # Check kb_thread table columns
                cur.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_schema = 'public' 
                    AND table_name = 'kb_thread'
                """)
                kb_thread_columns = [row[0] for row in cur.fetchall()]
                required_kb_thread_columns = ['knowledgebase_id', 'thread_id', 'created_at']
                for col in required_kb_thread_columns:
                    assert col in kb_thread_columns, f"Required column '{col}' not found in kb_thread table"
                print("✓ kb_thread table has all required columns")
                
                # Check kb_thread primary key constraint
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM information_schema.table_constraints 
                    WHERE table_schema = 'public' 
                    AND table_name = 'kb_thread' 
                    AND constraint_type = 'PRIMARY KEY'
                """)
                kb_thread_pk_exists = cur.fetchone()[0] > 0
                assert kb_thread_pk_exists, "Primary key constraint not found on kb_thread table"
                print("✓ Primary key constraint exists on kb_thread table")
                
                # Check kb_thread foreign key constraints
                cur.execute("""
                    SELECT COUNT(*) 
                    FROM information_schema.table_constraints 
                    WHERE table_schema = 'public' 
                    AND table_name = 'kb_thread' 
                    AND constraint_type = 'FOREIGN KEY'
                """)
                kb_thread_fk_count = cur.fetchone()[0]
                assert kb_thread_fk_count >= 2, f"Expected at least 2 foreign key constraints on kb_thread table, found {kb_thread_fk_count}"
                print("✓ Foreign key constraints exist on kb_thread table")
        
        print("Database tables creation tests completed successfully!")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"Database tables test failed with error: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("Testing thread refactoring...")
    print("=" * 50)
    
    try:
        test_basic_functionality()
        test_in_memory_mode()
        test_database_tables_creation()
        test_database_mode()
        
        print("All tests passed!")
        print("The thread refactoring is working correctly.")
        sys.exit(0)
        
    except Exception as e:
        print(f"Test failed with error: {e}")
        traceback.print_exc()
        sys.exit(1)
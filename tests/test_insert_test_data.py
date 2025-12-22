import os
import sys
import traceback
import uuid
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Append src to path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from memory.memory import MemoryManager
from memory.thread import ThreadManager


def insert_test_data():
    """
    Insert test user and test thread into the database.
    """
    print("Inserting test data into database...")
    
    try:
        # Create memory manager with actual database connection
        memory_manager = MemoryManager()
        
        # Create thread manager
        thread_manager = ThreadManager(memory_manager)
        
        # Check if DB_URI is set
        if not memory_manager.conn_str:
            print("Error: DB_URI environment variable is not set.")
            print("Please set DB_URI in .env file or as environment variable.")
            return False
        
        # Create test user
        test_username = "testuser"
        test_email = "test@example.com"
        test_password = "password123"
        
        print(f"Creating test user: {test_username} ({test_email})")
        
        # Try to create the user, if it already exists, find it
        try:
            user_id = memory_manager.create_user(test_username, test_email, test_password)
            print(f"Created test user with ID: {user_id}")
        except ValueError as e:
            if "Username or email already exists" in str(e):
                print(f"User already exists: {e}")
                # Find the existing user
                with memory_manager.connection_pool.connection() as conn:
                    with conn.cursor() as cur:
                        cur.execute(
                            "SELECT id FROM users WHERE username = %s",
                            (test_username,)
                        )
                        user_id = cur.fetchone()[0]
                        print(f"Found existing user with ID: {user_id}")
            else:
                raise
        
        # Create test thread for the user
        thread_title = "Test Conversation"
        print(f"Creating test thread for user {user_id}: {thread_title}")
        thread_id = thread_manager.create_thread(user_id, thread_title)
        print(f"Created test thread with ID: {thread_id}")
        
        # Set the thread as active
        success = thread_manager.set_active_thread(user_id, thread_id)
        if success:
            print(f"Set thread {thread_id} as active for user {user_id}")
        else:
            print(f"Failed to set thread {thread_id} as active for user {user_id}")
        
        print("Test data insertion completed successfully!")
        print("=" * 50)
        print(f"Test user credentials:")
        print(f"Username: {test_username}")
        print(f"Email: {test_email}")
        print(f"Password: {test_password}")
        print(f"Active Thread ID: {thread_id}")
        print("=" * 50)
        return True
    except Exception as e:
        print(f"Error inserting test data: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    insert_test_data()
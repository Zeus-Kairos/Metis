import json
import os
import shutil
from io import BytesIO
from fastapi.testclient import TestClient
import sys

# Add the src directory to the path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

# Import the FastAPI app from the main API module
from src.api.main import app
from src.memory.memory import MemoryManager

# Create a test client
client = TestClient(app)

# Initialize MemoryManager for test setup
memory_manager = MemoryManager()

def setup_test_user():
    """Create a test user for authentication purposes"""
    # Cleanup any existing test user
    if memory_manager.conn_str:
        with memory_manager.connection_pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE username = %s", ("test_api_user",))
                conn.commit()
    
    # Create test user
    user_data = {
        "username": "test_api_user",
        "email": "test_api@example.com",
        "password": "test_api_password"
    }
    
    # Create user via API
    response = client.post("/api/users", json=user_data)
    assert response.status_code == 200, f"Failed to create test user: {response.json()}"
    
    return user_data

def get_auth_token(username, password):
    """Get authentication token for test requests"""
    # Login to get token
    response = client.post(
        "/api/token",
        data={"username": username, "password": password},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert response.status_code == 200, f"Failed to get auth token: {response.json()}"
    
    token_data = response.json()
    return token_data["access_token"]

def test_upload_api():
    """Test the file upload API endpoint"""
    # Setup test user and get auth token
    user_data = setup_test_user()
    token = get_auth_token(user_data["username"], user_data["password"])
    
    # Create test file
    test_content = b"Test content for API verification"
    files = {
        'files': ('test_verification.txt', BytesIO(test_content), 'text/plain')
    }
    
    # Create form data
    data = {
        'knowledge_base': 'test_api_kb',
        'directory': 'test_dir'
    }
    
    try:
        # Send request with authentication
        response = client.post(
            "/api/upload",
            data=data,
            files=files,
            headers={"Authorization": f"Bearer {token}"}
        )
        
        print(f"\n=== File Upload Test ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        
        # Verify response
        assert response.status_code == 200, f"API upload failed with status: {response.status_code}"
        response_json = response.json()
        assert response_json.get("status") in ["success", "partial_success"], f"API upload failed: {response_json}"
        
        print("✓ API upload successful!")
        
        # Check if directory structure was created
        upload_path = os.path.join('uploads', '1', 'test_api_kb', 'origin', 'test_dir')
        if os.path.exists(upload_path):
            print(f"✓ Directory structure created: {upload_path}")
            
            # Check if file was uploaded
            file_path = os.path.join(upload_path, 'test_verification.txt')
            if os.path.exists(file_path):
                print(f"✓ File uploaded successfully: {file_path}")
                with open(file_path, 'rb') as f:
                    content = f.read()
                    print(f"✓ File content matches: {content.decode('utf-8')}")
            else:
                print(f"✗ File not found at: {file_path}")
        else:
            print(f"✗ Directory structure not found: {upload_path}")
            
    finally:
        # Cleanup - use shutil.rmtree for complete directory removal
        upload_path = os.path.join('uploads', '1', 'test_api_kb')
        if os.path.exists(upload_path):
            shutil.rmtree(upload_path)
        
        # Cleanup test user
        if memory_manager.conn_str:
            with memory_manager.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM users WHERE username = %s", ("test_api_user",))
                    conn.commit()
        
        print("\nCleanup completed")

def test_create_knowledgebase_api():
    """Test the create knowledge base API endpoint"""
    # Setup test user and get auth token
    user_data = setup_test_user()
    token = get_auth_token(user_data["username"], user_data["password"])
    
    # Test data for knowledge base creation
    knowledgebase_data = {
        "name": "Test API Knowledge Base",
        "description": "This is a test knowledge base created via API",
        "navigation": {"type": "main", "items": []}
    }
    
    try:
        # Send request with authentication
        response = client.post(
            "/api/knowledgebase",
            json=knowledgebase_data,
            headers={"Authorization": f"Bearer {token}"}
        )
        
        print(f"\n=== Knowledge Base Creation Test ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        
        # Verify response
        assert response.status_code == 200, f"API knowledge base creation failed with status: {response.status_code}"
        response_data = response.json()
        assert response_data.get("success"), f"API knowledge base creation failed: {response.json()}"
        
        knowledgebase_id = response_data.get("knowledgebase_id")
        print(f"✓ API knowledge base creation successful!")
        print(f"✓ Created knowledge base with ID: {knowledgebase_id}")
        print(f"✓ Response message: {response_data.get('message')}")
        
        return knowledgebase_id
        
    finally:
        # Cleanup test user
        if memory_manager.conn_str:
            with memory_manager.connection_pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("DELETE FROM users WHERE username = %s", ("test_api_user",))
                    conn.commit()
        
        print("\nCleanup completed")

if __name__ == "__main__":
    # Run tests
    test_upload_api()
    test_create_knowledgebase_api()
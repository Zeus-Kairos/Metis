import requests
from io import BytesIO
import os
import shutil
import json

# Create a test user first to ensure user_id exists
def create_test_user():
    user_data = {
        "username": "test_api_user",
        "email": "test_api@example.com",
        "password": "test_api_password"
    }
    
    try:
        # Create user via the API if available, otherwise use direct DB access
        # Note: Currently there's no public API for user creation, so we'll assume user_id 1 exists
        print("Assuming test user with ID 1 exists")
        return 1
    except Exception as e:
        print(f"✗ Exception creating test user: {e}")
        return None

# Test the upload endpoint with the new directory structure
def test_upload_api(user_id=1):
    # Create test file
    test_content = b"Test content for API verification"
    files = {'files': ('test_verification.txt', BytesIO(test_content), 'text/plain')}
    data = {'user_id': user_id, 'knowledge_base': 'test_api_kb', 'directory': 'test_dir'}
    
    try:
        # Send request
        response = requests.post('http://localhost:8000/api/upload', data=data, files=files)
        
        print(f"\n=== File Upload Test ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        
        # Verify response
        if response.status_code == 200:
            print("✓ API upload successful!")
            
            # Check if directory structure was created
            upload_path = os.path.join('uploads', str(user_id), 'test_api_kb', 'origin', 'test_dir')
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
        else:
            print("✗ API upload failed")
            
    finally:
        # Cleanup - use shutil.rmtree for complete directory removal
        upload_path = os.path.join('uploads', str(user_id), 'test_api_kb')
        if os.path.exists(upload_path):
            shutil.rmtree(upload_path)
        
        print("\nCleanup completed")

# Test the create knowledge base endpoint
def test_create_knowledgebase_api(user_id=1):
    # Test data for knowledge base creation
    knowledgebase_data = {
        "user_id": user_id,
        "name": "Test API Knowledge Base",
        "description": "This is a test knowledge base created via API",
        "navigation": {"type": "main", "items": []}
    }
    
    try:
        # Send POST request to create knowledge base
        response = requests.post('http://localhost:8000/api/knowledgebase', json=knowledgebase_data)
        
        print(f"\n=== Knowledge Base Creation Test ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        
        # Verify response
        if response.status_code == 200:
            response_data = response.json()
            if response_data.get("success"):
                knowledgebase_id = response_data.get("knowledgebase_id")
                print(f"✓ API knowledge base creation successful!")
                print(f"✓ Created knowledge base with ID: {knowledgebase_id}")
                print(f"✓ Response message: {response_data.get('message')}")
                return knowledgebase_id  # Return for potential further tests
            else:
                print("✗ API knowledge base creation failed - response indicates failure")
        else:
            print("✗ API knowledge base creation failed with status code")
            
    except Exception as e:
        print(f"✗ Exception occurred: {e}")
    
    return None

if __name__ == "__main__":
    # Create test user
    user_id = create_test_user()
    
    if user_id:
        # Run upload test
        test_upload_api(user_id)
        
        # Run knowledge base creation test
        test_create_knowledgebase_api(user_id)
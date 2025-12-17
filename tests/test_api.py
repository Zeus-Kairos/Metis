import requests
from io import BytesIO
import os
import shutil

# Test the upload endpoint with the new directory structure
def test_upload_api():
    # Create test file
    test_content = b"Test content for API verification"
    files = {'files': ('test_verification.txt', BytesIO(test_content), 'text/plain')}
    data = {'user_id': 'test_user', 'knowledge_base': 'test_api_kb', 'directory': 'test_dir'}
    
    try:
        # Send request
        response = requests.post('http://localhost:8000/api/upload', data=data, files=files)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        
        # Verify response
        if response.status_code == 200:
            print("✓ API upload successful!")
            
            # Check if directory structure was created
            upload_path = os.path.join('uploads', 'test_user', 'test_api_kb', 'origin', 'test_dir')
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
        upload_path = os.path.join('uploads', 'test_user', 'test_api_kb')
        if os.path.exists(upload_path):
            shutil.rmtree(upload_path)
        
        print("\nCleanup completed")

if __name__ == "__main__":
    test_upload_api()
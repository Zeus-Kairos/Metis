import pytest
import sys
import time
from datetime import datetime
from fastapi.testclient import TestClient
from src.api.main import app
import json
import random
import string

# Add the project root to Python path
sys.path.insert(0, r'c:\Apps\Metis')

client = TestClient(app)

# Function to generate random string
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def test_unique_constraints():
    """Test unique constraints for username and email."""
    
    # Test 1: Create a new user (should succeed)
    username = f"testuser_{generate_random_string()}"
    email = f"test_{generate_random_string()}@example.com"
    password = "TestPassword123!"
    
    response = client.post(
        "/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "email": email, "password": password})
    )
    
    print(f"Test 1: Create new user ({username}, {email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json()["success"] == True
    
    # Test 2: Create a user with the same username (should fail with 400)
    duplicate_email = f"test_{generate_random_string()}@example.com"
    response = client.post(
        "/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "email": duplicate_email, "password": password})
    )
    
    print(f"Test 2: Create user with duplicate username ({username}, {duplicate_email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    assert response.status_code == 400, f"Expected status 400, got {response.status_code}"
    assert "duplicate" in response.json()["detail"].lower() or "already exists" in response.json()["detail"].lower()
    
    # Test 3: Create a user with the same email (should fail with 400)
    duplicate_username = f"testuser_{generate_random_string()}"
    response = client.post(
        "/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": duplicate_username, "email": email, "password": password})
    )
    
    print(f"Test 3: Create user with duplicate email ({duplicate_username}, {email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    assert response.status_code == 400, f"Expected status 400, got {response.status_code}"
    assert "duplicate" in response.json()["detail"].lower() or "already exists" in response.json()["detail"].lower()
    
    # Test 4: Create a user with both username and email different (should succeed)
    new_username = f"testuser_{generate_random_string()}"
    new_email = f"test_{generate_random_string()}@example.com"
    response = client.post(
        "/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": new_username, "email": new_email, "password": password})
    )
    
    print(f"Test 4: Create another new user ({new_username}, {new_email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json()["success"] == True
    
    print("\n✅ All tests PASSED! Unique constraint handling is working correctly.")

def test_knowledgebase_name_unique_per_user():
    """
    Test that knowledgebase names must be unique for each user.
    """
    # Generate unique timestamp for this test run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    username = f"testuser_kb_{timestamp}"
    email = f"{username}@example.com"
    
    print(f"Using unique username: {username}")
    
    # Step 1: Create a new user
    user_data = {
        "username": username,
        "email": email,
        "password": "TestPassword123!"
    }

    response = client.post("/api/users", json=user_data)
    print(f"User creation response: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    
    # Step 2: Login to get token
    login_data = {
        "username": username,
        "password": "TestPassword123!"
    }

    response = client.post("/api/token", data=login_data)
    print(f"Login response: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    
    token = response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Step 3: Create first knowledgebase with name "Test KB"
    kb_data = {
        "name": "Test KB",
        "description": "First test knowledgebase"
    }

    response = client.post("/api/knowledgebase", headers=headers, json=kb_data)
    print(f"First KB creation response: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    kb1_id = response.json()["knowledgebase_id"]
    
    # Step 4: Try to create another knowledgebase with the same name for the same user
    kb_data_same = {
        "name": "Test KB",
        "description": "Second test knowledgebase with same name"
    }

    response = client.post("/api/knowledgebase", headers=headers, json=kb_data_same)
    print(f"Second KB creation response (same name): {response.status_code}, {response.json()}")
    assert response.status_code == 400  # Should fail with duplicate error
    
    # Step 5: Create another knowledgebase with different name for the same user
    kb_data_diff = {
        "name": "Test KB 2",
        "description": "Third test knowledgebase with different name"
    }

    response = client.post("/api/knowledgebase", headers=headers, json=kb_data_diff)
    print(f"Third KB creation response (different name): {response.status_code}, {response.json()}")
    assert response.status_code == 200
    kb3_id = response.json()["knowledgebase_id"]
    
    # Cleanup
    print("Cleaning up test data...")
    
    # Create another user for cross-user test
    username2 = f"testuser_kb2_{timestamp}"
    email2 = f"{username2}@example.com"
    
    user_data2 = {
        "username": username2,
        "email": email2,
        "password": "TestPassword123!"
    }

    response = client.post("/api/users", json=user_data2)
    print(f"Second user creation response: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    
    # Login as second user
    login_data2 = {
        "username": username2,
        "password": "TestPassword123!"
    }

    response = client.post("/api/token", data=login_data2)
    print(f"Second user login response: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    
    token2 = response.json()["access_token"]
    headers2 = {"Authorization": f"Bearer {token2}"}
    
    # Step 6: Create knowledgebase with same name as first user's KB
    kb_data_same_other_user = {
        "name": "Test KB",
        "description": "Knowledgebase with same name as another user's KB"
    }

    response = client.post("/api/knowledgebase", headers=headers2, json=kb_data_same_other_user)
    print(f"KB creation response (same name, different user): {response.status_code}, {response.json()}")
    assert response.status_code == 200  # Should succeed for different user
    
    print("All tests passed!")

if __name__ == "__main__":
    print("Testing unique constraint handling...")
    print("=" * 50)
    test_unique_constraints()
    print("\n" + "=" * 50)
    print("Testing knowledgebase name uniqueness per user...")
    print("=" * 50)
    test_knowledgebase_name_unique_per_user()
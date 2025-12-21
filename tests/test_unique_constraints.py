import pytest
from fastapi.testclient import TestClient
from src.api.main import app
import json
import random
import string

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

if __name__ == "__main__":
    print("Testing unique constraint handling...")
    print("=" * 50)
    test_unique_constraints()

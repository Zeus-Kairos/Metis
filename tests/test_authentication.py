import sys
import os

# Add the src directory to the path BEFORE importing from src
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from fastapi.testclient import TestClient
from src.api.main import app
from src.memory.memory import MemoryManager
import time

client = TestClient(app)
memory_manager = MemoryManager()

# Test data with unique values
TEST_USER = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "test123"  # Shorter password within 72-byte limit
}

def test_user_creation():
    """Test creating a new user."""
    print("=== Testing User Creation ===")
    
    # Cleanup any existing user directly from the database
    try:
        with memory_manager.connection_pool.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM users WHERE username = %s OR email = %s", 
                           (TEST_USER["username"], TEST_USER["email"]))
                conn.commit()
        print("✓ Cleaned up any existing test user")
    except Exception as e:
        print(f"⚠ Error during cleanup: {e}")
    
    # Create new user
    response = client.post("/api/users", json=TEST_USER)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    print("✓ User creation test passed!")
    return response.json()


def get_token():
    """Get a JWT token for the test user."""
    login_data = {
        "username": TEST_USER["username"],
        "password": TEST_USER["password"]
    }
    response = client.post("/api/token", data=login_data)
    return response.json()["access_token"]


def test_login():
    """Test logging in to get a JWT token."""
    print("\n=== Testing Login ===")
    login_data = {
        "username": TEST_USER["username"],
        "password": TEST_USER["password"]
    }
    response = client.post("/api/token", data=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "access_token" in response.json(), "Expected access_token in response"
    assert "token_type" in response.json(), "Expected token_type in response"
    print("✓ Login test passed!")
    return response.json()


def test_protected_endpoint():
    """Test accessing a protected endpoint with the JWT token."""
    print("\n=== Testing Protected Endpoint ===")
    
    # Get a token first
    token = get_token()
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get("/api/users/me", headers=headers)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json()["username"] == TEST_USER["username"], f"Expected username {TEST_USER['username']}"
    assert response.json()["email"] == TEST_USER["email"], f"Expected email {TEST_USER['email']}"
    print("✓ Protected endpoint test passed!")
    return response.json()


def test_unauthorized_access():
    """Test accessing a protected endpoint without a token."""
    print("\n=== Testing Unauthorized Access ===")
    response = client.get("/api/users/me")
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 401, f"Expected status 401, got {response.status_code}"
    print("✓ Unauthorized access test passed!")


if __name__ == "__main__":
    try:
        # Run all tests
        user_data = test_user_creation()
        token_data = test_login()
        protected_data = test_protected_endpoint()  # No longer needs token_data parameter
        test_unauthorized_access()
        
        print("\n🎉 All authentication tests passed successfully!")
        print(f"\nTest Summary:")
        print(f"- User created with ID: {user_data['user_id']}")
        print(f"- Token received: {token_data['access_token'][:20]}...")
        print(f"- Token type: {token_data['token_type']}")
        print(f"- User data retrieved: {protected_data}")
        
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
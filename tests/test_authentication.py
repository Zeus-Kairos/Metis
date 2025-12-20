import requests
import json

BASE_URL = "http://127.0.0.1:8000"

# Test data
TEST_USER = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "test123"  # Shorter password within 72-byte limit
}


def test_user_creation():
    """Test creating a new user."""
    print("=== Testing User Creation ===")
    response = requests.post(f"{BASE_URL}/api/users", json=TEST_USER)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert response.json()["success"] is True, "Expected success to be True"
    print("✓ User creation test passed!")
    return response.json()


def test_login():
    """Test logging in to get a JWT token."""
    print("\n=== Testing Login ===")
    login_data = {
        "username": TEST_USER["username"],
        "password": TEST_USER["password"]
    }
    response = requests.post(f"{BASE_URL}/api/token", data=login_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200, f"Expected status 200, got {response.status_code}"
    assert "access_token" in response.json(), "Expected access_token in response"
    assert "token_type" in response.json(), "Expected token_type in response"
    print("✓ Login test passed!")
    return response.json()


def test_protected_endpoint(token_data):
    """Test accessing a protected endpoint with the JWT token."""
    print("\n=== Testing Protected Endpoint ===")
    headers = {
        "Authorization": f"Bearer {token_data['access_token']}"
    }
    response = requests.get(f"{BASE_URL}/api/users/me", headers=headers)
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
    response = requests.get(f"{BASE_URL}/api/users/me")
    print(f"Status Code: {response.status_code}")
    assert response.status_code == 401, f"Expected status 401, got {response.status_code}"
    print("✓ Unauthorized access test passed!")


if __name__ == "__main__":
    try:
        # Run all tests
        user_data = test_user_creation()
        token_data = test_login()
        protected_data = test_protected_endpoint(token_data)
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
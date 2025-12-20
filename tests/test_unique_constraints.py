import requests
import json
import random
import string

# Base URL for the API
BASE_URL = "http://localhost:8000"

# Function to generate random string
def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Test 1: Create a new user (should succeed)
def test_create_user():
    username = f"testuser_{generate_random_string()}"
    email = f"test_{generate_random_string()}@example.com"
    password = "TestPassword123!"
    
    response = requests.post(
        f"{BASE_URL}/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "email": email, "password": password})
    )
    
    print(f"Test 1: Create new user ({username}, {email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    return username, email, response.status_code

# Test 2: Create a user with the same username (should fail with 400)
def test_create_duplicate_username(original_username):
    username = original_username
    email = f"test_{generate_random_string()}@example.com"
    password = "TestPassword123!"
    
    response = requests.post(
        f"{BASE_URL}/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "email": email, "password": password})
    )
    
    print(f"Test 2: Create user with duplicate username ({username}, {email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    return response.status_code

# Test 3: Create a user with the same email (should fail with 400)
def test_create_duplicate_email(original_email):
    username = f"testuser_{generate_random_string()}"
    email = original_email
    password = "TestPassword123!"
    
    response = requests.post(
        f"{BASE_URL}/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "email": email, "password": password})
    )
    
    print(f"Test 3: Create user with duplicate email ({username}, {email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    return response.status_code

# Test 4: Create a user with both username and email different (should succeed)
def test_create_another_user():
    username = f"testuser_{generate_random_string()}"
    email = f"test_{generate_random_string()}@example.com"
    password = "TestPassword123!"
    
    response = requests.post(
        f"{BASE_URL}/api/users",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"username": username, "email": email, "password": password})
    )
    
    print(f"Test 4: Create another new user ({username}, {email})")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    print("-" * 50)
    
    return response.status_code

# Run all tests
if __name__ == "__main__":
    print("Testing unique constraint handling...")
    print("=" * 50)
    
    # Run tests
    username, email, status1 = test_create_user()
    status2 = test_create_duplicate_username(username)
    status3 = test_create_duplicate_email(email)
    status4 = test_create_another_user()
    
    # Summary
    print("\nTest Summary:")
    print(f"Test 1 (Create new user): {'PASS' if status1 == 200 else 'FAIL'} (Status: {status1})")
    print(f"Test 2 (Duplicate username): {'PASS' if status2 == 400 else 'FAIL'} (Status: {status2})")
    print(f"Test 3 (Duplicate email): {'PASS' if status3 == 400 else 'FAIL'} (Status: {status3})")
    print(f"Test 4 (Create another user): {'PASS' if status4 == 200 else 'FAIL'} (Status: {status4})")
    
    # Overall result
    if status1 == 200 and status2 == 400 and status3 == 400 and status4 == 200:
        print("\n✅ All tests PASSED! Unique constraint handling is working correctly.")
    else:
        print("\n❌ Some tests FAILED. Please check the results above.")



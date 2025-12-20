# Minimal test script to debug password hashing issue

from passlib.context import CryptContext

# Test password (very short, should be well under 72 bytes)
test_password = "test123"

print(f"Testing password: {test_password}")
print(f"Password length in characters: {len(test_password)}")
print(f"Password length in bytes: {len(test_password.encode('utf-8'))} bytes")

try:
    # Create password context
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    
    # Try to hash the password
    hashed_password = pwd_context.hash(test_password)
    print(f"✓ Password hashed successfully: {hashed_password}")
    
    # Try with truncation
    test_password_long = "a" * 100  # 100 characters, way over 72 bytes
    print(f"\nTesting long password (100 'a's):")
    print(f"Long password length in bytes: {len(test_password_long.encode('utf-8'))} bytes")
    
    # First try without truncation
    try:
        hashed_password_long = pwd_context.hash(test_password_long)
        print(f"✓ Long password hashed successfully without truncation: {hashed_password_long}")
    except Exception as e:
        print(f"✗ Error hashing long password: {e}")
        
    # Then try with truncation to 72 bytes
    try:
        # Encode to bytes and truncate
        password_bytes = test_password_long.encode('utf-8')[:72]
        password_truncated = password_bytes.decode('utf-8', 'ignore')
        hashed_password_truncated = pwd_context.hash(password_truncated)
        print(f"✓ Long password hashed successfully with truncation: {hashed_password_truncated}")
    except Exception as e:
        print(f"✗ Error hashing truncated long password: {e}")
        
except Exception as e:
    print(f"✗ Unexpected error: {e}")
    import traceback
    traceback.print_exc()

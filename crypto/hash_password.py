from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

# Initialize Argon2id PasswordHasher with secure defaults
ph = PasswordHasher()

def hash_password(plain_text: str) -> str:
    """Generates a secure Argon2id hash with a cryptographically unique salt."""
    if not isinstance(plain_text, str) or not plain_text:
        raise ValueError("Password must be a non-empty string.")
    return ph.hash(plain_text)

def verify_password(plain_text: str, stored_hash: str) -> bool:
    """Verifies a plaintext password against an Argon2id hash in constant time."""
    try:
        return ph.verify(stored_hash, plain_text)
    except VerifyMismatchError:
        return False
    except Exception:
        return False

if __name__ == "__main__":
    test_pwd = "SuperSecurePassword123!"
    h1 = hash_password(test_pwd)
    h2 = hash_password(test_pwd)
    
    print(f"Password: {test_pwd}")
    print(f"Hash 1: {h1}")
    print(f"Hash 2: {h2}")
    print(f"Hashes match: {h1 == h2}")
    print(f"Verification Check: {verify_password(test_pwd, h1)}")

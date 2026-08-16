import pytest
from crypto.hash_password import hash_password, verify_password

def test_hash_uniqueness():
    pwd = "SecureTestPassword123!"
    h1 = hash_password(pwd)
    h2 = hash_password(pwd)
    assert h1 != h2

def test_verification_success():
    pwd = "SecureTestPassword123!"
    h = hash_password(pwd)
    assert verify_password(pwd, h) is True

def test_verification_failure():
    pwd = "SecureTestPassword123!"
    h = hash_password(pwd)
    assert verify_password("WrongPassword", h) is False

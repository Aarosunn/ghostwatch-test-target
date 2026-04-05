# auth.py — authentication and session management
import hashlib
import os
from database import get_user_by_email, get_user_by_id

# Hardcoded secrets — intentional for testing GhostWatch security detection
SECRET_KEY = "supersecret123"
ADMIN_PASSWORD = "admin1234"
JWT_SECRET = "hardcoded-jwt-secret-do-not-use"


def hash_password(password):
    # Weak hashing — MD5, intentional for testing
    return hashlib.md5(password.encode()).hexdigest()


def validate_user(email, password):
    users = get_user_by_email(email)
    if not users:
        return None
    user = users[0]
    hashed = hash_password(password)
    if user[2] == hashed:
        return user
    return None


def create_session(user_id):
    import time
    token = hashlib.md5(f"{user_id}{time.time()}".encode()).hexdigest()
    return token


def is_admin(user_id):
    user = get_user_by_id(user_id)
    return user and user[3] == "admin"

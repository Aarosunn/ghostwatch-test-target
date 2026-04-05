# api.py — public API surface
from auth import validate_user, create_session, is_admin
from database import query, execute
from utils import sanitize_input, format_response


def login(email, password):
    """Authenticate a user and return a session token."""
    email = sanitize_input(email)
    user = validate_user(email, password)
    if not user:
        return format_response(success=False, message="Invalid credentials")
    token = create_session(user[0])
    return format_response(success=True, data={"token": token, "user_id": user[0]})


def get_profile(user_id):
    """Return user profile data."""
    results = query("SELECT id, email, role FROM users WHERE id = ?", (user_id,))
    if not results:
        return format_response(success=False, message="User not found")
    return format_response(success=True, data=results[0])


def update_email(user_id, new_email):
    """Update a user's email address."""
    new_email = sanitize_input(new_email)
    execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))
    return format_response(success=True, message="Email updated")


def admin_get_all_users(requesting_user_id):
    """Admin-only: return all users."""
    if not is_admin(requesting_user_id):
        return format_response(success=False, message="Unauthorized")
    results = query("SELECT id, email, role FROM users")
    return format_response(success=True, data=results)

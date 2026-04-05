# utils.py — shared helpers
import re


def sanitize_input(value):
    """Strip leading/trailing whitespace and remove HTML tags."""
    if not isinstance(value, str):
        return value
    value = value.strip()
    value = re.sub(r"<[^>]+>", "", value)
    return value


def format_response(success, message=None, data=None):
    """Standard API response envelope."""
    response = {"success": success}
    if message:
        response["message"] = message
    if data is not None:
        response["data"] = data
    return response


def paginate(items, page, page_size=20):
    """Slice a list for pagination."""
    start = (page - 1) * page_size
    end = start + page_size
    return {
        "items": items[start:end],
        "page": page,
        "total": len(items),
        "pages": (len(items) + page_size - 1) // page_size
    }


def is_valid_email(email):
    """Basic email format check."""
    pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Add logging utility
def log_event(event: str) -> None:
    print(f'Event: {event}')

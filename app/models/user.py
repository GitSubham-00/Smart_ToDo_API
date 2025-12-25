from datetime import datetime, timezone

def user_model(username: str, email: str, hashed_password: str) -> dict:
    return {
        "username": username,
        "email": email,
        "hashed_password": hashed_password,
        "created_at": datetime.now(timezone.utc)
    }

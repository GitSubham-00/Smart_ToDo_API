
from datetime import datetime, timezone

def task_model(title: str, description: str, user_email: str) -> dict:
    return {
        "title": title,
        "description": description,
        "completed": False,
        "user_email": user_email,
        "created_at": datetime.now(timezone.utc)
    }

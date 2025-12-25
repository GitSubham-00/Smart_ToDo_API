from fastapi import APIRouter, HTTPException, Security
from bson import ObjectId
from app.database import db
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.models.task import task_model
from app.utils.auth_dependency import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

tasks_collection = db["tasks"]


@router.post("/")
def create_task(
    task: TaskCreate,
    user_email: str = Security(get_current_user)
):
    new_task = task_model(
        title=task.title,
        description=task.description,
        user_email=user_email
    )
    tasks_collection.insert_one(new_task)
    return {"message": "Task created successfully"}


@router.get("/")
def get_tasks(user_email: str = Security(get_current_user)):
    tasks = list(tasks_collection.find({"user_email": user_email}))
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks


@router.put("/{task_id}")
def update_task(
    task_id: str,
    task: TaskUpdate,
    user_email: str = Security(get_current_user)
):
    updated = tasks_collection.update_one(
        {"_id": ObjectId(task_id), "user_email": user_email},
        {"$set": {k: v for k, v in task.dict().items() if v is not None}}
    )

    if updated.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task updated successfully"}


@router.delete("/{task_id}")
def delete_task(
    task_id: str,
    user_email: str = Security(get_current_user)
):
    deleted = tasks_collection.delete_one(
        {"_id": ObjectId(task_id), "user_email": user_email}
    )

    if deleted.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}

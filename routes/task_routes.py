from fastapi import APIRouter
from app.models.task import Task
from app.database.connection import tasks_collection
from bson import ObjectId

task_router = APIRouter()

@task_router.post("/tasks")
async def create_task(task: Task):
    task_dict = task.dict()
    result = tasks_collection.insert_one(task_dict)
    return {"id": str(result.inserted_id), "message": "Task created successfully"}

@task_router.get("/tasks")
async def get_tasks():
    tasks = list(tasks_collection.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks

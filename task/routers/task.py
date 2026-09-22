from fastapi import APIRouter, HTTPException, status
from models.task import Task

task_router = APIRouter()

@task_router.get("", response_model=Task)
async def get_tasks():
    return 
from typing import Annotated
from fastapi import APIRouter, Depends
from repo import TaskRepo
from schemas import STask, STaskAdd, STaskID

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)

@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepo.add_one(task)
    return {"OK": True, "task_id": task_id}

@router.get("")
async def get_tasks() -> list[STask]: 
    tasks = await TaskRepo.find_all()
    return tasks
    
    





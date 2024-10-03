from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import tasks as crud_tasks
from app.schemas.task import Task as TaskSchema, Task, TaskCreate, TaskUpdate
from app.db.session import SessionLocal
from app.crud.tasks import get_tasks_by_project_id
from typing import List
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud_tasks.create_task(db=db, task=task)

@router.get("/", response_model=list[Task])
def read_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_tasks.get_tasks(db=db, skip=skip, limit=limit)

@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = crud_tasks.get_task(db=db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return crud_tasks.update_task(db=db, task_id=task_id, task=task)

@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud_tasks.delete_task(db=db, task_id=task_id)

@router.get("/tasks", response_model=List[TaskSchema])
async def read_tasks(proyecto_id: int, db: Session = Depends(get_db)):
    tasks = get_tasks_by_project_id(db, proyecto_id)
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return tasks
from fastapi import APIRouter, Depends, HTTPException, status
from ..database.database import get_db
from ..database import models
from sqlalchemy.orm import Session
from ..schemas.Task import Task, ResponseTask
from typing import List


router = APIRouter(
    prefix='/tasks',
    tags=['Task']
)

@router.get("/", response_model=List[ResponseTask])
def get_tasks(db: Session = Depends(get_db)):
    data = db.query(models.Task).all()
    return data

@router.post("/", response_model=ResponseTask)
def create_task(task: Task, db: Session = Depends(get_db)):
    task.model_dump()
    new_task = models.Task(**task.__dict__)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get('/{id}', response_model=ResponseTask)
def get_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the task with the id {id} was not found')
    return task

@router.delete('/{id}')
def delete_task(id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == id)
    if task.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the task with the id {id} was not found')
    task.delete(synchronize_session=False)
    db.commit()

@router.put("/{id}", response_model=ResponseTask)
def update_task(id: int, task: Task, db: Session = Depends(get_db)):
    db_query = db.query(models.Task).filter(models.Task.id == id)
    db_task = db_query.first()
    if db_task == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'the task with the id {id} was not found')
    
    db_query.update(task.model_dump(), synchronize_session=False)
    db.commit()

    return task
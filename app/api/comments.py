from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import comments as crud_comments
from app.schemas.comment import Comment, CommentCreate
from app.db.session import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Comment)
def create_comment(comment: CommentCreate, db: Session = Depends(get_db)):
    return crud_comments.create_comment(db=db, comment=comment)

@router.get("/{task_id}", response_model=list[Comment])
def read_comments(task_id: int, db: Session = Depends(get_db)):
    return crud_comments.get_comments(db=db, task_id=task_id)
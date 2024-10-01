from sqlalchemy.orm import Session
from app.db.models import Comment
from app.schemas.comment import CommentCreate

def get_comments(db: Session, task_id: int):
    return db.query(Comment).filter(Comment.tarea_id == task_id).all()

def create_comment(db: Session, comment: CommentCreate):
    db_comment = Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
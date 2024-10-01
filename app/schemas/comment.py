from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommentBase(BaseModel):
    tarea_id: int
    contenido: str
    usuario_id: int

class CommentCreate(CommentBase):
    pass

class CommentInDBBase(CommentBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True

class Comment(CommentInDBBase):
    pass
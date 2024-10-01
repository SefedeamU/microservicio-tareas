from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    estado: str
    proyecto_id: int
    responsable_id: int
    fecha_vencimiento: Optional[datetime] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskInDBBase(TaskBase):
    id: int
    fecha_creacion: datetime

    class Config:
        from_attributes = True

class Task(TaskInDBBase):
    pass
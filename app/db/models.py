from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(Text)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)
    estado = Column(String, index=True)
    proyecto_id = Column(Integer, index=True)
    responsable_id = Column(Integer, index=True)
    fecha_vencimiento = Column(DateTime)

    comentarios = relationship("Comment", back_populates="tarea")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    tarea_id = Column(Integer, ForeignKey("tasks.id"))
    contenido = Column(Text)
    usuario_id = Column(Integer, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)

    tarea = relationship("Task", back_populates="comentarios")
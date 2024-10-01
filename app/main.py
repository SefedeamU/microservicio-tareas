from fastapi import FastAPI
from app.api import tasks, comments
from app.db import models
from app.db.session import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

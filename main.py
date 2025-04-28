from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Task(BaseModel):
    id: int
    title: str
    completed: bool = False


tasks: List[Task] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API!"}


@app.post("/tasks/")
def create_task(task: Task):
    tasks.append(task)
    return task


@app.get("/tasks/")
def read_tasks():
    return tasks


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for t in tasks:
        if t.id == task_id:
            t.title = task.title
            t.completed = task.completed
            return t
    return {"error": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    glo
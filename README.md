# Task Manager API

A simple CRUD API built with FastAPI.

## Live Demo

https://task-manager-api-production-b6c2.up.railway.app/

## Endpoints

- `GET /` → Welcome message
- `POST /tasks/` → Create a new task
- `GET /tasks/` → Get all tasks
- `PUT /tasks/{task_id}` → Update a task
- `DELETE /tasks/{task_id}` → Delete a task

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

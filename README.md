# Task Manager API

A simple CRUD API built with FastAPI.

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

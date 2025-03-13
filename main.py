
from task_model import Task
from fastapi import FastAPI

app = FastAPI()

tasks = [
    Task(),
    Task()
]

@app.get("/")
def root():
    return "Hello world"

@app.get("/get-tasks")
def get_all_tasks():
    return tasks

@app.post("/create-task")
def create_task():
    return 

@app.put("/update-task")
def update_task():
    return 


@app.delete("/delete-task")
def delete_task():
    return
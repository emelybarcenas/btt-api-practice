
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
def create_task(task: Task):
    tasks.append(task)
   

@app.put("/update-task")
def update_task(task_id: int, updated_task: Task):
    for i, task in enumerate(tasks):
        if task_id == task_id:
            tasks[i] = update_task


@app.delete("/delete-task")
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task.id == task.id:
            deleted_task = tasks.pop(i)
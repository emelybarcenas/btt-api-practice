
from db_task_model import create_db_and_tables, get_session
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from task_model import Task
from db_task_service import *
from sqlmodel import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def root():
    return "Hello World"
@app.get("/tasks/all")
def get_all(session: Session = Depends(get_session)):
    return get_all_tasks(session)

@app.post("/task")
def create(task: Task, session: Session = Depends(get_session)):
    return create_task(task, session)    

@app.put("/{task_id}")
def update(task_id: int, updated:Task, session: Session = Depends(get_session)):
    return update_task(task_id, updated, session)

@app.delete("/task/delete/{task_id}")
def delete(task_id: int, session : Session = Depends(get_session)):
    return delete_task(task_id, session)

@app.get("/get-task/{task_id}")
def get (task_id: int, session: Session = Depends(get_session)):
    return get_task(task_id, session)


#If using just postman and no SQL:
# @app.get("/")
# def root():
#     return "Hello world"

# @app.get("/tasks/all")
# def get_all(session: Session = Depends(get_session)):
#     return get_all_tasks(session)
    

# @app.get("/get-tasks")
# def get_all_tasks():
#     return tasks

# @app.post("/create-task")
# def create_task(task: Task):
#     tasks.append(task)
#     return "Task created"
   

# @app.put("/update-task/{task_id}")
# def update_task(task_id: int, updated_task: Task):
#    for task in tasks:
#        if task.id == task_id:
#            task.description = updated_task.description
#            task.isComplete = updated_task.isComplete
#            return "Updated task"
           
#        return "task not found"

# @app.delete("/delete-task/{task_id}")
# def delete_task(task_id: int):
#     for i, task in enumerate(tasks):
#         if task.id == task.id:
#             deleted_task = tasks.pop(i)
#             return "Task deleted"
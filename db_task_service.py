from db_task_model import Task
from sqlmodel import select, Session

def get_all_tasks(session: Session):
    statement = select(Task)
    tasks = session.exec(statement).all()
    return tasks

def create_task(task: Task, session: Session):
    session.add(task)
    session.commit()
    session.refresh(task)
    return task

def update_task(task_id,updated: Task, session: Session):
    task = session.get(Task, task_id)

    if not task:
        return "task not found"
    
    task.description = updated.description
    task.isComplete = updated.isComplete

    session.commit()
    session.refresh(task)

    return task

def delete_task(task_id: int, session: Session):

    task = session.get(Task, task_id)


  # If task doesn't exist, return an error message
    if not task:
        return "Task not found"
    
    # Delete the task from the session
    session.delete(task)
    # Commit the changes to the database
    session.commit()

    return "Task deleted successfully"


def get_task(task_id: int, session: Session):
    """
    Retrieve a specific task by ID from the database.
    
    Args:
        task_id (int): The ID of the task to retrieve
        session (Session): The database session object
        
    Returns:
        Task or str: The requested Task object if found, or error message if not found
    """
    # Get the task with the specified ID
    task = session.get(Task, task_id)
    
    # If task doesn't exist, return an error message
    if not task:
        return "Task Not Found"
    
    return task
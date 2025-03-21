
from pydantic import BaseModel

cur_id = 0

def increment():
    global cur_id
    cur_id +=1
    return cur_id
    
class CreateTask(BaseModel):
    description: str = ""
    isCompleted: bool = False

class Task(BaseModel):
    id: int
    description: str = ""
    isComplete: bool = False

    def __init__(self, **data):
        super().__init__(id = increment(), **data)
 

from pydantic import BaseModel

class Task(BaseModel):
    title: str
    isComplete: bool = False

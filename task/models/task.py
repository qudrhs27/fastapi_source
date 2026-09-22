from pydantic import BaseModel

class Task(BaseModel):
    id: int
    text: str
    done: bool
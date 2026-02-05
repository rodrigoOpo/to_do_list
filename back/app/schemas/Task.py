from pydantic import BaseModel

class Base_Task(BaseModel):
    title: str
    content: str

class Task(Base_Task):
    pass

class ResponseTask(BaseModel):
    title: str
    content: str
    id: int
    class Config:
        from_attributes = True
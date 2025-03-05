from pydantic import BaseModel

class Question(BaseModel):
    q: str
from pydantic import BaseModel
from typing import List
from datetime import datetime
from answers.models import Answer

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime
    answers: List[Answer] = []

    class Config:
        orm_mode = True
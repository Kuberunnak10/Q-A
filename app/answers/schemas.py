from pydantic import BaseModel
from typing import List
from datetime import datetime

class AnswerBase(BaseModel):
    text: str
    user_id: str

class AnswerCreate(AnswerBase):
    pass

class Answer(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        orm_mode = True
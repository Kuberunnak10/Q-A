from pydantic import BaseModel, Field, validator
from typing import List
from datetime import datetime
from app.answers.schemas import Answer as AnswerSchema

class QuestionBase(BaseModel):
    text: str
    
    @validator('text')
    def text_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Question text cannot be empty')
        return v.strip()

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime
    answers: List[AnswerSchema] = Field(default_factory=list)

    class Config:
        from_attributes = True
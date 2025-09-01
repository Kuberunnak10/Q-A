from pydantic import BaseModel, field_validator
from typing import List
from datetime import datetime

class QuestionBase(BaseModel):
    text: str
    
    @field_validator('text')
    @classmethod
    def text_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Question text cannot be empty')
        return v.strip()

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# Schema for question with answers (used in GET /questions/{id})
class QuestionWithAnswers(Question):
    answers: List['AnswerInQuestion'] = []

    class Config:
        from_attributes = True

# Simplified answer schema for nested use
class AnswerInQuestion(BaseModel):
    id: int
    user_id: str
    text: str
    created_at: datetime

    class Config:
        from_attributes = True
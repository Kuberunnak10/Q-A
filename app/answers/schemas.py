from pydantic import BaseModel, field_validator
from datetime import datetime

class AnswerBase(BaseModel):
    text: str
    user_id: str
    
    @field_validator('text')
    @classmethod
    def text_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Answer text cannot be empty')
        return v.strip()
    
    @field_validator('user_id')
    @classmethod
    def user_id_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('User ID cannot be empty')
        return v.strip()

class AnswerCreate(AnswerBase):
    pass

class Answer(AnswerBase):
    id: int
    question_id: int
    created_at: datetime

    class Config:
        from_attributes = True
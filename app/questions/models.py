from sqlalchemy import Column, Integer, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class Question(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    answers = relationship("Answer", back_populates="question", cascade="all, delete-orphan")
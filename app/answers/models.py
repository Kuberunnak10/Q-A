from sqlalchemy import Column, Integer, Text, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String

class Answer(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"))
    user_id = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    
    question = relationship("Question", back_populates="answers")
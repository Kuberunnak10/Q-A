from app.answers.models import Answer
from app.dao.base import BaseDAO

class AnswerDAO(BaseDAO):
    model = Answer
from app.questions.models import Question
from app.dao.base import BaseDAO
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class QuestionDAO(BaseDAO):
    model = Question

    @classmethod
    async def find_with_answers(cls, db_session, question_id: int):
        async with db_session() as session:
            query = select(cls.model).options(joinedload(cls.model.answers)).filter_by(id=question_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

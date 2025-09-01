from app.questions.models import Question
from app.dao.base import BaseDAO
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession

class QuestionDAO(BaseDAO):
    model = Question

    @classmethod
    async def find_with_answers(cls, session: AsyncSession, question_id: int):
        query = select(cls.model).options(joinedload(cls.model.answers)).filter_by(id=question_id)
        result = await session.execute(query)
        return result.unique().scalar_one_or_none()

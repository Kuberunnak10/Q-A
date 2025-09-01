from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, session: AsyncSession, model_id: int):
        result = await session.execute(select(cls.model).filter_by(id=model_id))
        return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, session: AsyncSession, **filter_by):
        result = await session.execute(select(cls.model).filter_by(**filter_by))
        return result.scalars().all()

    @classmethod
    async def add(cls, session: AsyncSession, **data):
        instance = cls.model(**data)
        session.add(instance)
        await session.commit()
        await session.refresh(instance)
        return instance

    @classmethod
    async def delete(cls, session: AsyncSession, **filter_by):
        await session.execute(delete(cls.model).filter_by(**filter_by))
        await session.commit()

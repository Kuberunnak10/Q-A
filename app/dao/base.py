from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert, delete

class BaseDAO:
    model = None

    @classmethod
    async def find_by_id(cls, db_session: AsyncSession, model_id: int):
        async with db_session() as session:
            result = await session.execute(select(cls.model).filter_by(id=model_id))
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, db_session: AsyncSession, **filter_by):
        async with db_session() as session:
            result = await session.execute(select(cls.model).filter_by(**filter_by))
            return result.scalars().all()

    @classmethod
    async def add(cls, db_session: AsyncSession, **data):
        async with db_session() as session:
            result = await session.execute(insert(cls.model).values(**data).returning(cls.model.id))
            await session.commit()
            return result.scalar()

    @classmethod
    async def delete(cls, db_session: AsyncSession, **filter_by):
        async with db_session() as session:
            await session.execute(delete(cls.model).filter_by(**filter_by))
            await session.commit()

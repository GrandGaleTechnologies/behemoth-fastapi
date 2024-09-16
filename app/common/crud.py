from typing import Generic, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

T = TypeVar("T")


class CRUDBase(Generic[T]):
    """
    CRUD object with default methods to Create, Read, Update, Delete (CRUD).
    """

    def __init__(self, model: Type[T], db: AsyncSession):
        self.model = model
        self.db = db

    async def create(self, *, data: dict):
        """
        Create object
        """
        db_obj = self.model(**data)
        self.db.add(db_obj)
        await self.db.commit()
        await self.db.refresh(db_obj)

        return db_obj

    async def get(self, **kwargs):
        """
        Retrieve object
        """
        obj = await self.db.execute(select(self.model).filter_by(**kwargs))
        return obj.scalars().first()

    async def get_all(self, return_qs: bool = False):
        """
        Get all objects
        """
        qs = await self.db.execute(select(self.model))
        if return_qs:
            return qs.scalars()
        return qs.scalars().all()

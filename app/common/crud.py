# type: ignore
from typing import Generic, Type, TypeVar

from bson import ObjectId
from pydantic import BaseModel
from pymongo.collection import Collection
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Types
T = TypeVar("T")
P = TypeVar("P")


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
        qs = select(self.model)
        if return_qs:
            return qs
        result = await self.db.execute(qs)
        return result.scalars().all()


class MongoCRUDBase(Generic[P]):
    """
    CRUD base class for MongoDB using Pymongo and Pydantic
    """

    def __init__(self, model: Type(P), collection: Collection):
        self.model = model
        self.collection = collection

    def create(self, data: dict) -> P:
        """
        Insert a new document and return it as a model
        """
        result = self.collection.insert_one(data)
        doc = self.collection.find_one({"_id": result.inserted_id})
        return self.model(**doc)

    def get(self, **filters) -> P | None:
        """
        Retrieve a single document matching filters
        """
        doc = self.collection.find_one(filters)
        return self.model(**doc) if doc else None

    def update(self, id: str, data: dict) -> P | None:
        """
        Update a document by its ID
        """
        self.collection.update_one({"_id": ObjectId(id)}, {"$set": data})
        updated = self.collection.find_one({"_id": ObjectId(id)})
        return self.model(**updated) if updated else None

    def delete(self, id: str) -> bool:
        """
        Delete a document by it's ID
        """
        result = self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count == 1

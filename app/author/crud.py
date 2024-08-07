from sqlalchemy.orm import Session

from app.author import models


class AuthorCRUD:
    """
    The author crud class
    """

    def __init__(self, *, db: Session):
        """
        The crud init method
        """
        self.db = db
        self.qs = db.query(models.Author)

    async def create(self, *, data: dict):
        """
        Create a author obj
        """
        # Create model instance
        obj = models.Author(**data)

        # Save to db
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    async def get(self, **kwargs):
        """
        Retrieve author using it's ID
        """
        return self.qs.filter_by(**kwargs).first()


class BookCRUD:
    """
    The book crud class
    """

    def __init__(self, *, db: Session):
        """
        The crud init method
        """
        self.db = db
        self.qs = db.query(models.Book)

    async def create(self, *, data: dict):
        """
        Create a book obj
        """
        # Create model instance
        obj = models.Book(**data)

        # Save to db
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)

        return obj

    async def get(self, **kwargs):
        """
        Retrieve book using it's ID
        """
        return self.qs.filter_by(**kwargs).first()

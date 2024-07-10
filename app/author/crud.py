from sqlalchemy.orm import Session
from app.author import models

from app.author.schemas import create


class AuthorCRUD:
    """
    The author crud class
    """

    def __init__(self, *, session: Session):
        """
        The crud init method
        """
        self.session = session

    async def create(self, *, data: create.AuthorCreate):
        # Create model instance
        obj = models.Author(**data.model_dump())

        # Save to db
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)

        return obj

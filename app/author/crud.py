from sqlalchemy.ext.asyncio import AsyncSession

from app.author import models
from app.common.crud import CRUDBase


class AuthorCRUD(CRUDBase[models.Author]):
    """
    The author crud class
    """

    def __init__(self, db: AsyncSession):
        super().__init__(model=models.Author, db=db)


class BookCRUD(CRUDBase[models.Book]):
    """
    The book crud class
    """

    def __init__(self, db: AsyncSession):
        super().__init__(models.Book, db)

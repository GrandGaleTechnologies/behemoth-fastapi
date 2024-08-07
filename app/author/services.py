from sqlalchemy.orm import Session
from app.author import models
from app.author.crud import AuthorCRUD, BookCRUD

from app.author.schemas import create


async def create_author(*, data: create.AuthorCreate, db: Session):
    """
    Create Author obj

    Args:
        data (create.AuthorCreate): The author's details
        db (Session): The database session

    Returns:
        models.Author
    """
    # Init author crud
    author_crud = AuthorCRUD(db=db)

    # Create author
    author = await author_crud.create(data=data.model_dump())

    return author


async def create_book(author: models.Author, data: create.BookCreate, db: Session):
    """
    Create Book obj

    Args:
        author (models.Author): The book's author
        data (create.BookCreate): The book's details
        db (Session): The database session

    Returns:
        models.Book
    """

    # Init CRUD
    book_crud = BookCRUD(db=db)

    # Create book
    data_dict = data.model_dump()
    data_dict["author_id"] = author.id

    book = await book_crud.create(data=data_dict)

    return book

from fastapi import APIRouter, status

from app.author import selectors, services
from app.author.formatters import format_author, format_book
from app.author.schemas import create, response
from app.common.annotations import DatabaseSession

router = APIRouter()


@router.post(
    "",
    summary="Create Author",
    response_description="The created author's details",
    status_code=status.HTTP_201_CREATED,
    response_model=response.AuthorResponse,
)
async def author_create(author_in: create.AuthorCreate, db: DatabaseSession):
    """
    This endpoint creates an author
    """

    author = await services.create_author(data=author_in, db=db)

    return {"data": await format_author(author=author)}


@router.post(
    "/{author_id}/book",
    summary="Create a book",
    response_description="The created book's details",
    status_code=status.HTTP_201_CREATED,
    response_model=response.BookResponse,
)
async def book_create(author_id: int, book_in: create.BookCreate, db: DatabaseSession):
    """
    This endpoint creates a book
    """

    # Get author
    author = await selectors.get_author_by_id(id=author_id, db=db)

    # Create book
    book = await services.create_book(author=author, data=book_in, db=db)

    return {"data": await format_book(book=book)}

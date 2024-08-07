from pydantic import Field

from app.author.schemas.base import Author, Book
from app.common.schemas import ResponseSchema


class AuthorResponse(ResponseSchema):
    """
    The base author's response model
    """

    data: Author = Field(description="The author's details")


class BookResponse(ResponseSchema):
    """
    The base book response model
    """

    data: Book = Field(description="The book's details")

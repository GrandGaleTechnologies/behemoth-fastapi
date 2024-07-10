from pydantic import Field

from app.author.schemas.base import Author
from app.common.schemas import ResponseSchema


class AuthorResponse(ResponseSchema):
    """
    The base author's response model
    """

    data: Author = Field(description="The author's details")

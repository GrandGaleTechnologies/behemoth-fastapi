from datetime import datetime
from pydantic import BaseModel, Field


class Author(BaseModel):
    """
    The base schema for authors
    """

    id: int = Field(description="The ID of the author")
    full_name: str = Field(description="The name of the author")
    created_at: datetime = Field(description="The time the author was created")


class Book(BaseModel):
    """
    The base schema for books
    """

    id: int = Field(description="The ID of the book")
    author: Author = Field(description="The author's details")
    name: str = Field(description="The name of the book")
    created_at: datetime = Field(description="The time the book was created")

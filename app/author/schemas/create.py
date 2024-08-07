from pydantic import BaseModel, Field


class AuthorCreate(BaseModel):
    """
    The schema for creating authors
    """

    full_name: str = Field(description="The name of the author", max_length=250)


class BookCreate(BaseModel):
    """
    The schema for creating books
    """

    name: str = Field(description="The name of the book", max_length=145)

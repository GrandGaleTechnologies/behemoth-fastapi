from pydantic import BaseModel, Field


class AuthorCreate(BaseModel):
    """
    The schema for creating authors
    """

    full_name: str = Field(description="The name of the author")

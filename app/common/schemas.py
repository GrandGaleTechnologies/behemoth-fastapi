from typing import Any

from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    """This is the generic base response schema"""
    message: str = Field(description="The response message", default="success")
    data: Any = Field(description="The response data")

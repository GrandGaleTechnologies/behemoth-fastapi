from functools import lru_cache

from pydantic import BaseModel


class RouteTags(BaseModel):
    """
    Base model for app route tags
    """

    # Module Tags
    AUTHOR: str = "Author APIs"
    BOOK: str = "Book APIs"


@lru_cache
def get_tags():
    """
    Get app rotue tags
    """
    return RouteTags()

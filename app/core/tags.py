from functools import lru_cache

from pydantic import BaseModel


class RouteTags(BaseModel):
    """
    Base model for app route tags
    """

    # Module Tags
    SAMPLE: str = "Sample APIs"


@lru_cache
def get_tags():
    """
    Get app rotue tags
    """
    return RouteTags()

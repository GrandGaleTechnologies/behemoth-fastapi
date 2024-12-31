from typing import Literal

from app.common.types import PaginationParamsType
from app.core.database import AsyncSessionLocal


async def get_session():
    """
    Start a db session
    """
    async with AsyncSessionLocal() as session:  # type: ignore
        yield session


def pagination_params(
    q: str | None = None,
    page: int = 1,
    size: int = 10,
    order_by: Literal["asc", "desc"] = "desc",
):
    """
    Helper Dependency for pagination
    """
    return PaginationParamsType(q=q, page=page, size=size, order_by=order_by)

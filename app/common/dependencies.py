from typing import Literal

import redis.asyncio as redis

from app.common.types import PaginationParamsType
from app.core.database import AsyncSessionLocal
from app.core.settings import get_settings

settings = get_settings()


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


def get_redis_client():
    """
    Helper dependency for redis
    """
    return redis.from_url(
        settings.REDIS_BROKER_URL, encoding="utf-8", decode_responses=True
    )

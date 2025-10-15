import hashlib
import json
from typing import Any, Generic, Type, TypeVar

from fastapi.encoders import jsonable_encoder
from logfire import info, instrument

from app.common.dependencies import get_redis_client

# Type vars
T = TypeVar("T")


def generate_cache_key(data: dict, prefix: str) -> str:
    """
    Generate a deterministic Redis cache key based on a data dict.
    Handles non-JSON-serializable types like datetime.date, Decimal, etc.
    """

    json_str = json.dumps(jsonable_encoder(data), sort_keys=True)
    cache_hash = hashlib.sha256(json_str.encode()).hexdigest()
    cache_key = f"{prefix}{cache_hash}"
    return cache_key


class CacheManager(Generic[T]):
    """
    Generic cache manager for Redis-backed caching.
    """

    def __init__(
        self,
        ttl: int,
        cache_prefix: str,
        data: dict,
        model_class: Type[T] | None = None,
    ):
        """
        Initialize the cache manager.

        Args:
            ttl: Time-to-live for cached items in seconds
            model_class: (optional) Pydantic or dataclass type for decoding cached data
            cache_prefix: The cache prefix
            data: Dictionary containing the data to generate cache key from
        """
        self.redis_client = get_redis_client()
        self.ttl = ttl
        self.model_class = model_class
        self.cache_prefix = cache_prefix
        self.data = data

    @instrument("Get cached data from Redis")
    async def get(self) -> T | None:
        """
        Get cached data from Redis.

        Returns:
            Cached data if found, None otherwise
        """
        cache_key = generate_cache_key(self.data, self.cache_prefix)
        info(f"Looking for cache key: {cache_key}")

        cached_data = await self.redis_client.get(cache_key)
        if not cached_data:
            info(f"Cache miss for key: {cache_key}")
            return None

        info(f"Cache hit for key: {cache_key}")
        data = json.loads(cached_data)

        # If model_class is provided, parse into that model
        if self.model_class:
            return self.model_class(**data)

        return data  # type: ignore

    @instrument("Set cached data in Redis")
    async def set(
        self,
        value: Any,
    ):
        """
        Cache data in Redis.

        Args:
            value: The value to cache (will be JSON-encoded)
        """
        cache_key = generate_cache_key(self.data, self.cache_prefix)
        info(f"Setting cache key: {cache_key}")

        encoded_data = json.dumps(jsonable_encoder(value))

        await self.redis_client.setex(cache_key, self.ttl, encoded_data)

        info(f"Cache key {cache_key} set with TTL {self.ttl}")

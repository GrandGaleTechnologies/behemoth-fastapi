from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field  # ✅ import Field separately

class Settings(BaseSettings):
    """The settings for the application."""

    model_config = SettingsConfigDict(env_file=".env")

    # App
    DEBUG: bool = Field(default=True)

    # Logfire
    LOGFIRE_TOKEN: str | None = None

    # DB Settings
    POSTGRES_DATABASE_URL: str = Field(
        default="sqlite+aiosqlite:///./app.db", env="POSTGRES_DATABASE_URL"
    )

    SYNC_DATABASE_URL: str = Field(
        default="sqlite:///./app.db", env="SYNC_DATABASE_URL"
    )

    # REDIS
    REDIS_BROKER_URL: str | None = Field(default=None, env="REDIS_BROKER_URL")

@lru_cache
def get_settings() -> Settings:
    """Cached settings instance"""
    return Settings()

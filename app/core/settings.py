import os
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """The settings for the application."""

    model_config = SettingsConfigDict(env_file=".env")

    # App
    DEBUG: bool = os.environ.get("DEBUG")  # type: ignore

    # DB Settings
    POSTGRES_DATABASE_URL: str = os.environ.get("POSTGRES_DATABASE_URL")  # type: ignore


@lru_cache
def get_settings():
    """This function returns the settings obj for the application."""
    return Settings()

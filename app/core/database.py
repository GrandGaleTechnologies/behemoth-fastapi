from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.settings import get_settings

settings = get_settings()

# Async DB URL for FastAPI runtime
ASYNC_DATABASE_URL = settings.POSTGRES_DATABASE_URL

# Sync DB URL for Alembic migrations
SYNC_DATABASE_URL = settings.SYNC_DATABASE_URL or "sqlite:///./app.db"

# Engines
async_engine = create_async_engine(ASYNC_DATABASE_URL, future=True, echo=settings.DEBUG)
sync_engine = create_engine(SYNC_DATABASE_URL, future=True)

# Session factories
AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
    expire_on_commit=False,
)

SyncSessionLocal = sessionmaker(
    bind=sync_engine,
    autocommit=False,
    autoflush=False,
)

# Base model
Base = declarative_base()


# Dependency for FastAPI (async sessions)
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

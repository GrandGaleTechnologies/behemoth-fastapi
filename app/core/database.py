from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.core.settings import get_settings

settings = get_settings()

engine = create_async_engine(
    url=settings.POSTGRES_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=100,  # The size of the connection pool
    max_overflow=50,  # The maximum number of connections that can be opened beyond the pool size. Set to -1 for no limit.
)


# Add this function to initialize the pools
async def initialize_connection_pools():
    """Pre-warm the connection pools by creating initial connections"""
    async with engine.connect() as conn:
        # Create initial connections up to pool_size
        await conn.execute(text("SELECT 1"))
        await conn.commit()


AsyncSessionLocal = sessionmaker(  # type: ignore
    bind=engine,  # type: ignore
    class_=AsyncSession,
    expire_on_commit=False,
)

DBBase = declarative_base()

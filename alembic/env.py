from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from app.core.database import Base
from app.models import user  # ensure Alembic sees all models
from app.core.settings import get_settings

# Load settings
settings = get_settings()

# Alembic Config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata for autogenerate support
target_metadata = Base.metadata

# Use Postgres if available, else fallback to local SQLite
DB_URL = settings.SYNC_DATABASE_URL

def run_migrations_offline() -> None:
    """Run migrations in offline mode"""
    context.configure(
        url=DB_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in online mode"""
    connect_args = {"check_same_thread": False} if "sqlite" in DB_URL else {}
    connectable = create_engine(DB_URL, poolclass=pool.NullPool, connect_args=connect_args)
    
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

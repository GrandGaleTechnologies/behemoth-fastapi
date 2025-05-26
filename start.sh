#!/bin/bash
set -e

# Run Alembic migrations
uv run -- alembic upgrade head

uv run -- fastapi run --port $PORT

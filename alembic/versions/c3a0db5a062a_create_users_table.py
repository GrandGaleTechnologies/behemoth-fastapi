"""create users table

Revision ID: c3a0db5a062a
Revises: 
Create Date: 2025-09-03 00:26:09.298517
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "c3a0db5a062a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create the users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("username", sa.String, nullable=False, unique=True, index=True),
        sa.Column("email", sa.String, nullable=False, unique=True, index=True),
        sa.Column("password_hash", sa.String, nullable=False),
        sa.Column("role", sa.String, nullable=False, server_default="user"),
    )


def downgrade() -> None:
    # Drop the users table
    op.drop_table("users")


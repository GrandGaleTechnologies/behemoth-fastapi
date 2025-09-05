"""add role column to users

Revision ID: 98d97bd4d6a9
Revises: c3a0db5a062a
Create Date: 2025-09-04 15:38:18.499631
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98d97bd4d6a9'
down_revision: Union[str, None] = 'c3a0db5a062a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "users",
        sa.Column("role", sa.String(), nullable=False, server_default="user")
    )


def downgrade() -> None:
    op.drop_column("users", "role")

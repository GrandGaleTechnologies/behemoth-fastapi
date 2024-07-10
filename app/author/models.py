from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from app.core.database import DBBase


class Author(DBBase):
    """
    The database model for authors
    """

    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)


class Book(DBBase):
    """
    The database model for books
    """

    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(
        Integer, ForeignKey("authors.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now, nullable=False)

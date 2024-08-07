from app.author import models


async def format_author(*, author: models.Author):
    """
    Formats author obj to dict
    """
    return {
        "id": author.id,
        "full_name": author.full_name,
        "created_at": author.created_at,
    }


async def format_book(*, book: models.Book):
    """
    Format book obj to dict
    """
    return {
        "id": book.id,
        "name": book.name,
        "author": await format_author(author=book.author),
        "created_at": book.created_at,
    }

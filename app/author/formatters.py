from app.author import models


async def format_author(*, author: models.Author):
    """
    This function formats an author obj
    """
    return {
        "id": author.id,
        "full_name": author.full_name,
        "created_at": author.created_at,
    }

from sqlalchemy.ext.asyncio import AsyncSession

from app.author.crud import AuthorCRUD
from app.author.exceptions import AuthorNotFound


# pylint: disable=redefined-builtin
async def get_author_by_id(*, id: int, db: AsyncSession, raise_exc: bool = True):
    """
    Get author using their ID

    Args:
        id (int): THe ID of the author
        db (Session): The database session
        raise_exception (bool = True): Raise a 404 if not found

    Raises:
        NotFound: Author not found

    Returns:
        models.Author | None
    """

    # Init CRUD
    author_crud = AuthorCRUD(db=db)

    # Get obj
    obj = await author_crud.get(id=id)

    # Check obj
    if not obj and raise_exc:
        raise AuthorNotFound()

    return obj

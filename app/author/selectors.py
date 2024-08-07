from sqlalchemy.orm import Session

from app.author.crud import AuthorCRUD
from app.common.exceptions import NotFound


async def get_author_by_id(*, id: int, db: Session, raise_exception: bool = True):
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
    if not obj and raise_exception:
        raise NotFound(msg="Author not found")

    return obj

from sqlalchemy.orm import Session
from app.author.crud import AuthorCRUD

from app.author.schemas import create


async def create_author(data: create.AuthorCreate, session: Session):
    # Init author crud
    author_crud = AuthorCRUD(session=session)

    # Create author
    author = await author_crud.create(data=data)

    return author

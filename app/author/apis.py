from fastapi import APIRouter, status
from app.author import services
from app.author.formatters import format_author

from app.author.schemas import create, response
from app.common.annotations import DatabaseSession

router = APIRouter()


@router.post(
    "",
    summary="Create Author",
    response_description="The created author's details",
    status_code=status.HTTP_201_CREATED,
    response_model=response.AuthorResponse,
)
async def author_create(author_in: create.AuthorCreate, session: DatabaseSession):
    """
    This endpoint creates an author in the database
    """

    author = await services.create_author(data=author_in, session=session)

    return {"data": await format_author(author=author)}

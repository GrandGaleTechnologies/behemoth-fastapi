from fastapi import APIRouter, status

from app.author.schemas import response

router = APIRouter()

@router.post(
    "",
    summary="Create Author",
    response_description="The created author's details",
    status_code=status.HTTP_201_CREATED,
    response_model=response.AuthorResponse
)
async def author_create():
    """
    This endpoint creates an author in the database
    """

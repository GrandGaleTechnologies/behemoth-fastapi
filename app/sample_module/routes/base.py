from fastapi import APIRouter

from app.common.schemas import ResponseSchema

# Globals
router = APIRouter()


@router.get(
    "",
    summary="Sample API Endpoint",
    response_description="Some json response",
    status_code=200,
    response_model=ResponseSchema,
)
async def route_sample_get():
    """
    This endpoint is a sample endpoint for the behemoth
    """

    return {
        "msg": "Lowkey on God",
        "data": {
            "website": "https://grandgale.tech",
            "email": "contact@grandgale.tech",
            "phone": "+2349066122515",
        },
    }

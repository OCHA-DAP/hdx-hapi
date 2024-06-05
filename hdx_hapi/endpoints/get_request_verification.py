from fastapi import APIRouter

router = APIRouter(
    tags=['Nginx'],
)


@router.get(
    '/api/util/verify-request',
    response_model=None,
    include_in_schema=False,
)
@router.get(
    '/api/v1/util/verify-request',
    response_model=None,
    include_in_schema=False,
)
async def get_request_verification():
    return None

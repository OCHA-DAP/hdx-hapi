import logging

from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from hdx_hapi.endpoints.util.exceptions import RequestParamsValidationError


logger = logging.getLogger(__name__)


async def request_validation_error_handler(request: Request, exc: RequestParamsValidationError) -> JSONResponse:
    error_message = str(exc)
    logger.warning(f'Following request params validation error happened on url {request.url}: {error_message}')

    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({'error': error_message}),
    )

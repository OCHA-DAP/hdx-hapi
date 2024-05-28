import logging

from fastapi import Request, status
from fastapi.exceptions import ResponseValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)


async def response_validation_error_handler(request: Request, exc: ResponseValidationError) -> JSONResponse:
    errors = exc.errors()
    err_num = len(errors) if errors else 0
    error_message = 'Internal Server Error. Response data is invalid.'
    logger.error(f'{error_message}. There were {err_num} errors. Request url was {request.url}.')
    if err_num > 0:
        error_message += (
            f' There were {err_num} errors. A couple of errors will be shown in the "error_sample_list" field.'
        )
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder({'error_sample_list': errors[:5], 'error': error_message}),
    )

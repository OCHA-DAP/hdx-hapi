from fastapi import Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

from hdx_hapi.config.config import get_config
from hdx_hapi.endpoints.util.util import app_name_identifier_query, email_identifier_query

import base64
import logging


logger = logging.getLogger(__name__)

CONFIG = get_config()


ALLOWED_API_ENDPOINTS = {
    '/api/v1/encode_app_identifier',
    '/api/encode_app_identifier',
}


# I've tried using the Pydantic model directly in the get_encoded_identifier endpoint, but then the generated OpenAPI
# specs don't include all the details anymore
class IdentifierParams(BaseModel):
    application: str = app_name_identifier_query
    email: EmailStr = email_identifier_query


async def app_identifier_middleware(request: Request, call_next):
    """
    Middleware to check for the app_identifier in the request and add it to the request state
    """
    if (
        CONFIG.HAPI_IDENTIFIER_FILTERING
        and request.url.path.startswith('/api')
        and request.url.path not in ALLOWED_API_ENDPOINTS
    ):
        app_identifier = request.query_params.get('app_identifier')
        authorization = request.headers.get('X-HDX-HAPI-APP-IDENTIFIER')
        encoded_value = app_identifier or authorization

        if not encoded_value:
            return JSONResponse(
                content={'error': 'Missing app identifier'}, status_code=status.HTTP_400_BAD_REQUEST
            )

        try:
            decoded_value = base64.b64decode(encoded_value).decode('utf-8')
            application, email = decoded_value.split(':')
            identifier_params = IdentifierParams(application=application, email=email)
            logger.warning(f'Application: {application}, Email: {email}')
            # Adding the app_name to the request state so it can be accessed in the endpoint
            request.state.app_name = identifier_params.application
        except Exception:
            return JSONResponse(
                content={'error': 'Invalid app identifier'}, status_code=status.HTTP_400_BAD_REQUEST
            )

    response = await call_next(request)
    return response

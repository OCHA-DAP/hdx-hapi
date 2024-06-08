from typing import Optional, Tuple
from fastapi import Request, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr

from hdx_hapi.config.config import get_config
from hdx_hapi.endpoints.util.util import app_name_identifier_query, email_identifier_query
from hdx_hapi.endpoints.middleware.util.util import extract_path_identifier_and_query_params

import base64
import logging


logger = logging.getLogger(__name__)

CONFIG = get_config()


ALLOWED_API_ENDPOINTS = {
    '/api/v1/encode_app_identifier',
    '/api/encode_app_identifier',
    '/api/v1/util/version',
    '/api/util/version',
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
    if CONFIG.HAPI_IDENTIFIER_FILTERING:
        header_identifier = request.headers.get('X-HDX-HAPI-APP-IDENTIFIER')

        is_nginx_verify_request = request.url.path.startswith(
            '/api/v1/util/verify-request'
        ) or request.url.path.startswith('/api/util/verify-request')
        request.state.is_nginx_verify_request = is_nginx_verify_request
        original_uri_from_nginx = request.headers.get('X-Original-URI')

        if is_nginx_verify_request:
            if not original_uri_from_nginx:
                return JSONResponse(content={'error': 'Missing X-Original-URI'}, status_code=status.HTTP_403_FORBIDDEN)
            path, app_identifier, _ = extract_path_identifier_and_query_params(original_uri_from_nginx)
        else:
            path = request.url.path
            app_identifier = request.query_params.get('app_identifier')

        status_code, error_message, identifier_params = _check_allow_request(path, app_identifier or header_identifier)

        if status_code == status.HTTP_200_OK:
            request.state.app_name = identifier_params.application if identifier_params else None
        else:
            return JSONResponse(content={'error': error_message}, status_code=status_code)

    response = await call_next(request)
    return response


def _check_allow_request(
    request_path: str, encoded_app_identifier: Optional[str]
) -> Tuple[int, Optional[str], Optional[IdentifierParams]]:
    """
    Check if the request is allowed.
    Args:
        request_path: The path of the request
        encoded_app_identifier: The app_identifier
    Returns:
        Tuple of status code, error message and IdentifierParams
    """
    if request_path and request_path.startswith('/api') and request_path not in ALLOWED_API_ENDPOINTS:
        if not encoded_app_identifier:
            return status.HTTP_403_FORBIDDEN, 'Missing app identifier', None

        try:
            decoded_value = base64.b64decode(encoded_app_identifier).decode('utf-8')
            application, email = decoded_value.split(':')
            identifier_params = IdentifierParams(application=application, email=email)
            logger.warning(f'Application: {application}, Email: {email}')

            return status.HTTP_200_OK, None, identifier_params

        except Exception:
            return status.HTTP_403_FORBIDDEN, 'Invalid app identifier', None

    return status.HTTP_200_OK, None, None

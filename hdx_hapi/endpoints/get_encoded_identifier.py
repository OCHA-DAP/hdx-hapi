import base64
from typing import Annotated
from fastapi import APIRouter
from pydantic import EmailStr

from hdx_hapi.endpoints.models.encoded_identifier import IdentifierResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.util.util import app_name_identifier_query, email_identifier_query

router = APIRouter(
    tags=['Generate App Identifier'],
)


SUMMARY_TEXT = 'Get an app identifier by encoding an application name and email'

ROUTER_DICT = {
    'response_model': IdentifierResponse,
    'summary': SUMMARY_TEXT,
    'responses': ERROR_RESPONSES,
}


@router.get('/api/encode_app_identifier', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v1/encode_app_identifier', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v2/encode_app_identifier', **ROUTER_DICT)
async def get_encoded_identifier(
    application: Annotated[str, app_name_identifier_query],
    email: Annotated[EmailStr, email_identifier_query],
):
    """
    Encode an application name and email address in base64 to serve as an client identifier in HDX HAPI calls.
    """
    encoded_identifier = base64.b64encode(bytes(f'{application}:{email}', 'utf-8'))

    result = {'encoded_app_identifier': encoded_identifier.decode('utf-8')}
    return result

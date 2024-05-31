import base64
from typing import Annotated
from fastapi import APIRouter
from pydantic import EmailStr

from hdx_hapi.endpoints.models.encoded_identifier import IdentifierResponse
from hdx_hapi.endpoints.util.util import app_name_identifier_query, email_identifier_query

router = APIRouter(
    tags=['Generate App Identifier'],
)

SUMMARY = 'Get an app identifier by encoding an application name and email'


@router.get(
    '/api/encode_app_identifier',
    response_model=IdentifierResponse,
    summary=SUMMARY,
    include_in_schema=False,
)
@router.get(
    '/api/v1/encode_app_identifier',
    response_model=IdentifierResponse,
    summary=SUMMARY,
)
async def get_encoded_identifier(
    application: Annotated[str, app_name_identifier_query],
    email: Annotated[EmailStr, email_identifier_query],
):
    """
    Encode an application name and email address in base64 to serve as an client identifier in HDX HAPI calls
    """
    encoded_identifier = base64.b64encode(bytes(f'{application}:{email}', 'utf-8'))

    result = {'encoded_app_identifier': encoded_identifier.decode('utf-8')}
    return result

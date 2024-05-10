import base64
from typing import Annotated
from fastapi import APIRouter, Query
from pydantic import EmailStr

from hdx_hapi.endpoints.models.encoded_identifier import IdentifierResponse

router = APIRouter(
    tags=['Utility'],
)

SUMMARY = 'Get an encoded application name plus email'


@router.get(
    '/api/encode_identifier',
    response_model=IdentifierResponse,
    summary=SUMMARY,
    include_in_schema=False,
)
@router.get(
    '/api/v1/encode_identifier',
    response_model=IdentifierResponse,
    summary=SUMMARY,
)
async def get_encoded_identifier(
    application: Annotated[str, Query(max_length=512, description='A name for the calling application')],
    email: Annotated[EmailStr, Query(max_length=512, description='An email address')],
):
    """
    Encode an application name and email address in base64 to serve as an client identifier in HAPI calls
    """
    encoded_identifier = base64.b64encode(bytes(f'{application}:{email}', 'utf-8'))

    result = {'encoded_identifier': encoded_identifier.decode('utf-8')}
    return result
    # return transform_result_to_csv_stream_if_requested(result, OutputFormat.JSON, IdentifierResponse)

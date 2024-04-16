from typing import Annotated
from fastapi import APIRouter, Depends, Query
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested

from hdx_hapi.endpoints.models.encoded_identifier import IdentifierResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters

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
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    application: Annotated[str, Query(max_length=512, description='A name for the calling application')] = None,
    email: Annotated[str, Query(max_length=512, description='An email address')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Get information about the <a href="https://data.humdata.org/dataset">HDX Datasets</a> that are used as data sources
    for HAPI. Datasets contain one or more resources, which are the sources of the data found in HAPI.
    """
    result = {'encoded_identifier': f'{application}:{email}'}
    return transform_result_to_csv_stream_if_requested(result, output_format, IdentifierResponse)

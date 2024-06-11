from typing import Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import DOC_CURRENCY_CODE

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.currency import CurrencyResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested

from hdx_hapi.services.currency_logic import get_currencies_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Metadata'],
)


@router.get(
    '/api/metadata/currency',
    response_model=HapiGenericResponse[CurrencyResponse],
    summary='Get information about how currencies are classified',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/currency',
    response_model=HapiGenericResponse[CurrencyResponse],
    summary='Get information about how currencies are classified',
)
async def get_currencies(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[
        str, Query(max_length=32, description=f'{DOC_CURRENCY_CODE}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Provide currency information to use in conjunction with the food-prices endpoint
    """
    result = await get_currencies_srv(
        pagination_parameters=common_parameters,
        db=db,
        code=code,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, CurrencyResponse)

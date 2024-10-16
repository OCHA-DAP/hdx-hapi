import datetime
from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_NAME,
    DOC_LOCATION_CODE,
    DOC_SEE_LOC,
    DOC_ADMIN1_NAME,
    DOC_ADMIN1_CODE,
    DOC_SEE_ADMIN1,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_SEE_ADMIN2,
    DOC_UPDATE_DATE_MIN,
    DOC_UPDATE_DATE_MAX,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.availability import AvailabilityResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested

from hdx_hapi.services.availability_logic import get_availability_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Metadata'],
)


@router.get(
    '/api/metadata/data-availability',
    response_model=HapiGenericResponse[AvailabilityResponse],
    summary='Get information about the availability of data for different geographic admin levels',
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/data-availability',
    response_model=HapiGenericResponse[AvailabilityResponse],
    summary='Get information about the availability of data for different geographic admin levels',
)
async def get_data_availability(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    category: Annotated[
        Optional[str], Query(max_length=128, description='Filter the response by a data category')
    ] = None,
    subcategory: Annotated[
        Optional[str], Query(max_length=128, description='Filter the response by a data subcategory')
    ] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    admin1_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')
    ] = None,
    admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')
    ] = None,
    admin2_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')
    ] = None,
    admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')
    ] = None,
    hapi_updated_date_min: Annotated[
        Optional[datetime.datetime | datetime.date],
        Query(description=f'{DOC_UPDATE_DATE_MIN}'),
    ] = None,
    hapi_updated_date_max: Annotated[
        Optional[datetime.datetime | datetime.date],
        Query(description=f'{DOC_UPDATE_DATE_MAX}'),
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Provide currency information to use in conjunction with the food-prices endpoint
    """
    result = await get_availability_srv(
        pagination_parameters=common_parameters,
        db=db,
        category=category,
        subcategory=subcategory,
        location_name=location_name,
        location_code=location_code,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, AvailabilityResponse)

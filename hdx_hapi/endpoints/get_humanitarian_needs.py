from datetime import date
from typing import Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_GENDER,
    DOC_AGE_RANGE,
    DOC_SECTOR_CODE,
    DOC_SECTOR_NAME,
    DOC_HDX_PROVIDER_STUB,
    DOC_ADMIN1_CODE,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_LOC,
    DOC_UPDATE_DATE_MAX,
    DOC_UPDATE_DATE_MIN,
    DOC_SEE_ADMIN2,
    DOC_HAPI_UPDATED_DATE_MIN,
    DOC_HAPI_UPDATED_DATE_MAX,
    DOC_HAPI_REPLACED_DATE_MIN,
    DOC_HAPI_REPLACED_DATE_MAX,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.humanitarian_needs import HumanitarianNeedsResponse
from hdx_hapi.endpoints.util.util import AdminLevel, CommonEndpointParams, OutputFormat, common_endpoint_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.humanitarian_needs_logic import get_humanitarian_needs_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Humanitarian Needs'],
)


@router.get(
    '/api/affected-people/humanitarian-needs',
    response_model=HapiGenericResponse[HumanitarianNeedsResponse],
    summary='Get humanitarian needs data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/affected-people/humanitarian-needs',
    response_model=HapiGenericResponse[HumanitarianNeedsResponse],
    summary='Get humanitarian needs data',
)
async def get_humanitarian_needs(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    admin2_ref: Annotated[int, Query(description='Admin2 reference')] = None,
    gender: Annotated[str, Query(max_length=1, description=f'{DOC_GENDER}')] = None,
    age_range: Annotated[str, Query(max_length=32, description=f'{DOC_AGE_RANGE}')] = None,
    min_age: Annotated[int, Query(description='Min age')] = None,
    max_age: Annotated[int, Query(description='Max age')] = None,
    disabled_marker: Annotated[bool, Query(description='Disabled marker')] = None,
    sector_code: Annotated[str, Query(max_length=32, description=f'{DOC_SECTOR_CODE}')] = None,
    population_group: Annotated[str, Query(max_length=32, description='Population group')] = None,
    population_status: Annotated[str, Query(max_length=32, description='Population status')] = None,
    population: Annotated[int, Query(description='Population')] = None,
    reference_period_start: Annotated[
        NaiveDatetime | date,
        Query(description='Reference period start', openapi_examples={'2020-01-01': {'value': '2020-01-01'}}),
    ] = None,
    reference_period_end: Annotated[
        NaiveDatetime | date,
        Query(description='Reference period end', openapi_examples={'2024-12-31': {'value': '2024-12-31'}}),
    ] = None,
    sector_name: Annotated[str, Query(max_length=512, description=f'{DOC_SECTOR_NAME}')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    location_ref: Annotated[int, Query(description='Location reference')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')] = None,
    admin1_ref: Annotated[int, Query(description='Admin1 reference')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of humanitarian needs data
    """
    result = await get_humanitarian_needs_srv(
        pagination_parameters=common_parameters,
        db=db,
        admin2_ref=admin2_ref,
        gender=gender,
        age_range=age_range,
        min_age=min_age,
        max_age=max_age,
        disabled_marker=disabled_marker,
        sector_code=sector_code,
        population_group=population_group,
        population_status=population_status,
        population=population,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
        sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
        location_ref=location_ref,
        admin1_code=admin1_code,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin1_ref=admin1_ref,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, HumanitarianNeedsResponse)

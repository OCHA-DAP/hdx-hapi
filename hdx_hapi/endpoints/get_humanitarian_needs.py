from datetime import date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_GENDER_CODE,
    DOC_AGE_RANGE_CODE,
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

from hdx_hapi.endpoints.models.humanitarian_needs import HumanitarianNeedsResponse
from hdx_hapi.endpoints.util.util import AdminLevel, OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.humanitarian_needs_logic import get_humanitarian_needs_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Humanitarian Needs'],
)


@router.get(
    '/api/themes/humanitarian_needs',
    response_model=List[HumanitarianNeedsResponse],
    summary='Get humanitarian needs data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/themes/humanitarian_needs',
    response_model=List[HumanitarianNeedsResponse],
    summary='Get humanitarian needs data',
)
async def get_humanitarian_needs(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    gender_code: Annotated[str, Query(max_length=1, description=f'{DOC_GENDER_CODE}')] = None,
    age_range_code: Annotated[str, Query(max_length=32, description=f'{DOC_AGE_RANGE_CODE}')] = None,
    disabled_marker: Annotated[bool, Query(description='Disabled marker')] = None,
    sector_code: Annotated[str, Query(max_length=32, description=f'{DOC_SECTOR_CODE}')] = None,
    sector_name: Annotated[str, Query(max_length=512, description=f'{DOC_SECTOR_NAME}')] = None,
    population_group_code: Annotated[str, Query(max_length=32, description='Population group code')] = None,
    population_status_code: Annotated[str, Query(max_length=32, description='Population status code')] = None,
    population: Annotated[int, Query(description='Population')] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_PROVIDER_STUB}')] = None,
    resource_update_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MIN}', openapi_examples={'2020-01-01': {'value': '2020-01-01'}}),
    ] = None,
    resource_update_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MAX}', openapi_examples={'2024-12-31': {'value': '2024-12-31'}}),
    ] = None,
    hapi_updated_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_UPDATED_DATE_MIN}'),
    ] = None,
    hapi_updated_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_UPDATED_DATE_MAX}'),
    ] = None,
    hapi_replaced_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_REPLACED_DATE_MIN}'),
    ] = None,
    hapi_replaced_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_REPLACED_DATE_MAX}'),
    ] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    location_ref: Annotated[int, Query(description='Location reference')] = None,
    # admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
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
        pagination_parameters=pagination_parameters,
        db=db,
        gender_code=gender_code,
        age_range_code=age_range_code,
        disabled_marker=disabled_marker,
        sector_code=sector_code,
        sector_name=sector_name,
        population_group_code=population_group_code,
        population_status_code=population_status_code,
        population=population,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
        hapi_replaced_date_min=hapi_replaced_date_min,
        hapi_replaced_date_max=hapi_replaced_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        # admin1_name=admin1_name,
        location_ref=location_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin1_ref=admin1_ref,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, HumanitarianNeedsResponse)

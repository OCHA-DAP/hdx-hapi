from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter
# from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_GENDER,
    DOC_AGE_RANGE,
    DOC_SECTOR_CODE,
    DOC_SECTOR_NAME,
    DOC_ADMIN1_CODE,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_LOC,
    DOC_SEE_ADMIN2,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.humanitarian_needs import HumanitarianNeedsResponse
from hdx_hapi.endpoints.models.refugees import RefugeesResponse
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.humanitarian_needs_logic import get_humanitarian_needs_srv
from hdx_hapi.services.refugees_logic import get_refugees_srv
from hdx_hapi.services.sql_alchemy_session import get_db
from hapi_schema.utils.enums import DisabledMarker, Gender, PopulationGroup, PopulationStatus
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
    AdminLevel,
)

router = APIRouter(
    tags=['Affected people'],
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
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    admin2_ref: Annotated[Optional[int], Query(description='Admin2 reference')] = None,
    gender: Annotated[Optional[Gender], Query(max_length=3, description=f'{DOC_GENDER}')] = None,
    age_range: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_AGE_RANGE}')] = None,
    disabled_marker: Annotated[Optional[DisabledMarker], Query(description='Disabled marker')] = None,
    sector_code: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_SECTOR_CODE}')] = None,
    population_group: Annotated[Optional[PopulationGroup], Query(max_length=32, description='Population group')] = None,
    population_status: Annotated[
        Optional[PopulationStatus], Query(max_length=32, description='Population status')
    ] = None,
    population_min: Annotated[int, Query(description='Population, minimum value for filter')] = None,
    population_max: Annotated[int, Query(description='Population, maximum value for filter')] = None,
    # reference_period_start: Annotated[
    #     NaiveDatetime | date,
    #     Query(description='Reference period start', openapi_examples={'2020-01-01': {'value': '2020-01-01'}}),
    # ] = None,
    # reference_period_end: Annotated[
    #     NaiveDatetime | date,
    #     Query(description='Reference period end', openapi_examples={'2024-12-31': {'value': '2024-12-31'}}),
    # ] = None,
    sector_name: Annotated[Optional[str], Query(max_length=512, description=f'{DOC_SECTOR_NAME}')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    location_ref: Annotated[Optional[int], Query(description='Location reference')] = None,
    admin1_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')
    ] = None,
    admin2_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')
    ] = None,
    admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')
    ] = None,
    admin1_ref: Annotated[Optional[int], Query(description='Admin1 reference')] = None,
    admin_level: Annotated[Optional[AdminLevel], Query(description='Filter the response by admin level')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of humanitarian needs data
    """
    ref_period_parameters = None
    result = await get_humanitarian_needs_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        admin2_ref=admin2_ref,
        gender=gender,
        age_range=age_range,
        disabled_marker=disabled_marker,
        sector_code=sector_code,
        population_group=population_group,
        population_status=population_status,
        population_min=population_min,
        population_max=population_max,
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


## refugees


@router.get(
    '/api/affected-people/refugees',
    response_model=HapiGenericResponse[RefugeesResponse],
    summary='Get refugees data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/affected-people/refugees',
    response_model=HapiGenericResponse[RefugeesResponse],
    summary='Get refugees data',
)
async def get_refugees(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    population_group: Annotated[Optional[PopulationGroup], Query(max_length=32, description='Population group')] = None,
    population_min: Annotated[int, Query(description='Population, minimum value for filter')] = None,
    population_max: Annotated[int, Query(description='Population, maximum value for filter')] = None,
    gender: Annotated[Optional[Gender], Query(max_length=3, description=f'{DOC_GENDER}')] = None,
    age_range: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_AGE_RANGE}')] = None,
    origin_location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    origin_location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    asylum_location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    asylum_location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of refugees data
    """
    ref_period_parameters = None
    result = await get_refugees_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        population_group=population_group,
        population_min=population_min,
        population_max=population_max,
        gender=gender,
        age_range=age_range,
        origin_location_code=origin_location_code,
        origin_location_name=origin_location_name,
        asylum_location_code=asylum_location_code,
        asylum_location_name=asylum_location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, RefugeesResponse)

from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_GENDER,
    DOC_AGE_RANGE,
    DOC_POPULATION_GROUP,
    DOC_POPULATION_STATUS,
    DOC_SECTOR_CODE,
    DOC_SECTOR_NAME,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.humanitarian_needs import HumanitarianNeedsResponse
from hdx_hapi.endpoints.models.refugees import RefugeesResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.humanitarian_needs_logic import get_humanitarian_needs_srv
from hdx_hapi.services.refugees_logic import get_refugees_srv
from hdx_hapi.services.sql_alchemy_session import get_db
from hapi_schema.utils.enums import Gender, PopulationGroup, PopulationStatus
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    # ReferencePeriodParameters,
    common_date_range_params,
    common_endpoint_parameters,
    # reference_period_parameters,
    common_location_parameters,
)

CONFIG = get_config()

router = APIRouter(
    tags=['Affected People'],
)

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
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    population_group: Annotated[
        Optional[PopulationGroup], Query(max_length=32, description=f'{DOC_POPULATION_GROUP}')
    ] = None,
    population_min: Annotated[
        Optional[int], Query(description='Filter the response by a lower bound for the population.')
    ] = None,
    population_max: Annotated[
        Optional[int], Query(description='Filter the response by a upper bound for the population.')
    ] = None,
    gender: Annotated[Optional[Gender], Query(max_length=3, description=f'{DOC_GENDER}')] = None,
    age_range: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_AGE_RANGE}')] = None,
    origin_location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    origin_location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    origin_has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    origin_in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    asylum_location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    asylum_location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    asylum_has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    asylum_in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_refugees_srv(
        common_date_range_params=common_date_range_params,
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
        origin_has_hrp=origin_has_hrp,
        origin_in_gho=origin_in_gho,
        asylum_location_code=asylum_location_code,
        asylum_location_name=asylum_location_name,
        asylum_has_hrp=asylum_has_hrp,
        asylum_in_gho=asylum_in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, RefugeesResponse)


get_refugees.__doc__ = (
    "UNHCR's Refugee data provides information about displaced people in a crisis. "
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'affected_people/#refugees-persons-of-concern">HDX HAPI documentation</a>, '
    'and the <a href="https://data.humdata.org/dataset/unhcr-population-data-for-world">original HDX source</a> '
    'website.'
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
    responses=ERROR_RESPONSES,  # type: ignore
    summary='Get humanitarian needs data',
)
async def get_humanitarian_needs(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    category: Annotated[
        Optional[str],
        Query(
            max_length=128,
            description='A category combining gender, age range, disability marker and population group information',
        ),
    ] = None,
    sector_code: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_SECTOR_CODE}')] = None,
    population_status: Annotated[
        Optional[PopulationStatus], Query(max_length=32, description=f'{DOC_POPULATION_STATUS}')
    ] = None,
    population_min: Annotated[
        Optional[int],
        Query(description='Filter the response by a lower bound for the population.'),
    ] = None,
    population_max: Annotated[
        Optional[int], Query(description='Filter the response by a upper bound for the population.')
    ] = None,
    sector_name: Annotated[Optional[str], Query(max_length=512, description=f'{DOC_SECTOR_NAME}')] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_humanitarian_needs_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        category=category,
        sector_code=sector_code,
        population_status=population_status,
        population_min=population_min,
        population_max=population_max,
        sector_name=sector_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(
        result, common_parameters.output_format, HumanitarianNeedsResponse
    )


get_humanitarian_needs.__doc__ = (
    "OCHA's Humanitarian Needs data, based on the Joint and Intersectoral Analysis Framework (JIAF), "
    'provides information about the number of people in need during a crisis. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'affected_people/#humanitarian-needs">HDX HAPI documentation</a>, '
    'and the <a href="https://www.jiaf.info/">original JIAF source</a> website.'
)

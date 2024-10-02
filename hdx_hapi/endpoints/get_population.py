from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import Gender

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN_LEVEL_FILTER,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_PROVIDER_ADMIN1_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_PROVIDER_ADMIN2_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
    DOC_GENDER,
    DOC_AGE_RANGE,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.population import PopulationResponse
from hdx_hapi.endpoints.models.poverty_rate import PovertyRateResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
    AdminLevel,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.poverty_rate_logic import get_poverty_rates_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Population & Socio-Economy'],
)


@router.get(
    '/api/population-social/population',
    response_model=HapiGenericResponse[PopulationResponse],
    summary='Get baseline population data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/population-social/population',
    response_model=HapiGenericResponse[PopulationResponse],
    summary='Get baseline population data',
)
async def get_populations(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    db: AsyncSession = Depends(get_db),
    gender: Annotated[Optional[Gender], Query(max_length=3, description=f'{DOC_GENDER}')] = None,
    age_range: Annotated[Optional[str], Query(max_length=32, description=f'{DOC_AGE_RANGE}')] = None,
    population_min: Annotated[
        Optional[int], Query(description='Filter the response by a lower bound for the population.')
    ] = None,
    population_max: Annotated[
        Optional[int], Query(description='Filter the response by a upper bound for the population.')
    ] = None,
    location_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    admin1_ref: Annotated[Optional[int], Query(description=f'{DOC_ADMIN1_REF}')] = None,
    admin1_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')
    ] = None,
    admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')
    ] = None,
    provider_admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_PROVIDER_ADMIN1_NAME}')
    ] = None,
    admin2_ref: Annotated[Optional[int], Query(description=f'{DOC_ADMIN2_REF}')] = None,
    admin2_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')
    ] = None,
    admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')
    ] = None,
    provider_admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_PROVIDER_ADMIN2_NAME}')
    ] = None,
    admin_level: Annotated[Optional[AdminLevel], Query(description=DOC_ADMIN_LEVEL_FILTER)] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_populations_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        gender=gender,
        age_range=age_range,
        population_min=population_min,
        population_max=population_max,
        admin1_ref=admin1_ref,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        provider_admin1_name=provider_admin1_name,
        admin2_ref=admin2_ref,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        provider_admin2_name=provider_admin2_name,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationResponse)


get_populations.__doc__ = (
    'Baseline population data sourced and maintained by UNFPA (UN Population Fund). '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'population_and_socio-economy/#baseline-population">HDX HAPI documentation</a>, '
    'and the <a href="https://data.humdata.org/organization/unfpa">UNFPA on HDX</a>.'
)


@router.get(
    '/api/population-social/poverty-rate',
    response_model=HapiGenericResponse[PovertyRateResponse],
    summary='Get poverty rate data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/population-social/poverty-rate',
    response_model=HapiGenericResponse[PovertyRateResponse],
    summary='Get poverty rate data',
)
async def get_poverty_rates(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    db: AsyncSession = Depends(get_db),
    mpi_min: Annotated[Optional[float], Query(description='Multidimensional Poverty Index (MPI), lower bound.')] = None,
    mpi_max: Annotated[Optional[float], Query(description='Multidimensional Poverty Index (MPI), upper bound.')] = None,
    location_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    provider_admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_PROVIDER_ADMIN1_NAME} {DOC_SEE_ADMIN1}')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_poverty_rates_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        mpi_min=mpi_min,
        mpi_max=mpi_max,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        provider_admin1_name=provider_admin1_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PovertyRateResponse)


get_poverty_rates.__doc__ = (
    'Poverty rate data from the Oxford Department of International Development. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'population_and_socio-economy/#poverty-rate">HDX HAPI documentation</a>, '
    'and the <a href="https://ophi.org.uk/global-mpi">Oxford Department of International Development</a> website.'
)

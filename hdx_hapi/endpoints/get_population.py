from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import Gender
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
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
    # ReferencePeriodParameters,
    common_endpoint_parameters,
    # reference_period_parameters,
    AdminLevel,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.poverty_rate_logic import get_poverty_rates_srv
from hdx_hapi.services.sql_alchemy_session import get_db

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
    population_min: Annotated[int, Query(description='Population, minimum value for filter')] = None,
    population_max: Annotated[int, Query(description='Population, maximum value for filter')] = None,
    location_ref: Annotated[int, Query(description='Location reference')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_ref: Annotated[int, Query(description='Admin1 reference')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
    # admin1_is_unspecified: Annotated[bool, Query(description='Location Adm1 is not specified')] = None,
    admin2_ref: Annotated[int, Query(description='Admin2 reference')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level')] = None,
    # admin2_is_unspecified: Annotated[bool, Query(description='Is admin2 specified or not')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of populations
    """
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
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin2_ref=admin2_ref,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationResponse)


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
    mpi_min: Annotated[Optional[float], Query(description='Multidimensional Poverty Index (MPI), lower bound')] = None,
    mpi_max: Annotated[Optional[float], Query(description='Multidimensional Poverty Index (MPI), upper bound')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of poverty rates
    """
    ref_period_parameters = None
    result = await get_poverty_rates_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        mpi_min=mpi_min,
        mpi_max=mpi_max,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PovertyRateResponse)

from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import Gender

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_GENDER,
    DOC_AGE_RANGE,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.models.population import PopulationResponse
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    common_date_range_params,
    common_endpoint_parameters,
    common_location_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Geography & Infrastructure'],
)

SUMMARY_TEXT = 'Get baseline population data'

ROUTER_DICT = {
    'response_model': HapiGenericResponse[PopulationResponse],
    'summary': SUMMARY_TEXT,
    'responses': ERROR_RESPONSES,
}


@router.get('/api/geography-infrastructure/baseline-population', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v1/population-social/population', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v2/geography-infrastructure/baseline-population', **ROUTER_DICT)
async def get_population(
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
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
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_populations_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        gender=gender,
        age_range=age_range,
        population_min=population_min,
        population_max=population_max,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, PopulationResponse)


get_population.__doc__ = (
    'Baseline population data sourced and maintained by UNFPA (UN Population Fund). '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'population_and_socio-economy/#baseline-population">HDX HAPI documentation</a>, '
    'and the <a href="https://data.humdata.org/organization/unfpa">UNFPA on HDX</a>.'
)

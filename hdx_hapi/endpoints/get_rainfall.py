from decimal import Decimal
from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import AggregationPeriod

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_AGGREGATION_PERIOD,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.models.rainfall import RainfallResponse
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    common_date_range_params,
    common_endpoint_parameters,
    common_location_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.rainfall_logic import get_rainfall_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Climate'],
)

SUMMARY_TEXT = 'Get rainfall data'

ROUTER_DICT = {
    'response_model': HapiGenericResponse[RainfallResponse],
    'summary': SUMMARY_TEXT,
    'responses': ERROR_RESPONSES,
}


@router.get('/api/climate/rainfall', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v1/climate/rainfall', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v2/climate/rainfall', **ROUTER_DICT)
async def get_rainfall(
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    aggregation_period: Annotated[
        Optional[AggregationPeriod], Query(max_length=12, description=f'{DOC_AGGREGATION_PERIOD}')
    ] = None,
    # rainfall: Annotated[Optional[Decimal], Query(description='Filter the response by rainfall.')] = None,
    # rainfall_long_term_average: Annotated[
    #     Optional[Decimal], Query(description='Filter the response by rainfall long term average.')
    # ] = None,
    # rainfall_anomaly_pct: Annotated[
    #     Optional[Decimal], Query(description='Filter the response by rainfall anomaly pct.')
    # ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_rainfall_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        aggregation_period=aggregation_period,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, RainfallResponse)


get_rainfall.__doc__ = (
    f'Rainfall data . See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    # 'population_and_socio-economy/#baseline-population">HDX HAPI documentation</a>, '
    # 'and the <a href="https://data.humdata.org/organization/unfpa">UNFPA on HDX</a>.'
)

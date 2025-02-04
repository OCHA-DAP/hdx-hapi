from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Query

from hapi_schema.utils.enums import EventType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_ACLED_EVENT_TYPE,
)
from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.conflict_event import ConflictEventResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    # ReferencePeriodParameters,
    common_date_range_params,
    common_endpoint_parameters,
    common_location_parameters,
    # reference_period_parameters,
)
from hdx_hapi.services.conflict_view_logic import get_conflict_event_srv
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Coordination & Context'],
)
SUMMARY_TEXT = 'Get the list of conflict events'

ROUTER_DICT = {
    'response_model': HapiGenericResponse[ConflictEventResponse],
    'summary': SUMMARY_TEXT,
    'responses': ERROR_RESPONSES,
}


@router.get('/api/coordination-context/conflict-events', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v1/coordination-context/conflict-event', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v2/coordination-context/conflict-events', **ROUTER_DICT)
async def get_conflict_event(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    event_type: Annotated[
        Optional[EventType],
        Query(description=DOC_ACLED_EVENT_TYPE),
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_conflict_event_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        event_type=event_type,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, ConflictEventResponse)


get_conflict_event.__doc__ = (
    'Armed Conflict Location & Events Data from ACLED. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'coordination_and_context/#conflict-events">HDX HAPI documentation</a>, '
    'and the <a href="https://acleddata.com/">original ACLED source</a> website.'
)

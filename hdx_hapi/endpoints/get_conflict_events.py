from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Query

from hapi_schema.utils.enums import EventType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN1_REF,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
    DOC_SEE_LOC,
    DOC_ACLED_EVENT_TYPE,
)
from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.conflict_event import ConflictEventResponse
from hdx_hapi.endpoints.util.util import (
    AdminLevel,
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
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


@router.get(
    '/api/coordination-context/conflict-event',
    response_model=HapiGenericResponse[ConflictEventResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/v1/coordination-context/conflict-event',
    response_model=HapiGenericResponse[ConflictEventResponse],
    summary=SUMMARY_TEXT,
)
async def get_conflict_events(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    event_type: Annotated[
        Optional[EventType],
        Query(description=DOC_ACLED_EVENT_TYPE),
    ] = None,
    location_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    admin1_ref: Annotated[Optional[int], Query(description=f'{DOC_ADMIN1_REF}')] = None,
    admin1_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')
    ] = None,
    admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')
    ] = None,
    admin2_ref: Annotated[Optional[int], Query(description=f'{DOC_ADMIN2_REF}')] = None,
    admin2_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')
    ] = None,
    admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')
    ] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level.')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_conflict_event_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        event_type=event_type,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        admin1_ref=admin1_ref,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, ConflictEventResponse)


get_conflict_events.__doc__ = (
    'Armed Conflict Location & Events Data from ACLED. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'coordination_and_context/#conflict-events">HDX HAPI documentation</a>, '
    'and the <a href="https://acleddata.com/">original ACLED source</a> website.'
)

from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from hdx_hapi.config.config import get_config
from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    # DOC_HAPI_UPDATED_DATE_MIN,
    # DOC_HAPI_UPDATED_DATE_MAX,
    # DOC_HAPI_REPLACED_DATE_MIN,
    # DOC_HAPI_REPLACED_DATE_MAX,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.models.operational_presence import OperationalPresenceResponse
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
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.operational_presence_logic import get_operational_presences_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Coordination & Context'],
)

SUMMARY_TEXT = 'Get the list of organizations present and in which humanitarian sectors they are working'


@router.get(
    '/api/coordination-context/operational-presence',
    response_model=HapiGenericResponse[OperationalPresenceResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/v1/coordination-context/operational-presence',
    response_model=HapiGenericResponse[OperationalPresenceResponse],
    responses=ERROR_RESPONSES,  # type: ignore
    summary=SUMMARY_TEXT,
)
async def get_operational_presence(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    sector_code: Annotated[
        Optional[str],
        Query(
            max_length=512,
            description=(
                'Filter the response by sector codes, which describe the humanitarian sector '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_sector_api_v1_metadata_sector_get" '
                'target="_blank">sector endpoint</a> for details.'
            ),
        ),
    ] = None,
    sector_name: Annotated[
        Optional[str],
        Query(
            max_length=512,
            description=(
                'Filter the response by sector names, '
                'which describe the humanitarian sector to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_sector_api_v1_metadata_sector_get" '
                'target="_blank">sector endpoint</a> for details.'
            ),
        ),
    ] = None,
    org_acronym: Annotated[
        Optional[str],
        Query(
            max_length=32,
            description=(
                'Filter the response by the acronym of the organization '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_org_api_v1_metadata_org_get" '
                'target="_blank">org endpoint</a> for details.'
            ),
        ),
    ] = None,
    org_name: Annotated[
        Optional[str],
        Query(
            max_length=512,
            description=(
                'Filter the response by the name of the organization '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_org_api_v1_metadata_org_get" '
                'target="_blank">org endpoint</a> for details.'
            ),
        ),
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    ref_period_parameters = None
    result = await get_operational_presences_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        sector_code=sector_code,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(
        result, common_parameters.output_format, OperationalPresenceResponse
    )


get_operational_presence.__doc__ = (
    "OCHA's 3W (Who is doing What Where) Operational Presence data provides "
    'information about which organizations are working in different locations affected by a crisis. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'coordination_and_context/#who-is-doing-what-where-operational-presence">HDX HAPI documentation</a>, '
    'and the <a href="https://3w.unocha.org/">original OCHA 3W source</a> website. '
)

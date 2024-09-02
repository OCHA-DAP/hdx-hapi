from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from hdx_hapi.config.config import get_config
from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN_LEVEL_FILTER,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
    DOC_SEE_LOC,
    # DOC_HAPI_UPDATED_DATE_MIN,
    # DOC_HAPI_UPDATED_DATE_MAX,
    # DOC_HAPI_REPLACED_DATE_MIN,
    # DOC_HAPI_REPLACED_DATE_MAX,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.operational_presence import OperationalPresenceResponse
from hdx_hapi.endpoints.util.util import (
    AdminLevel,
    CommonEndpointParams,
    OutputFormat,
    # ReferencePeriodParameters,
    common_endpoint_parameters,
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
    summary=SUMMARY_TEXT,
)
async def get_operational_presences(
    # ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    sector_code: Annotated[
        str,
        Query(
            max_length=512,
            description=(
                'Filter the response by sector codes, which describe the humanitarian sector '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_sectors_api_v1_metadata_sector_get" '
                'target="_blank">sector endpoint</a> for details.'
            ),
        ),
    ] = None,
    sector_name: Annotated[
        str,
        Query(
            max_length=512,
            description=(
                'Filter the response by sector names, '
                'which describe the humanitarian sector to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_sectors_api_v1_metadata_sector_get" '
                'target="_blank">sector endpoint</a> for details.'
            ),
        ),
    ] = None,
    org_acronym: Annotated[
        str,
        Query(
            max_length=32,
            description=(
                'Filter the response by the acronym of the organization '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_orgs_api_v1_metadata_org_get" '
                'target="_blank">org endpoint</a> for details.'
            ),
        ),
    ] = None,
    org_name: Annotated[
        str,
        Query(
            max_length=512,
            description=(
                'Filter the response by the name of the organization '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Metadata/get_orgs_api_v1_metadata_org_get" '
                'target="_blank">org endpoint</a> for details.'
            ),
        ),
    ] = None,
    location_ref: Annotated[int, Query(description=f'{DOC_LOCATION_REF}')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
    admin1_ref: Annotated[int, Query(description=f'{DOC_ADMIN1_REF}')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
    # admin1_is_unspecified: Annotated[bool, Query(description='Location Adm1 is not specified')] = None,
    admin2_ref: Annotated[int, Query(description=f'{DOC_ADMIN2_REF}')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')] = None,
    admin_level: Annotated[AdminLevel, Query(description=DOC_ADMIN_LEVEL_FILTER)] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    ref_period_parameters = None
    result = await get_operational_presences_srv(
        pagination_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        sector_code=sector_code,
        # dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        # resource_update_date_min=resource_update_date_min,
        # resource_update_date_max=resource_update_date_max,
        # hapi_updated_date_min=hapi_updated_date_min,
        # hapi_updated_date_max=hapi_updated_date_max,
        # hapi_replaced_date_min=hapi_replaced_date_min,
        # hapi_replaced_date_max=hapi_replaced_date_max,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_ref=location_ref,
        has_hrp=has_hrp,
        in_gho=in_gho,
        # admin1_is_unspecified=admin1_is_unspecified,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin1_ref=admin1_ref,
        # admin2_is_unspecified=admin2_is_unspecified
        # dataset_hdx_id=dataset_hdx_id,
        # dataset_hdx_stub=dataset_hdx_stub,
        # dataset_title=dataset_title,
        # dataset_hdx_provider_name=dataset_hdx_provider_name,
        # resource_hdx_id=resource_hdx_id,
        # resource_name=resource_name,
        # org_type_code=org_type_code,
        # org_type_description=org_type_description,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, OperationalPresenceResponse)


get_operational_presences.__doc__ = (
    "OCHA's 3W (Who is doing What Where) Operational Presence data provides "
    'information about which organizations are working in different locations affected by a crisis. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'coordination_and_context/#who-is-doing-what-where-operational-presence">HDX HAPI documentation</a>, '
    'and the <a href="https://3w.unocha.org/">original OCHA 3W source</a> website. '
)

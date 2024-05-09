from datetime import date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime

from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.operational_presence import OperationalPresenceResponse
from hdx_hapi.endpoints.util.util import AdminLevel, CommonEndpointParams, OutputFormat, common_endpoint_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.operational_presence_logic import get_operational_presences_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['3W Operational Presence'],
)

SUMMARY_TEXT = (
    'Get the list of organizations present and in which humanitarian sectors they are working. '
    "There are two versions of this endpoint to support the uppercase and lowercase 'w'"
)


@router.get(
    '/api/themes/3w',
    response_model=List[OperationalPresenceResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/themes/3W',
    response_model=List[OperationalPresenceResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/v1/themes/3w',
    response_model=List[OperationalPresenceResponse],
    summary=SUMMARY_TEXT,
)
@router.get(
    '/api/v1/themes/3W',
    response_model=List[OperationalPresenceResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
async def get_operational_presences(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    sector_code: Annotated[
        str,
        Query(
            max_length=512,
            description=(
                'Filter the response by sector codes, which describe the humanitarian sector '
                'to which the operational presence applies. '
                'See the <a href="/docs#/Humanitarian%20Organizations%20and%20Sectors/get_sectors_api_v1_sector_get" '
                'target="_blank">sector endpoint</a> for details'
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
                'See the <a href="/docs#/Humanitarian%20Organizations%20and%20Sectors/get_sectors_api_v1_sector_get" '
                'target="_blank">sector endpoint</a> for details'
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
                'See the <a href="/docs#/Humanitarian%20Organizations%20and%20Sectors/get_orgs_api_v1_org_get" '
                'target="_blank">org endpoint</a> for details'
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
                'See the <a href="/docs#/Humanitarian%20Organizations%20and%20Sectors/get_orgs_api_v1_org_get" '
                'target="_blank">org endpoint</a> for details'
            ),
        ),
    ] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')] = None,
    # admin1_is_unspecified: Annotated[bool, Query(description='Location Adm1 is not specified')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level')] = None,
    # admin2_is_unspecified: Annotated[bool, Query(description='Location Adm2 is not specified')] = None,
    resource_update_date_min: Annotated[
        NaiveDatetime | date,
        Query(
            description=(
                'Filter the response to data updated on or after this date. '
                'For example 2020-01-01 or 2020-01-01T00:00:00'
            ),
            openapi_examples={'2020-01-01': {'value': '2020-01-01'}},
        ),
    ] = None,
    resource_update_date_max: Annotated[
        NaiveDatetime | date,
        Query(
            description=(
                'Filter the response to data updated on or before this date. '
                'For example 2024-12-31 or 2024-12-31T23:59:59'
            ),
            openapi_examples={'2024-12-31': {'value': '2024-12-31'}},
        ),
    ] = None,
    dataset_hdx_provider_stub: Annotated[
        str,
        Query(
            max_length=128,
            description=(
                'Filter the query by the organizations contributing the source data to HDX. '
                'If you want to filter by the organization mentioned in the operational presence record, '
                'see the org_name and org_acronym parameters below.'
            ),
        ),
    ] = None,
    # org_ref: Annotated[int, Query(ge=1, description='Organization reference')] = None,
    # dataset_hdx_id: Annotated[str, Query(max_length=36, description='HDX Dataset ID')] = None,
    # dataset_hdx_stub: Annotated[str, Query(max_length=128, description='HDX Dataset Name')] = None,
    # dataset_title: Annotated[str, Query(max_length=1024, description='Location name')] = None,
    # dataset_hdx_provider_name: Annotated[str, Query(max_length=512, description='Location name')] = None,
    # resource_hdx_id: Annotated[str, Query(max_length=36, description='Location name')] = None,
    # resource_name: Annotated[str, Query(max_length=256, description='Location name')] = None,
    # org_type_code: Annotated[str, Query(max_length=32, description='Location name')] = None,
    # org_type_description: Annotated[str, Query(max_length=512, description='Location name')] = None,
    # admin1_name: Annotated[str, Query(max_length=512, description='Location Adm1 Name')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    UNOCHA's 3W (Who is doing What Where) Operational Presence data provides
    information about which organizations are working in different locations affected by a
    crisis. <a href="https://3w.unocha.org/">Learn more about 3W</a>
    """
    result = await get_operational_presences_srv(
        pagination_parameters=common_parameters,
        db=db,
        sector_code=sector_code,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        # admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
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

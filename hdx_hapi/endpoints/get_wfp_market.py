from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN_LEVEL_FILTER,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_PROVIDER_ADMIN1_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
    DOC_PROVIDER_ADMIN2_NAME,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.wfp_market import WfpMarketResponse
from hdx_hapi.endpoints.util.util import (
    AdminLevel,
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.sql_alchemy_session import get_db
from hdx_hapi.services.wfp_market_logic import get_wfp_markets_srv

router = APIRouter(
    tags=['Metadata'],
)

SUMMARY_TEXT = 'Get the list of WFP markets.'


@router.get(
    '/api/metadata/wfp-market',
    response_model=HapiGenericResponse[WfpMarketResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/wfp-market',
    response_model=HapiGenericResponse[WfpMarketResponse],
    summary=SUMMARY_TEXT,
)
async def get_wfp_market(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[
        Optional[str],
        Query(max_length=32, description='Filter the response by the unique code identifying the market.'),
    ] = None,
    name: Annotated[
        Optional[str], Query(max_length=512, description='Filter the response by the name of the market.')
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
    """
    Provide physical market location information to use in conjunction with the food-prices endpoint
    """
    result = await get_wfp_markets_srv(
        pagination_parameters=common_parameters,
        db=db,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        provider_admin1_name=provider_admin1_name,
        location_ref=location_ref,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        provider_admin2_name=provider_admin2_name,
        admin1_ref=admin1_ref,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, WfpMarketResponse)

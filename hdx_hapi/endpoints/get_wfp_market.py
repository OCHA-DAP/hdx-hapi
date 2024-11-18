from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.models.wfp_market import WfpMarketResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    CommonLocationParameters,
    common_endpoint_parameters,
    common_location_parameters,
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
    responses=ERROR_RESPONSES,  # type: ignore
    summary=SUMMARY_TEXT,
)
async def get_wfp_market(
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[
        Optional[str],
        Query(max_length=32, description='Filter the response by the unique code identifying the market.'),
    ] = None,
    name: Annotated[
        Optional[str], Query(max_length=512, description='Filter the response by the name of the market.')
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    """
    Provide physical market location information to use in conjunction with the food-prices endpoint
    """
    result = await get_wfp_markets_srv(
        pagination_parameters=common_parameters,
        common_location_params=common_location_params,
        db=db,
        code=code,
        name=name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, WfpMarketResponse)

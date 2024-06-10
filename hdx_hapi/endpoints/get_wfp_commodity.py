from typing import Annotated, Optional
from fastapi import APIRouter, Depends, Query
from hapi_schema.utils.enums import CommodityCategory
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import DOC_COMMODITY_CATEGORY
from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.wfp_commodity import WfpCommodityResponse
from hdx_hapi.endpoints.util.util import CommonEndpointParams, OutputFormat, common_endpoint_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.sql_alchemy_session import get_db
from hdx_hapi.services.wfp_commodity_logic import get_wfp_commodities_srv


router = APIRouter(
    tags=['Metadata'],
)

SUMMARY = 'Get the list of WFP commodities'


@router.get(
    '/api/metadata/wfp-commodity',
    response_model=HapiGenericResponse[WfpCommodityResponse],
    summary=SUMMARY,
    include_in_schema=False,
)
@router.get(
    '/api/v1/metadata/wfp-commodity',
    response_model=HapiGenericResponse[WfpCommodityResponse],
    summary=SUMMARY,
)
async def get_wfp_commodities(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[
        Optional[str],
        Query(max_length=32, description='Filter the response by the unique code identifying the commodity.'),
    ] = None,
    category: Annotated[Optional[CommodityCategory], Query(description=DOC_COMMODITY_CATEGORY)] = None,
    name: Annotated[
        Optional[str], Query(max_length=512, description='Filter the response by the name of the commodity.')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Provide commodity information to use in conjunction with the food-prices endpoint
    """
    result = await get_wfp_commodities_srv(
        pagination_parameters=common_parameters, db=db, code=code, category=category, name=name
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, WfpCommodityResponse)

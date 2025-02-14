from decimal import Decimal
from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.config import get_config
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_IN_GHO,
    DOC_PRICE_FLAG,
    DOC_PRICE_TYPE,
    DOC_COMMODITY_CATEGORY,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.error import ERROR_RESPONSES
from hdx_hapi.endpoints.models.food_price import FoodPriceResponse
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonEndpointParams,
    CommonLocationParameters,
    common_date_range_params,
    common_endpoint_parameters,
    common_location_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.food_price_logic import get_food_prices_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Food Security, Nutrition & Poverty'],
)

SUMMARY_TEXT = 'Get food prices'

ROUTER_DICT = {
    'response_model': HapiGenericResponse[FoodPriceResponse],
    'summary': SUMMARY_TEXT,
    'responses': ERROR_RESPONSES,
}


@router.get('/api/food-security-nutrition-poverty/food-prices-market-monitor', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v1/food/food-price', include_in_schema=False, **ROUTER_DICT)
@router.get('/api/v2/food-security-nutrition-poverty/food-prices-market-monitor', **ROUTER_DICT)
async def get_food_price(
    common_date_range_params: Annotated[CommonDateRangeParams, Depends(common_date_range_params)],
    common_location_params: Annotated[CommonLocationParameters, Depends(common_location_parameters)],
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    market_code: Annotated[
        Optional[str], Query(max_length=32, description='Filter the response by the unique code identifying the market')
    ] = None,
    market_name: Annotated[
        Optional[str], Query(max_length=512, description='Filter the response by the name of the market')
    ] = None,
    commodity_code: Annotated[
        Optional[str],
        Query(max_length=32, description='Filter the response by the unique code identifying the commodity'),
    ] = None,
    commodity_category: Annotated[Optional[CommodityCategory], Query(description=DOC_COMMODITY_CATEGORY)] = None,
    commodity_name: Annotated[
        Optional[str], Query(max_length=512, description='Filter the response by the name of the commodity')
    ] = None,
    price_flag: Annotated[Optional[PriceFlag], Query(description=f'{DOC_PRICE_FLAG}')] = None,
    price_type: Annotated[Optional[PriceType], Query(description=f'{DOC_PRICE_TYPE}')] = None,
    price_min: Annotated[
        Optional[Decimal], Query(description='Filter the response by a lower bound for the price.')
    ] = None,
    price_max: Annotated[
        Optional[Decimal], Query(description='Filter the response by a upper bound for the price.')
    ] = None,
    has_hrp: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_HAS_HRP}')] = None,
    in_gho: Annotated[Optional[bool], Query(description=f'{DOC_LOCATION_IN_GHO}')] = None,
):
    result = await get_food_prices_srv(
        common_date_range_params=common_date_range_params,
        pagination_parameters=common_parameters,
        common_location_params=common_location_params,
        db=db,
        market_code=market_code,
        market_name=market_name,
        commodity_code=commodity_code,
        commodity_category=commodity_category,
        commodity_name=commodity_name,
        price_flag=price_flag,
        price_type=price_type,
        price_min=price_min,
        price_max=price_max,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )
    return transform_result_to_csv_stream_if_requested(result, common_parameters.output_format, FoodPriceResponse)


get_food_price.__doc__ = (
    'The World Food Programme (WFP) food prices data provides information about food prices for a range of commodities '
    'at markets across the world. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'food_security_and_nutrition/#food-prices">HDX HAPI documentation</a>, '
    'and the <a href="https://dataviz.vam.wfp.org/economic/prices">original WFP source</a> website.'
)

from decimal import Decimal
from typing import Annotated, Optional
from fastapi import Depends, Query, APIRouter

from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.config import get_config
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
    DOC_PRICE_FLAG,
    DOC_PRICE_TYPE,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2,
    DOC_SEE_LOC,
    DOC_COMMODITY_CATEGORY,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.food_price import FoodPriceResponse
from hdx_hapi.endpoints.util.util import (
    AdminLevel,
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.food_price_logic import get_food_prices_srv
from hdx_hapi.services.sql_alchemy_session import get_db

CONFIG = get_config()

router = APIRouter(
    tags=['Food Security & Nutrition'],
)

SUMMARY_TEXT = 'Get food prices'


@router.get(
    '/api/food/food-price',
    response_model=HapiGenericResponse[FoodPriceResponse],
    summary=SUMMARY_TEXT,
    include_in_schema=False,
)
@router.get(
    '/api/v1/food/food-price',
    response_model=HapiGenericResponse[FoodPriceResponse],
    summary=SUMMARY_TEXT,
)
async def get_food_price(
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
    result = await get_food_prices_srv(
        pagination_parameters=common_parameters,
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
    return transform_result_to_csv_stream_if_requested(result, output_format, FoodPriceResponse)


get_food_price.__doc__ = (
    'The World Food Programme (WFP) food prices data provides information about food prices for a range of commodities '
    'at markets across the world. '
    f'See the more detailed technical <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/'
    'food_security_and_nutrition/#food-prices">HDX HAPI documentation</a>, '
    'and the <a href="https://dataviz.vam.wfp.org/economic/prices">original WFP source</a> website.'
)

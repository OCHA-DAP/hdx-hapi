from decimal import Decimal
from typing import Optional, Sequence, Union
from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from hapi_schema.db_views_as_tables import DBFoodPriceVAT
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.food_price_dao import food_price_view_list
from hdx_hapi.db.models.views.all_views import FoodPriceView
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams


async def get_food_prices_srv(
    pagination_parameters: PaginationParams,
    common_location_params: CommonLocationParameters, 
    db: AsyncSession,
    market_code: Optional[str] = None,
    market_name: Optional[str] = None,
    commodity_code: Optional[str] = None,
    commodity_category: Optional[CommodityCategory] = None,
    commodity_name: Optional[str] = None,
    price_flag: Optional[PriceFlag] = None,
    price_type: Optional[PriceType] = None,
    price_min: Optional[Decimal] = None,
    price_max: Optional[Decimal] = None,
    # lat: Optional[float] = None,
    # lon: Optional[float] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Union[Sequence[FoodPriceView], Sequence[DBFoodPriceVAT]]:

    return await food_price_view_list(
        pagination_parameters=pagination_parameters,
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

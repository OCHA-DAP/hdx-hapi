from decimal import Decimal
from typing import Optional, Sequence
from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.food_price_dao import food_price_view_list
from hdx_hapi.db.models.views.all_views import FoodPriceView
from hdx_hapi.endpoints.util.util import AdminLevel, PaginationParams
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_food_prices_srv(
    pagination_parameters: PaginationParams,
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
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    location_ref: Optional[int] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin_level: Optional[AdminLevel] = None,
) -> Sequence[FoodPriceView]:
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await food_price_view_list(
        pagination_parameters=pagination_parameters,
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
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        admin1_ref=admin1_ref,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
    )

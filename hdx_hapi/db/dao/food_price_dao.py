from decimal import Decimal
import logging
from typing import Optional, Sequence

from hapi_schema.utils.enums import CommodityCategory, PriceFlag, PriceType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    case_insensitive_filter,
)
from hdx_hapi.db.models.views.all_views import FoodPriceView
from hdx_hapi.endpoints.util.util import PaginationParams


logger = logging.getLogger(__name__)


async def food_price_view_list(
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
    admin1_is_unspecified: Optional[bool] = None,
    location_ref: Optional[int] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
) -> Sequence[FoodPriceView]:
    query = select(FoodPriceView)
    if market_code:
        query = case_insensitive_filter(query, FoodPriceView.market_code, market_code)
    if market_name:
        query = query.where(FoodPriceView.market_name.icontains(market_name))
    if commodity_code:
        query = case_insensitive_filter(query, FoodPriceView.commodity_code, commodity_code)
    if commodity_category:
        query = query.where(FoodPriceView.commodity_category == commodity_category)
    if commodity_name:
        query = query.where(FoodPriceView.commodity_name.icontains(commodity_name))
    if price_flag:
        query = query.where(FoodPriceView.price_flag == price_flag)
    if price_type:
        query = query.where(FoodPriceView.price_type == price_type)
    if price_min:
        query = query.where(FoodPriceView.price >= price_min)
    if price_max:
        query = query.where(FoodPriceView.price < price_max)

    query = apply_location_admin_filter(
        query,
        FoodPriceView,
        location_ref,
        location_code,
        location_name,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
    )

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    food_prices = result.scalars().all()

    return food_prices

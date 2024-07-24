import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    case_insensitive_filter,
)
from hdx_hapi.db.models.views.vat_or_view import WfpMarketView
from hdx_hapi.endpoints.util.util import PaginationParams


logger = logging.getLogger(__name__)


async def wfp_market_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    name: Optional[str] = None,
    # lat: Optional[float] = None,
    # lon: Optional[float] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    location_ref: Optional[int] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
) -> Sequence[WfpMarketView]:
    query = select(WfpMarketView)
    if code:
        query = case_insensitive_filter(query, WfpMarketView.code, code)
    if name:
        query = query.where(WfpMarketView.name.icontains(name))
    query = apply_location_admin_filter(
        query,
        WfpMarketView,
        location_ref,
        location_code,
        location_name,
        has_hrp,
        in_gho,
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
    wfp_markets = result.scalars().all()

    return wfp_markets

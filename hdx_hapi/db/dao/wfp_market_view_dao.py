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
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams


logger = logging.getLogger(__name__)


async def wfp_market_view_list(
    pagination_parameters: PaginationParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    code: Optional[str] = None,
    name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[WfpMarketView]:
    query = select(WfpMarketView)
    if code:
        query = case_insensitive_filter(query, WfpMarketView.code, code)
    if name:
        query = query.where(WfpMarketView.name.icontains(name))
    query = apply_location_admin_filter(
        query,
        WfpMarketView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(WfpMarketView.code)

    result = await db.execute(query)
    wfp_markets = result.scalars().all()

    return wfp_markets

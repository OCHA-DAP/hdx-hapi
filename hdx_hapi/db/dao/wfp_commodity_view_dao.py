import logging
from typing import Optional, Sequence

from hapi_schema.utils.enums import CommodityCategory
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import WfpCommodityView
from hdx_hapi.db.dao.util.util import (
    apply_pagination,
    case_insensitive_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams


logger = logging.getLogger(__name__)


async def wfp_commodity_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    category: Optional[CommodityCategory] = None,
    name: Optional[str] = None,
) -> Sequence[WfpCommodityView]:
    query = select(WfpCommodityView)
    if code:
        query = case_insensitive_filter(query, WfpCommodityView.code, code)
    if category:
        query = query.where(WfpCommodityView.category == category)
    if name:
        query = query.where(WfpCommodityView.name.icontains(name))

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    wfp_commodities = result.scalars().all()
    return wfp_commodities

from typing import Optional
from hapi_schema.utils.enums import CommodityCategory
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.wfp_commodity_view_dao import wfp_commodity_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_wfp_commodities_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    category: Optional[CommodityCategory] = None,
    name: Optional[str] = None
):
    return await wfp_commodity_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        category=category,
        name=name
   )

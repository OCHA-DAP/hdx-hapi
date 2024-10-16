from typing import Optional, Sequence, Union
from hapi_schema.db_views_as_tables import DBWfpCommodityVAT
from hapi_schema.utils.enums import CommodityCategory
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.wfp_commodity_view_dao import wfp_commodity_view_list
from hdx_hapi.db.models.views.all_views import WfpCommodityView
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_wfp_commodities_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    category: Optional[CommodityCategory] = None,
    name: Optional[str] = None,
) -> Union[Sequence[WfpCommodityView], Sequence[DBWfpCommodityVAT]]:
    return await wfp_commodity_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        category=category,
        name=name,
    )

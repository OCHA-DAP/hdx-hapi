from typing import Optional, Sequence, Union
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.db_views_as_tables import DBWfpMarketVAT

from hdx_hapi.db.dao.wfp_market_view_dao import wfp_market_view_list
from hdx_hapi.db.models.views.all_views import WfpMarketView
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams


async def get_wfp_markets_srv(
    pagination_parameters: PaginationParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    code: Optional[str] = None,
    name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Union[Sequence[WfpMarketView], Sequence[DBWfpMarketVAT]]:
    return await wfp_market_view_list(
        pagination_parameters=pagination_parameters,
        common_location_params=common_location_params,
        db=db,
        code=code,
        name=name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

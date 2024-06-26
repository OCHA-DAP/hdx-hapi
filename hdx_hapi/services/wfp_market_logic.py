from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.wfp_market_view_dao import wfp_market_view_list
from hdx_hapi.db.models.views.all_views import WfpMarketView
from hdx_hapi.endpoints.util.util import AdminLevel, PaginationParams
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_wfp_markets_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    name: Optional[str] = None,
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
) -> Sequence[WfpMarketView]:
    
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await wfp_market_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
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

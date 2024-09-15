from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.db.models.views.all_views import IdpsView
from hdx_hapi.db.dao.idps_view_dao import idps_view_list

from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_idps_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    admin2_ref: Optional[int] = None,
    # provider_admin1_name: Optional[str] = None,
    # provider_admin2_name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
) -> Sequence[IdpsView]:
    return await idps_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        admin2_ref=admin2_ref,
        # provider_admin1_name=provider_admin1_name,
        # provider_admin2_name=provider_admin2_name,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
    )

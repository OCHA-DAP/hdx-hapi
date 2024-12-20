from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.location_view_dao import locations_view_list
from hdx_hapi.endpoints.util.util import CommonDateRangeParams, PaginationParams, ReferencePeriodParameters


async def get_locations_srv(
    common_date_range_params: CommonDateRangeParams,
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    id: Optional[int] = None,
    code: Optional[str] = None,
    name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    return await locations_view_list(
        common_date_range_params=common_date_range_params,
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        code=code,
        name=name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.admin1_view_dao import admin1_view_list
from hdx_hapi.endpoints.util.util import CommonDateRangeParams, PaginationParams, ReferencePeriodParameters


async def get_admin1_srv(
    common_date_range_params: CommonDateRangeParams,
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    id: Optional[int] = None,
    location_ref: Optional[int] = None,
    code: Optional[str] = None,
    name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
):
    return await admin1_view_list(
        common_date_range_params=common_date_range_params,
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        location_ref=location_ref,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
    )

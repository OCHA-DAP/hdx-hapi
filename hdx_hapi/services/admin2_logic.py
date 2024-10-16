from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.admin2_view_dao import admin2_view_list
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_admin2_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    id: Optional[int] = None,
    admin1_ref: Optional[int] = None,
    location_ref: Optional[int] = None,
    code: Optional[str] = None,
    name: Optional[str] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
):
    return await admin2_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        admin1_ref=admin1_ref,
        location_ref=location_ref,
        code=code,
        name=name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_code=location_code,
        location_name=location_name,
    )

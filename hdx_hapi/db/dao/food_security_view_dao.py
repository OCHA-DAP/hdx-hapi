from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hapi_schema.utils.enums import IPCType, IPCPhase

from hdx_hapi.db.models.views.vat_or_view import FoodSecurityView
from hdx_hapi.db.dao.util.util import (
    ReferencePeriodParameters,
    PaginationParams,
    apply_location_admin_filter,
    apply_reference_period_filter,
    apply_pagination,
)


async def food_security_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    ipc_phase: Optional[IPCPhase] = None,
    ipc_type: Optional[IPCType] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_code: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    location_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin2_ref: Optional[int] = None,
):
    query = select(FoodSecurityView)

    if ipc_phase:
        query = query.where(FoodSecurityView.ipc_phase == ipc_phase)
    if ipc_type:
        query = query.where(FoodSecurityView.ipc_type == ipc_type)

    query = apply_location_admin_filter(
        query,
        FoodSecurityView,
        location_ref,
        location_code,
        location_name,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, FoodSecurityView)
    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    food_security = result.scalars().all()
    return food_security

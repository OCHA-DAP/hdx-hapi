from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hapi_schema.utils.enums import IPCType, IPCPhase

from hdx_hapi.db.models.views.vat_or_view import FoodSecurityView
from hdx_hapi.db.dao.util.util import (
    ReferencePeriodParameters,
    PaginationParams,
    apply_date_range_filter,
    apply_location_admin_filter,
    apply_reference_period_filter,
    apply_pagination,
)
from hdx_hapi.endpoints.util.util import CommonDateRangeParams, CommonLocationParameters


async def food_security_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_date_range_params: CommonDateRangeParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    ipc_phase: Optional[IPCPhase] = None,
    ipc_type: Optional[IPCType] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    query = select(FoodSecurityView)

    if ipc_phase:
        query = query.where(FoodSecurityView.ipc_phase == ipc_phase)
    if ipc_type:
        query = query.where(FoodSecurityView.ipc_type == ipc_type)

    query = apply_date_range_filter(
        query,
        FoodSecurityView,
        common_date_range_params,
    )

    query = apply_location_admin_filter(
        query,
        FoodSecurityView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, FoodSecurityView)
    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        FoodSecurityView.admin2_ref,
        FoodSecurityView.ipc_phase,
        FoodSecurityView.ipc_type,
        FoodSecurityView.reference_period_start,
    )

    result = await db.execute(query)
    food_security = result.scalars().all()
    return food_security

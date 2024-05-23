from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import FoodSecurityView
from hdx_hapi.db.dao.util.util import (
    ReferencePeriodParameters,
    PaginationParams,
    apply_location_admin_filter,
    apply_reference_period_filter,
    apply_pagination,
    case_insensitive_filter,
)


async def food_security_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    ipc_phase_code: str = None,
    ipc_type_code: str = None,
    location_code: str = None,
    location_name: str = None,
    admin1_name: str = None,
    admin1_code: str = None,
    admin1_is_unspecified: bool = None,
    location_ref: int = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin2_is_unspecified: bool = None,
    admin1_ref: int = None,
    admin2_ref: int = None,
):
    query = select(FoodSecurityView)

    if ipc_phase_code:
        query = query.where(FoodSecurityView.ipc_phase_code == ipc_phase_code)
    if ipc_type_code:
        query = case_insensitive_filter(query, FoodSecurityView.ipc_type_code, ipc_type_code)

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

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

# pagination_parameters=pagination_parameters,
#         ref_period_parameters=ref_period_parameters,
#         db=db,
#         ipc_phase=ipc_phase,
#         ipc_type=ipc_type,
#         location_code=location_code,
#         location_name=location_name,
#         admin1_name=admin1_name,
#         admin1_code=admin1_code,
#         admin1_is_unspecified=admin1_is_unspecified,
#         location_ref=location_ref,
#         admin2_ref=admin2_ref,
#         admin2_code=admin2_code,
#         admin2_name=admin2_name,
#         admin2_is_unspecified=admin2_is_unspecified,
#         admin1_ref=admin1_ref,


async def food_security_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    ipc_phase: str = None,
    ipc_type: str = None,
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

    if ipc_phase:
        query = query.where(FoodSecurityView.ipc_phase == ipc_phase)
    if ipc_type:
        query = case_insensitive_filter(query, FoodSecurityView.ipc_type, ipc_type)

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

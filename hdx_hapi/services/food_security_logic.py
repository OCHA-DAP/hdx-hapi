from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.food_security_view_dao import food_security_view_list
from hdx_hapi.endpoints.util.util import AdminLevel, CommonEndpointParams, ReferencePeriodParameters
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_food_security_srv(
    ref_period_parameters: ReferencePeriodParameters,
    pagination_parameters: CommonEndpointParams,
    db: AsyncSession,
    ipc_phase: str = None,
    ipc_type: str = None,
    location_code: str = None,
    location_name: str = None,
    admin1_name: str = None,
    admin1_code: str = None,
    location_ref: int = None,
    admin2_ref: int = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin1_ref: int = None,
    admin_level: AdminLevel = None,
):
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await food_security_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        ipc_phase=ipc_phase,
        ipc_type=ipc_type,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin1_is_unspecified=admin1_is_unspecified,
        location_ref=location_ref,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
        admin1_ref=admin1_ref,
    )

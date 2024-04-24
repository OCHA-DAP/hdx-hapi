from datetime import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.food_security_view_dao import food_security_view_list
from hdx_hapi.endpoints.util.util import AdminLevel
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_food_security_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    ipc_phase_code: str = None,
    ipc_type_code: str = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min=None,
    resource_update_date_max=None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
    admin1_name: str = None,
    admin1_code: str = None,
    location_ref: int = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin1_ref: int = None,
    admin_level: AdminLevel = None,
):
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await food_security_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        ipc_phase_code=ipc_phase_code,
        ipc_type_code=ipc_type_code,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
        hapi_replaced_date_min=hapi_replaced_date_min,
        hapi_replaced_date_max=hapi_replaced_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin1_is_unspecified=admin1_is_unspecified,
        location_ref=location_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
        admin1_ref=admin1_ref,
    )

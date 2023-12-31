from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.operational_presence_view_dao import operational_presences_view_list
from hdx_hapi.endpoints.util.util import AdminLevel
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_operational_presences_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    sector_code: str = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min=None,
    resource_update_date_max=None,
    org_acronym: str = None,
    org_name: str = None,
    sector_name: str = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    admin1_name: str = None,
    # admin1_is_unspecified=None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin_level: AdminLevel = None,
    # admin2_is_unspecified=None,
):
    
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await operational_presences_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        sector_code=sector_code, 
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name, 
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code, 
        admin1_name=admin1_name,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code, 
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified 
    )

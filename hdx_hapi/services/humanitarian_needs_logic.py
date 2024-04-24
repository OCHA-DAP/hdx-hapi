from datetime import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.humanitarian_needs_view_dao import humanitarian_needs_view_list
from hdx_hapi.endpoints.util.util import AdminLevel
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_humanitarian_needs_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    gender_code: str = None,
    age_range_code: str = None,
    disabled_marker: bool = None,
    sector_code: str = None,
    sector_name: str = None,
    population_group_code: str = None,
    population_status_code: str = None,
    population: int = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min=None,
    resource_update_date_max=None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    # admin1_name: str = None,
    location_ref: int = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin1_ref: int = None,
    admin_level: AdminLevel = None,
):
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await humanitarian_needs_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        gender_code=gender_code,
        age_range_code=age_range_code,
        disabled_marker=disabled_marker,
        sector_code=sector_code,
        sector_name=sector_name,
        population_group_code=population_group_code,
        population_status_code=population_status_code,
        population=population,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
        hapi_replaced_date_min=hapi_replaced_date_min,
        hapi_replaced_date_max=hapi_replaced_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        # admin1_name=admin1_name,
        admin1_is_unspecified=admin1_is_unspecified,
        location_ref=location_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
        admin1_ref=admin1_ref,
    )

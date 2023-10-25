from datetime import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.population_view_dao import populations_view_list


async def get_populations_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    gender_code: str = None,
    age_range_code: str = None,
    population: int = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min=None,
    resource_update_date_max=None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    admin1_is_unspecified: bool = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin2_is_unspecified: bool = None,
):
    return await populations_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        gender_code=gender_code,
        age_range_code=age_range_code,
        population=population,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
    )

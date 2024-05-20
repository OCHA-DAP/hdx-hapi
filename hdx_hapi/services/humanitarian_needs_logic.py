from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.humanitarian_needs_view_dao import humanitarian_needs_view_list
from hdx_hapi.endpoints.util.util import AdminLevel, PaginationParams
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_humanitarian_needs_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    admin2_ref: int = None,
    gender: str = None,
    age_range: str = None,
    min_age: int = None,
    max_age: int = None,
    disabled_marker: bool = None,
    sector_code: str = None,
    population_group: str = None,
    population_status: str = None,
    population: int = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
    sector_name: str = None,
    location_code: str = None,
    location_name: str = None,
    location_ref: int = None,
    admin1_code: str = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin1_ref: int = None,
    admin_level: AdminLevel = None,
):
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await humanitarian_needs_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        admin2_ref=admin2_ref,
        gender=gender,
        age_range=age_range,
        min_age=min_age,
        max_age=max_age,
        disabled_marker=disabled_marker,
        sector_code=sector_code,
        population_group=population_group,
        population_status=population_status,
        population=population,
        reference_period_start=reference_period_start,
        reference_period_end=reference_period_end,
        sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
        location_ref=location_ref,
        admin1_code=admin1_code,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin1_ref=admin1_ref,
    )

import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import HumanitarianNeedsView
from hdx_hapi.db.dao.util.util import apply_location_admin_filter, apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


async def humanitarian_needs_view_list(
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
):
    query = select(HumanitarianNeedsView)

    if gender:
        query = case_insensitive_filter(query, HumanitarianNeedsView.gender, gender)
    if age_range:
        query = query.where(HumanitarianNeedsView.age_range == age_range)
    if min_age:
        query = query.where(HumanitarianNeedsView.min_age == min_age)
    if max_age:
        query = query.where(HumanitarianNeedsView.max_age == max_age)
    if disabled_marker:
        query = query.where(HumanitarianNeedsView.disabled_marker == disabled_marker)
    if sector_code:
        query = query.where(HumanitarianNeedsView.sector_code.icontains(sector_code))
    if population_group:
        query = query.where(HumanitarianNeedsView.population_group.icontains(population_group))
    if population_status:
        query = query.where(HumanitarianNeedsView.population_status.icontains(population_status))

    if population:
        query = query.where(HumanitarianNeedsView.population == population)

    # reference_period_start
    # reference_period_end

    if sector_name:
        query = query.where(HumanitarianNeedsView.sector_name.icontains(sector_name))

    query = apply_location_admin_filter(
        query,
        HumanitarianNeedsView,
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

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    humanitarian_needs = result.scalars().all()
    return humanitarian_needs

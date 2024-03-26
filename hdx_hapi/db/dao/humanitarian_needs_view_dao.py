import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_humanitarian_needs_view import HumanitarianNeedsView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter


async def humanitarian_needs_view_list(
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
    resource_update_date_min: datetime = None,
    resource_update_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    # admin1_name: str = None,
    admin1_is_unspecified: bool = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin2_is_unspecified: bool = None,
):

    query = select(HumanitarianNeedsView)

    if gender_code:
        query = case_insensitive_filter(query, HumanitarianNeedsView.gender_code, gender_code)
    if age_range_code:
        query = query.where(HumanitarianNeedsView.age_range_code == age_range_code)
    if disabled_marker:
        query = query.where(HumanitarianNeedsView.disabled_marker == disabled_marker)
    if sector_code:
        query = query.where(HumanitarianNeedsView.sector_code.icontains(sector_code))
    if sector_name:
        query = query.where(HumanitarianNeedsView.sector_name.icontains(sector_name))
    if population_group_code:
        query = query.where(HumanitarianNeedsView.population_group_code.icontains(population_group_code))
    if population_status_code:
        query = query.where(HumanitarianNeedsView.population_status_code.icontains(population_status_code))
    if population:
        query = query.where(HumanitarianNeedsView.population == population)
    if dataset_hdx_provider_stub:
        query = case_insensitive_filter(
            query, HumanitarianNeedsView.dataset_hdx_provider_stub, dataset_hdx_provider_stub
        )
    if resource_update_date_min:
        query = query.where(HumanitarianNeedsView.resource_update_date >= resource_update_date_min)
    if resource_update_date_max:
        query = query.where(HumanitarianNeedsView.resource_update_date < resource_update_date_max)
    if location_code:
        query = case_insensitive_filter(query, HumanitarianNeedsView.location_code, location_code)
    if location_name:
        query = query.where(HumanitarianNeedsView.location_name.icontains(location_name))
    if admin1_code:
        query = case_insensitive_filter(query, HumanitarianNeedsView.admin1_code, admin1_code)
    # if admin1_name:
    # query = query.where(HumanitarianNeedsView.admin1_name.icontains(admin1_name))
    if admin1_is_unspecified is not None:
        query = query.where(HumanitarianNeedsView.admin1_is_unspecified == admin1_is_unspecified)
    if admin2_code:
        query = case_insensitive_filter(query, HumanitarianNeedsView.admin2_code, admin2_code)
    if admin2_name:
        query = query.where(HumanitarianNeedsView.admin2_name.icontains(admin2_name))
    if admin2_is_unspecified is not None:
        query = query.where(HumanitarianNeedsView.admin2_is_unspecified == admin2_is_unspecified)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    humanitarian_needs = result.scalars().all()
    return humanitarian_needs

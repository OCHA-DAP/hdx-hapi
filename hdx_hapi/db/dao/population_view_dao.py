import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_population_view import PopulationView
from hdx_hapi.db.dao.util.util import apply_pagination

async def populations_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    gender_code: str = None,
    age_range_code: str = None,
    population: int = None,
    dataset_provider_code: str = None,
    resource_update_date_min: datetime = None,
    resource_update_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
    admin1_code: str = None,
    admin1_is_unspecified: bool = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin2_is_unspecified: bool = None,
):

    query = select(PopulationView)
    if gender_code:
        query = query.where(PopulationView.gender_code == gender_code)
    if age_range_code:
        query = query.where(PopulationView.age_range_code == age_range_code)
    if population:
        query = query.where(PopulationView.population == population)
    if dataset_provider_code:
        query = query.where(PopulationView.dataset_provider_code == dataset_provider_code)
    if resource_update_date_min:
        query = query.where(PopulationView.resource_update_date >= resource_update_date_min)
    if resource_update_date_max:
        query = query.where(PopulationView.resource_update_date <= resource_update_date_max)
    if location_code:
        query = query.where(PopulationView.location_code == location_code)
    if location_name:
        query = query.where(PopulationView.location_name.icontains(location_name))
    if admin1_code:
        query = query.where(PopulationView.admin1_code == admin1_code)
    if admin1_is_unspecified is not None:
        query = query.where(PopulationView.admin1_is_unspecified == admin1_is_unspecified)
    if admin2_code:
        query = query.where(PopulationView.admin2_code == admin2_code)
    if admin2_name:
        query = query.where(PopulationView.admin2_name.icontains(admin2_name))
    if admin2_is_unspecified is not None:
        query = query.where(PopulationView.admin2_is_unspecified == admin2_is_unspecified)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    populations = result.scalars().all()
    return populations
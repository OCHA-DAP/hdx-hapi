import logging
import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_population_view import PopulationView
from hdx_hapi.db.dao.util.util import apply_location_admin_filter, apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


logger = logging.getLogger(__name__)


async def populations_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    gender_code: str = None,
    age_range_code: str = None,
    population: int = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min: datetime = None,
    resource_update_date_max: datetime = None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
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
    logger.info(
        f'populations_view_list called with params: gender_code={gender_code}, age_range_code={age_range_code}, '
        f'population={population}, dataset_hdx_provider_stub={dataset_hdx_provider_stub}, '
        f'resource_update_date_min={resource_update_date_min}, resource_update_date_max={resource_update_date_max}, '
        f'location_code={location_code}, location_name={location_name}, admin1_name={admin1_name}, '
        f'admin1_code={admin1_code}, admin1_is_unspecified={admin1_is_unspecified}, admin2_code={admin2_code}, '
        f'admin2_name={admin2_name}, admin2_is_unspecified={admin2_is_unspecified}'
    )

    query = select(PopulationView)
    if gender_code:
        query = case_insensitive_filter(query, PopulationView.gender_code, gender_code)
    if age_range_code:
        query = query.where(PopulationView.age_range_code == age_range_code)
    if population:
        query = query.where(PopulationView.population == population)
    if dataset_hdx_provider_stub:
        query = case_insensitive_filter(query, PopulationView.dataset_hdx_provider_stub, dataset_hdx_provider_stub)
    if resource_update_date_min:
        query = query.where(PopulationView.resource_update_date >= resource_update_date_min)
    if resource_update_date_max:
        query = query.where(PopulationView.resource_update_date < resource_update_date_max)
    if hapi_updated_date_min:
        query = query.where(PopulationView.hapi_updated_date >= hapi_updated_date_min)
    if hapi_updated_date_max:
        query = query.where(PopulationView.hapi_updated_date < hapi_updated_date_max)
    if hapi_replaced_date_min:
        query = query.where(PopulationView.hapi_replaced_date >= hapi_replaced_date_min)
    if hapi_replaced_date_max:
        query = query.where(PopulationView.hapi_replaced_date < hapi_replaced_date_max)

    query = apply_location_admin_filter(
        query,
        PopulationView,
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

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    populations = result.scalars().all()

    logger.info(f'Retrieved {len(populations)} rows from the database')

    return populations

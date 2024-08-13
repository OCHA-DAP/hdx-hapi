import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hapi_schema.utils.enums import Gender

from hdx_hapi.db.models.views.vat_or_view import PopulationView
from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
    case_insensitive_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def populations_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    location_ref: Optional[int] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
) -> Sequence[PopulationView]:
    logger.info(
        f'populations_view_list called with params: gender={gender}, age_range={age_range}, '
        f'population_min={population_min}, population_max={population_max},'
        f'location_code={location_code}, location_name={location_name}, admin1_name={admin1_name}, '
        f'admin1_code={admin1_code}, admin1_is_unspecified={admin1_is_unspecified}, admin2_code={admin2_code}, '
        f'admin2_name={admin2_name}, admin2_is_unspecified={admin2_is_unspecified}'
        f'ref_period_parameters={ref_period_parameters}'
    )

    query = select(PopulationView)
    if gender:
        query = query.where(PopulationView.gender == gender)
    if age_range:
        query = case_insensitive_filter(query, PopulationView.age_range, age_range)
    if population_min:
        query = query.where(PopulationView.population >= population_min)
    if population_max:
        query = query.where(PopulationView.population < population_max)
    query = apply_location_admin_filter(
        query,
        PopulationView,
        location_ref,
        location_code,
        location_name,
        has_hrp,
        in_gho,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, PopulationView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(PopulationView.location_code.asc())

    logger.info(f'Executing SQL query: {query}')

    result = await db.execute(query)
    populations = result.scalars().all()

    logger.info(f'Retrieved {len(populations)} rows from the database')

    return populations

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
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def populations_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[PopulationView]:
    logger.info(
        f'populations_view_list called with params: gender={gender}, age_range={age_range}, '
        f'population_min={population_min}, population_max={population_max},'
        f'location_name={common_location_params.location_name}, '
        f'admin1_code={common_location_params.admin1_code}, admin1_name={common_location_params.admin1_name}, '
        f'admin2_code={common_location_params.admin2_code}, admin2_name={common_location_params.admin2_name}, '
        f'ref_period_parameters={ref_period_parameters}, admin_level={common_location_params.admin_level}, '
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
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, PopulationView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(PopulationView.admin2_ref, PopulationView.gender, PopulationView.age_range)

    logger.info(f'Executing SQL query: {query}')

    result = await db.execute(query)
    populations = result.scalars().all()

    logger.info(f'Retrieved {len(populations)} rows from the database')

    return populations

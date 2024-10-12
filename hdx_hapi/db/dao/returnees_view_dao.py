import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hapi_schema.utils.enums import PopulationGroup, Gender

from hdx_hapi.db.models.views.vat_or_view import ReturneesView
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters

logger = logging.getLogger(__name__)


async def returnees_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    population_group: Optional[PopulationGroup] = None,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    origin_location_code: Optional[str] = None,
    origin_location_name: Optional[str] = None,
    origin_has_hrp: Optional[bool] = None,
    origin_in_gho: Optional[bool] = None,
    asylum_location_code: Optional[str] = None,
    asylum_location_name: Optional[str] = None,
    asylum_has_hrp: Optional[bool] = None,
    asylum_in_gho: Optional[bool] = None,
) -> Sequence[ReturneesView]:
    query = select(ReturneesView)

    # Query statements
    if population_group:
        query = query.where(ReturneesView.population_group == population_group)
    if gender:
        query = query.where(ReturneesView.gender == gender)
    if age_range:
        query = case_insensitive_filter(query, ReturneesView.age_range, age_range)
    if min_age:
        query = query.where(ReturneesView.min_age == min_age)
    if max_age:
        query = query.where(ReturneesView.max_age == max_age)
    if origin_location_code:
        query = case_insensitive_filter(query, ReturneesView.origin_location_code, origin_location_code)
    if origin_location_name:
        query = query.where(ReturneesView.origin_location_name.icontains(origin_location_name))
    if origin_has_hrp:
        query = query.where(ReturneesView.origin_has_hrp == origin_has_hrp)
    if origin_in_gho:
        query = query.where(ReturneesView.origin_in_gho == origin_in_gho)
    if asylum_location_code:
        query = case_insensitive_filter(query, ReturneesView.asylum_location_code, asylum_location_code)
    if asylum_location_name:
        query = query.where(ReturneesView.asylum_location_name.icontains(asylum_location_name))
    if asylum_has_hrp:
        query = query.where(ReturneesView.asylum_has_hrp == asylum_has_hrp)
    if asylum_in_gho:
        query = query.where(ReturneesView.asylum_in_gho == asylum_in_gho)

    query = apply_reference_period_filter(query, ref_period_parameters, ReturneesView)
    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        ReturneesView.origin_location_ref,
        ReturneesView.asylum_location_ref,
        ReturneesView.population_group,
        ReturneesView.gender,
        ReturneesView.age_range,
        ReturneesView.reference_period_start,
    )

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    returnees = result.scalars().all()

    logger.info(f'Retrieved {len(returnees)} rows from the database')

    return returnees

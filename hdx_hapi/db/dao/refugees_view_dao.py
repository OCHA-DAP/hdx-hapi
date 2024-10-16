from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import RefugeesView
from hdx_hapi.db.dao.util.util import (
    apply_pagination,
    apply_reference_period_filter,
    case_insensitive_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters
from hapi_schema.utils.enums import Gender, PopulationGroup


async def refugees_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    population_group: Optional[PopulationGroup] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    origin_location_code: Optional[str] = None,
    origin_location_name: Optional[str] = None,
    origin_has_hrp: Optional[bool] = None,
    origin_in_gho: Optional[bool] = None,
    asylum_location_code: Optional[str] = None,
    asylum_location_name: Optional[str] = None,
    asylum_has_hrp: Optional[bool] = None,
    asylum_in_gho: Optional[bool] = None,
):
    query = select(RefugeesView)

    if gender:
        query = query.where(RefugeesView.gender == gender)
    if age_range:
        query = query.where(RefugeesView.age_range == age_range)
    if population_group:
        query = query.where(RefugeesView.population_group == population_group)
    if population_min:
        query = query.where(RefugeesView.population >= population_min)
    if population_max:
        query = query.where(RefugeesView.population < population_max)
    if origin_location_code:
        query = case_insensitive_filter(query, RefugeesView.origin_location_code, origin_location_code)
    if origin_location_name:
        query = query.where(RefugeesView.origin_location_name.icontains(origin_location_name))
    if asylum_location_code:
        query = case_insensitive_filter(query, RefugeesView.asylum_location_code, asylum_location_code)
    if asylum_location_name:
        query = query.where(RefugeesView.asylum_location_name.icontains(asylum_location_name))
    if origin_has_hrp is not None:
        query = query.where(RefugeesView.origin_has_hrp == origin_has_hrp)
    if origin_in_gho is not None:
        query = query.where(RefugeesView.origin_in_gho == origin_in_gho)
    if asylum_has_hrp is not None:
        query = query.where(RefugeesView.asylum_has_hrp == asylum_has_hrp)
    if asylum_in_gho is not None:
        query = query.where(RefugeesView.asylum_in_gho == asylum_in_gho)

    query = apply_reference_period_filter(query, ref_period_parameters, RefugeesView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        RefugeesView.origin_location_ref,
        RefugeesView.asylum_location_ref,
        RefugeesView.population_group,
        RefugeesView.gender,
        RefugeesView.age_range,
        RefugeesView.reference_period_start,
    )

    result = await db.execute(query)
    refugees = result.scalars().all()
    return refugees

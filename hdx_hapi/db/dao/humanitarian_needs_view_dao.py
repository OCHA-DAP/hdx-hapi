from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import HumanitarianNeedsView
from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
)
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams, ReferencePeriodParameters
from hapi_schema.utils.enums import PopulationStatus


async def humanitarian_needs_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    category: Optional[str] = None,
    sector_code: Optional[str] = None,
    population_status: Optional[PopulationStatus] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    sector_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[HumanitarianNeedsView]:
    query = select(HumanitarianNeedsView)

    if category:
        query = query.where(HumanitarianNeedsView.category.icontains(category))
    if sector_code:
        query = query.where(HumanitarianNeedsView.sector_code.icontains(sector_code))
    if population_status:
        query = query.where(HumanitarianNeedsView.population_status == population_status)

    if population_min:
        query = query.where(HumanitarianNeedsView.population >= population_min)
    if population_max:
        query = query.where(HumanitarianNeedsView.population < population_max)
    if sector_name:
        query = query.where(HumanitarianNeedsView.sector_name.icontains(sector_name))

    query = apply_location_admin_filter(
        query,
        HumanitarianNeedsView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, HumanitarianNeedsView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        HumanitarianNeedsView.admin2_ref,
        HumanitarianNeedsView.category,
        HumanitarianNeedsView.sector_code,
        HumanitarianNeedsView.population_status,
        HumanitarianNeedsView.reference_period_start,
    )

    result = await db.execute(query)
    humanitarian_needs = result.scalars().all()
    return humanitarian_needs

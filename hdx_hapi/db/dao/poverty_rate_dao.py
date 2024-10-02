from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import PovertyRateView
from hdx_hapi.db.dao.util.util import (
    apply_pagination,
    apply_reference_period_filter,
    case_insensitive_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def poverty_rates_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    mpi_min: Optional[float] = None,
    mpi_max: Optional[float] = None,
    location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    provider_admin1_name: Optional[str] = None,
):
    query = select(PovertyRateView)

    if mpi_min:
        query = query.where(PovertyRateView.mpi >= mpi_min)
    if mpi_max:
        query = query.where(PovertyRateView.mpi < mpi_max)

    if has_hrp is not None:
        query = query.where(PovertyRateView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(PovertyRateView.in_gho == in_gho)

    if location_ref:
        query = query.where(PovertyRateView.location_ref == location_ref)
    if location_code:
        query = case_insensitive_filter(query, PovertyRateView.location_code, location_code)
    if location_name:
        query = query.where(PovertyRateView.location_name.icontains(location_name))
    if provider_admin1_name:
        query = query.where(PovertyRateView.provider_admin1_name.icontains(provider_admin1_name))

    query = apply_reference_period_filter(query, ref_period_parameters, PovertyRateView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        PovertyRateView.admin1_ref, PovertyRateView.provider_admin1_name, PovertyRateView.reference_period_start
    )

    result = await db.execute(query)
    poverty_rates = result.scalars().all()
    return poverty_rates

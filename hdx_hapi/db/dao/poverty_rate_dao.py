from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import PovertyRateView
from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def poverty_rates_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    mpi_min: Optional[float] = None,
    mpi_max: Optional[float] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_name: Optional[str] = None,
):
    query = select(PovertyRateView)

    if mpi_min:
        query = query.where(PovertyRateView.mpi >= mpi_min)
    if mpi_max:
        query = query.where(PovertyRateView.mpi < mpi_max)

    query = apply_location_admin_filter(
        query,
        PovertyRateView,
        None,
        location_code,
        location_name,
        has_hrp,
        in_gho,
        None,
        None,
        admin1_name,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, PovertyRateView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        PovertyRateView.admin1_ref, PovertyRateView.admin1_name, PovertyRateView.reference_period_start
    )

    result = await db.execute(query)
    poverty_rates = result.scalars().all()
    return poverty_rates

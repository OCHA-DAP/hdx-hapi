import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import PovertyRateView
from hdx_hapi.db.dao.util.util import (
    apply_date_range_filter,
    apply_location_admin_1_filter,
    apply_pagination,
    apply_reference_period_filter,
)
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationAdm1Parameters,
    PaginationParams,
    ReferencePeriodParameters,
)

logger = logging.getLogger(__name__)


async def poverty_rates_view_list(
    pagination_parameters: PaginationParams,
    common_date_range_params: CommonDateRangeParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationAdm1Parameters,
    db: AsyncSession,
    mpi_min: Optional[float] = None,
    mpi_max: Optional[float] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[PovertyRateView]:
    logger.info(
        f'location_name={common_location_params.location_name}, '
        f'admin1_code={common_location_params.admin1_code}, admin1_name={common_location_params.admin1_name}, '
        f'ref_period_parameters={ref_period_parameters}, admin_level={common_location_params.admin_level}, '
    )
    query = select(PovertyRateView)

    if mpi_min:
        query = query.where(PovertyRateView.mpi >= mpi_min)
    if mpi_max:
        query = query.where(PovertyRateView.mpi < mpi_max)

    if has_hrp is not None:
        query = query.where(PovertyRateView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(PovertyRateView.in_gho == in_gho)

    query = apply_date_range_filter(
        query,
        PovertyRateView,
        common_date_range_params,
    )

    query = apply_location_admin_1_filter(
        query,
        PovertyRateView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, PovertyRateView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        PovertyRateView.admin1_ref, PovertyRateView.provider_admin1_name, PovertyRateView.reference_period_start
    )

    result = await db.execute(query)
    poverty_rates = result.scalars().all()
    return poverty_rates

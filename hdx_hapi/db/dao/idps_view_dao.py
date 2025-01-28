import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import IdpsView
from hdx_hapi.db.dao.util.util import (
    apply_date_range_filter,
    apply_pagination,
    apply_reference_period_filter,
    apply_location_admin_filter,
)
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationParameters,
    PaginationParams,
    ReferencePeriodParameters,
)

logger = logging.getLogger(__name__)


async def idps_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_date_range_params: CommonDateRangeParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[IdpsView]:
    query = select(IdpsView)

    if has_hrp is not None:
        query = query.where(IdpsView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(IdpsView.in_gho == in_gho)

    query = apply_date_range_filter(
        query,
        IdpsView,
        common_date_range_params,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, IdpsView)
    query = apply_pagination(query, pagination_parameters)
    query = apply_location_admin_filter(
        query,
        IdpsView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = query.order_by(
        IdpsView.admin2_ref,
        IdpsView.assessment_type,
        IdpsView.reporting_round,
        IdpsView.operation,
        IdpsView.population,
        IdpsView.reference_period_start,
        IdpsView.reference_period_end,
    )

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    idps = result.scalars().all()

    logger.info(f'Retrieved {len(idps)} rows from the database')

    return idps

import logging
from typing import Optional, Sequence

from hapi_schema.utils.enums import EventType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import ConflictEventView
from hdx_hapi.db.dao.util.util import (
    apply_date_range_filter,
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
)
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationParameters,
    PaginationParams,
    ReferencePeriodParameters,
)


logger = logging.getLogger(__name__)


async def conflict_event_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_date_range_params: CommonDateRangeParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    event_type: Optional[EventType] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[ConflictEventView]:
    query = select(ConflictEventView)
    if event_type:
        query = query.where(ConflictEventView.event_type == event_type)

    query = apply_date_range_filter(
        query,
        ConflictEventView,
        common_date_range_params,
    )

    query = apply_location_admin_filter(
        query,
        ConflictEventView,
        common_location_params,
        has_hrp,
        in_gho,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, ConflictEventView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        ConflictEventView.admin2_ref, ConflictEventView.event_type, ConflictEventView.reference_period_start
    )

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    conflict_events = result.scalars().all()

    logger.info(f'Retrieved {len(conflict_events)} rows from the database')

    return conflict_events

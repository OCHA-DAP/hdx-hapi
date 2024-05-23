import logging
from typing import Optional, Sequence

from hapi_schema.utils.enums import EventType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import ConflictEventView
from hdx_hapi.db.dao.util.util import (
    apply_location_admin_filter,
    apply_pagination,
    apply_reference_period_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def conflict_event_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    event_type: Optional[EventType] = None,
    location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
) -> Sequence[ConflictEventView]:
    query = select(ConflictEventView)
    if event_type:
        query = query.where(ConflictEventView.event_type == event_type)

    query = apply_location_admin_filter(
        query,
        ConflictEventView,
        location_ref,
        location_code,
        location_name,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
    )

    query = apply_reference_period_filter(query, ref_period_parameters, ConflictEventView)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    conflict_events = result.scalars().all()

    logger.info(f'Retrieved {len(conflict_events)} rows from the database')

    return conflict_events

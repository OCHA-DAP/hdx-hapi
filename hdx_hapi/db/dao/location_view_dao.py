import logging

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import LocationView
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters

logger = logging.getLogger(__name__)


async def locations_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    id: Optional[int] = None,
    code: Optional[str] = None,
    name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    logger.info(f'location_view_list called with params: code={code}, name={name}, has_hrp={has_hrp}, in_gho={in_gho}')

    query = select(LocationView)
    if id:
        query = query.where(LocationView.id == id)
    if code:
        query = case_insensitive_filter(query, LocationView.code, code)
    if name:
        query = query.where(LocationView.name.icontains(name))
    if has_hrp is not None:
        query = query.where(LocationView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(LocationView.in_gho == in_gho)

    query = apply_reference_period_filter(query, ref_period_parameters, LocationView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(LocationView.id)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    locations = result.scalars().all()

    logger.info(f'Retrieved {len(locations)} rows from the database')

    return locations

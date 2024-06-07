import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import LocationView
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters

logger = logging.getLogger(__name__)


async def locations_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    id: int = None,
    code: str = None,
    name: str = None,
):
    logger.info(f'orgs_view_list called with params: code={code}, name={name}')

    query = select(LocationView)
    if id:
        query = query.where(LocationView.id == id)
    if code:
        query = case_insensitive_filter(query, LocationView.code, code)
    if name:
        query = query.where(LocationView.name.icontains(name))

    query = apply_reference_period_filter(query, ref_period_parameters, LocationView)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    locations = result.scalars().all()

    logger.info(f'Retrieved {len(locations)} rows from the database')

    return locations

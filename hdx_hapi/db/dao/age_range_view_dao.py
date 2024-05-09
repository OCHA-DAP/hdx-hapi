import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_age_range_view import AgeRangeView
from hdx_hapi.db.dao.util.util import apply_pagination
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def age_ranges_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
):
    logger.info(f'age_ranges_view_list called with params: code={code}')

    query = select(AgeRangeView)
    if code:
        query = query.where(AgeRangeView.code == code)
    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    age_ranges = result.scalars().all()

    logger.info(f'Retrieved {len(age_ranges)} rows from the database')

    return age_ranges

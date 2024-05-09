import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_gender_view import GenderView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def genders_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
    description: str = None,
):
    logger.info(f'genders_view_list called with params: code={code}, description={description}')

    query = select(GenderView)
    if code:
        query = case_insensitive_filter(query, GenderView.code, code)
    if description:
        query = query.where(GenderView.description.icontains(description))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    genders = result.scalars().all()

    logger.info(f'Retrieved {len(genders)} rows from the database')

    return genders

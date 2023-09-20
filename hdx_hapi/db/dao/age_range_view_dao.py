import logging
from re import A

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_age_range_view import AgeRangeView
from hdx_hapi.db.dao.util.util import apply_pagination

logger = logging.getLogger(__name__)

async def age_ranges_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    age_min: int = None,
    age_max: int = None,
):

    logger.info(f'age_ranges_view_list called with params: code={code}, age_min={age_min}, age_max={age_max}')

    query = select(AgeRangeView)
    if code:
        query = query.where(AgeRangeView.code == code)
    if age_min is not None:
        query = query.where(AgeRangeView.age_min >= age_min)
    if age_max is not None:
        query = query.where(AgeRangeView.age_max <= age_max)
    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    age_ranges = result.scalars().all()

    logger.info(f'Retrieved {len(age_ranges)} rows from the database')

    return age_ranges
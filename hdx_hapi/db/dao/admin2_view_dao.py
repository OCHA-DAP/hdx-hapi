import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_admin2_view import Admin2View
from hdx_hapi.db.dao.util.util import apply_pagination

from datetime import datetime

logger = logging.getLogger(__name__)

async def admin2_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    is_unspecified: bool = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):

    logger.info(f'admin2_view_list called with params: code={code}, name={name}, is_unspecified={is_unspecified}, reference_period_start={reference_period_start}, reference_period_end={reference_period_end}')

    query = select(Admin2View)
    if code:
        query = query.where(Admin2View.code == code)
    if name:
        query = query.where(Admin2View.name.icontains(name))
    if is_unspecified is not None:
        query = query.where(Admin2View.is_unspecified == is_unspecified)
    if reference_period_start:
        query = query.where(Admin2View.reference_period_start >= reference_period_start)
    if reference_period_end:
        query = query.where(Admin2View.reference_period_end <= reference_period_end)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    admin2_data = result.scalars().all()

    logger.info(f'Retrieved {len(admin2_data)} rows from the database')

    return admin2_data
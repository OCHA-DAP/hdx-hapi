import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_sector_view import SectorView
from hdx_hapi.db.dao.util.util import apply_pagination

from datetime import datetime

logger = logging.getLogger(__name__)

async def sectors_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):

    logger.info(f'sectors_view_list called with params: code={code}, name={name}, reference_period_start={reference_period_start}, reference_period_end={reference_period_end}')

    query = select(SectorView)
    if code:
        query = query.where(SectorView.code == code)
    if name:
        query = query.where(SectorView.name.icontains(name))
    if reference_period_start:
        query = query.where(SectorView.reference_period_start >= reference_period_start)
    if reference_period_end:
        query = query.where(SectorView.reference_period_end <= reference_period_end)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    sectors = result.scalars().all()

    logger.info(f'Retrieved {len(sectors)} rows from the database')

    return sectors
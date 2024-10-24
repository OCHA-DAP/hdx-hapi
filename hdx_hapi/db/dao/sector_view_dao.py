import logging

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import SectorView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


logger = logging.getLogger(__name__)


async def sectors_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    name: Optional[str] = None,
):
    logger.info(f'sectors_view_list called with params: code={code}, name={name}')

    query = select(SectorView)
    if code:
        query = case_insensitive_filter(query, SectorView.code, code)
    if name:
        query = query.where(SectorView.name.icontains(name))

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(SectorView.code)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    sectors = result.scalars().all()

    logger.info(f'Retrieved {len(sectors)} rows from the database')

    return sectors

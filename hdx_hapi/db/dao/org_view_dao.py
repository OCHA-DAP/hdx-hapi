import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_org_view import OrgView
from hdx_hapi.db.dao.util.util import apply_pagination

from datetime import datetime

logger = logging.getLogger(__name__)

async def orgs_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    acronym: str = None,
    name: str = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):

    logger.info(f'orgs_view_list called with params: acronym={acronym}, name={name}, reference_period_start={reference_period_start}, reference_period_end={reference_period_end}')

    query = select(OrgView)
    if acronym:
        query = query.where(OrgView.acronym == acronym)
    if name:
        query = query.where(OrgView.name.icontains(name))
    if reference_period_start:
        query = query.where(OrgView.reference_period_start >= reference_period_start)
    if reference_period_end:
        query = query.where(OrgView.reference_period_end <= reference_period_end)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    orgs = result.scalars().all()

    logger.info(f'Retrieved {len(orgs)} rows from the database')

    return orgs
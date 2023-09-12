from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_org_view import OrgView
from hdx_hapi.db.dao.util.util import apply_pagination

from datetime import datetime

async def orgs_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    acronym: str = None,
    name: str = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):

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

    result = await db.execute(query)
    locations = result.scalars().all()
    return locations
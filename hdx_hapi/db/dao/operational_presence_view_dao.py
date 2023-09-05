from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.dboperationalpresenceview import OperationalPresenceView
from hdx_hapi.db.dao.util.util import apply_pagination

async def operational_presences_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    org_ref: int = None,
    location_name: str = None,
):

    query = select(OperationalPresenceView)
    if org_ref:
        query = query.where(OperationalPresenceView.org_ref == org_ref)
    if location_name:
        query = query.where(OperationalPresenceView.location_name == location_name)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    operational_presences = result.scalars().all()
    return operational_presences
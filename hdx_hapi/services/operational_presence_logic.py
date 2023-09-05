
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.dboperationalpresenceview import OperationalPresenceView

async def get_operational_presences_srv(
    db: AsyncSession,
    org_ref: int = None,
    location_name: str = None,
):

    query = select(OperationalPresenceView)
    if org_ref:
        query = query.where(OperationalPresenceView.org_ref == org_ref)
    if location_name:
        query = query.where(OperationalPresenceView.location_name == location_name)

    result = await db.execute(query)
    operational_presences = result.scalars().all()
    return operational_presences
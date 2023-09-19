import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.dboperationalpresenceview import OperationalPresenceView
from hdx_hapi.db.dao.util.util import apply_pagination


logger = logging.getLogger(__name__)

async def operational_presences_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    org_ref: int = None,
    location_name: str = None,
):

    logger.info(f'operational_presences_view_list called with params: org_ref={org_ref}, location_name={location_name}')

    query = select(OperationalPresenceView)
    if org_ref:
        query = query.where(OperationalPresenceView.org_ref == org_ref)
    if location_name:
        query = query.where(OperationalPresenceView.location_name == location_name)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    operational_presences = result.scalars().all()

    logger.info(f'Retrieved {len(operational_presences)} rows from the database')

    return operational_presences
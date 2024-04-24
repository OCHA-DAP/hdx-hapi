from datetime import datetime
import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_location_view import LocationView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter

logger = logging.getLogger(__name__)


async def locations_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
):

    logger.info(f'orgs_view_list called with params: code={code}, name={name}')

    query = select(LocationView)
    if code:
        query = case_insensitive_filter(query, LocationView.code, code)
    if name:
        query = query.where(LocationView.name.icontains(name))
    if hapi_updated_date_min:
        query = query.where(LocationView.hapi_updated_date >= hapi_updated_date_min)
    if hapi_updated_date_max:
        query = query.where(LocationView.hapi_updated_date < hapi_updated_date_max)
    if hapi_replaced_date_min:
        query = query.where(LocationView.hapi_replaced_date >= hapi_replaced_date_min)
    if hapi_replaced_date_max:
        query = query.where(LocationView.hapi_replaced_date < hapi_replaced_date_max)

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    locations = result.scalars().all()

    logger.info(f'Retrieved {len(locations)} rows from the database')

    return locations

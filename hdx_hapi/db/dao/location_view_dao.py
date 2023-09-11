from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_location_view import LocationView
from hdx_hapi.db.dao.util.util import apply_pagination

from datetime import datetime
import dateutil.parser

async def locations_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    reference_period_start: datetime = None,
    reference_period_end: datetime = None,
):

    query = select(LocationView)
    if code:
        query = query.where(LocationView.code == code)
    if name:
        query = query.where(LocationView.name.icontains(name))
    if reference_period_start:
        start_date = dateutil.parser.parse(reference_period_start)
        query = query.where(LocationView.reference_period_start >= start_date)
    if reference_period_end:
        end_date = dateutil.parser.parse(reference_period_end)
        query = query.where(LocationView.reference_period_end <= end_date)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    locations = result.scalars().all()
    return locations
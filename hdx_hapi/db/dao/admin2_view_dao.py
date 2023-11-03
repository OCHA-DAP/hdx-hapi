import logging

from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_admin2_view import Admin2View
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter

from datetime import datetime

logger = logging.getLogger(__name__)

async def admin2_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    admin1_code: str = None,
    admin1_name: str = None,
    location_code: str = None,
    location_name: str = None,
):

    logger.info(f'admin2_view_list called with params: code={code}, name={name}, admin1_code={admin1_code}, admin1_name={admin1_name}, location_code={location_code}, location_name={location_name}')

    query = select(Admin2View)
    if True:
        # TODO: implement debug=True to show unspecified values
        query = query.where(Admin2View.is_unspecified==False)
    if code:
        query = case_insensitive_filter(query, Admin2View.code, code)
    if name:
        query = query.where(Admin2View.name.icontains(name))
    if admin1_code:
        query = case_insensitive_filter(query, Admin2View.admin1_code, admin1_code)
    if admin1_name:
        query = query.where(Admin2View.admin1_name.icontains(admin1_name))
    if location_code:
        query = case_insensitive_filter(query, Admin2View.location_code, location_code)
    if location_name:
        query = query.where(Admin2View.location_name.icontains(location_name))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    admin2_data = result.scalars().all()

    logger.info(f'Retrieved {len(admin2_data)} rows from the database')

    return admin2_data
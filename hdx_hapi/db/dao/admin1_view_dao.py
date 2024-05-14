import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.all_views import Admin1View
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


logger = logging.getLogger(__name__)


async def admin1_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    location_code: str = None,
    location_name: str = None,
):
    logger.info(
        f'admin1_view_list called with params: code={code}, name={name}, '
        f'location_code={location_code}, location_name={location_name}'
    )

    query = select(Admin1View)
    if True:
        # TODO: implement debug=True to show unspecified values
        query = query.where(Admin1View.is_unspecified == False)
    if code:
        query = case_insensitive_filter(query, Admin1View.code, code)
    if name:
        query = query.where(Admin1View.name.icontains(name))
    if location_code:
        query = case_insensitive_filter(query, Admin1View.location_code, location_code)
    if location_name:
        query = query.where(Admin1View.location_name.icontains(location_name))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    admin1_data = result.scalars().all()

    logger.info(f'Retrieved {len(admin1_data)} rows from the database')

    return admin1_data

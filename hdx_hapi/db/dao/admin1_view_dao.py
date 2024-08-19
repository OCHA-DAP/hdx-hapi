import logging

from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import Admin1View
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def admin1_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    id: Optional[int] = None,
    location_ref: Optional[int] = None,
    code: Optional[str] = None,
    name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
):
    logger.info(
        f'admin1_view_list called with params: code={code}, name={name}, '
        f'location_code={location_code}, location_name={location_name}'
    )

    query = select(Admin1View)
    if True:
        # TODO: implement debug=True to show unspecified values
        query = query.where(Admin1View.is_unspecified == False)
    if id:
        query = query.where(Admin1View.id == id)
    if location_ref:
        query = query.where(Admin1View.location_ref == location_ref)
    if code:
        query = case_insensitive_filter(query, Admin1View.code, code)
    if name:
        query = query.where(Admin1View.name.icontains(name))
    if location_code:
        query = case_insensitive_filter(query, Admin1View.location_code, location_code)
    if location_name:
        query = query.where(Admin1View.location_name.icontains(location_name))

    query = apply_reference_period_filter(query, ref_period_parameters, Admin1View)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(Admin1View.id)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    admin1_data = result.scalars().all()

    logger.info(f'Retrieved {len(admin1_data)} rows from the database')

    return admin1_data

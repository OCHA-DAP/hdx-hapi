import logging
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import Admin2View
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def admin2_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    id: Optional[int] = None,
    admin1_ref: Optional[int] = None,
    location_ref: Optional[int] = None,
    code: Optional[str] = None,
    name: Optional[str] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
):
    logger.info(
        f'admin2_view_list called with params: code={code}, name={name}, admin1_code={admin1_code}, '
        f'admin1_name={admin1_name}, location_code={location_code}, location_name={location_name}'
    )

    query = select(Admin2View)
    if True:
        # TODO: implement debug=True to show unspecified values
        query = query.where(Admin2View.is_unspecified == False)
    if id:
        query = query.where(Admin2View.id == id)
    if admin1_ref:
        query = query.where(Admin2View.admin1_ref == admin1_ref)
    if location_ref:
        query = query.where(Admin2View.location_ref == location_ref)
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

    query = apply_reference_period_filter(query, ref_period_parameters, Admin2View)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(Admin2View.id)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    admin2_data = result.scalars().all()

    logger.info(f'Retrieved {len(admin2_data)} rows from the database')

    return admin2_data

import datetime
import logging
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import AvailabilityView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def availability_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    location_name: Optional[str] = None,
    location_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_code: Optional[str] = None,
    hapi_updated_date_min: Optional[datetime.datetime] = None,
    hapi_updated_date_max: Optional[datetime.datetime] = None,
):
    logger.info(f'availability_view_list called with params: {locals()}')

    query = select(AvailabilityView)
    if category:
        query = case_insensitive_filter(query, AvailabilityView.category, category)
    if subcategory:
        query = case_insensitive_filter(query, AvailabilityView.subcategory, subcategory)

    if location_code:
        query = case_insensitive_filter(query, AvailabilityView.location_code, location_code)
    if location_name:
        query = query.where(AvailabilityView.location_name.icontains(location_name))
    if admin1_code:
        query = case_insensitive_filter(query, AvailabilityView.admin1_code, admin1_code)
    if admin1_name:
        query = query.where(AvailabilityView.admin1_name.icontains(admin1_name))
    if admin2_code:
        query = case_insensitive_filter(query, AvailabilityView.admin2_code, admin2_code)
    if admin2_name:
        query = query.where(AvailabilityView.admin2_name.icontains(admin2_name))
    if hapi_updated_date_min:
        query = query.where(AvailabilityView.hapi_updated_date >= hapi_updated_date_min)
    if hapi_updated_date_max:
        query = query.where(AvailabilityView.hapi_updated_date < hapi_updated_date_max)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(
        AvailabilityView.category,
        AvailabilityView.subcategory,
        AvailabilityView.location_name,
        AvailabilityView.location_code,
        AvailabilityView.admin1_name,
        AvailabilityView.admin1_code,
        AvailabilityView.admin2_name,
        AvailabilityView.admin2_code,
    )

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    availabilities = result.scalars().all()

    logger.info(f'Retrieved {len(availabilities)} rows from the database')

    return availabilities

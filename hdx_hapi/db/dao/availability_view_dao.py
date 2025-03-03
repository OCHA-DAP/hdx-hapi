import datetime
import logging
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select, select, or_
from sqlalchemy.orm import Mapped

from hdx_hapi.db.models.views.vat_or_view import AvailabilityView
from hdx_hapi.db.dao.util.util import apply_location_admin_filter, apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams

logger = logging.getLogger(__name__)
_UNSPECIFIED = 'UNSPECIFIED'


async def availability_view_list(
    pagination_parameters: PaginationParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    hapi_updated_date_min: Optional[datetime.datetime | datetime.date] = None,
    hapi_updated_date_max: Optional[datetime.datetime | datetime.date] = None,
):
    logger.info(f'availability_view_list called with params: {locals()}')

    query = select(AvailabilityView)
    if category:
        query = case_insensitive_filter(query, AvailabilityView.category, category)
    if subcategory:
        query = case_insensitive_filter(query, AvailabilityView.subcategory, subcategory)

    query = apply_location_admin_filter(
        query,
        AvailabilityView,
        common_location_params,
    )

    if hapi_updated_date_min:
        query = query.where(AvailabilityView.hapi_updated_date >= hapi_updated_date_min)
    if hapi_updated_date_max:
        query = query.where(AvailabilityView.hapi_updated_date < hapi_updated_date_max)

    # Admin level filtering. Filtering by admin level is handled differently for the data availability table
    # beause we don't have the adminX_is_unspecified fields.
    # if admin_level == AdminLevel.ZERO:
    #     query = filter_is_unspecified(query, AvailabilityView.admin1_name)
    #     query = filter_is_unspecified(query, AvailabilityView.admin2_name)
    # elif admin_level == AdminLevel.ONE:
    #     query = filter_is_unspecified(query, AvailabilityView.admin1_name, negate=True)
    #     query = filter_is_unspecified(query, AvailabilityView.admin2_name)
    # elif admin_level == AdminLevel.TWO:
    #     query = filter_is_unspecified(query, AvailabilityView.admin1_name, negate=True)
    #     query = filter_is_unspecified(query, AvailabilityView.admin2_name, negate=True)

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


def filter_is_unspecified(query: Select, column: Mapped[str], negate=False) -> Select:
    or_clause = or_(column == '', column.is_(None), column.ilike(_UNSPECIFIED))
    if negate:
        return query.where(~or_clause)
    else:
        return query.where(or_clause)

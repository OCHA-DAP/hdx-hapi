import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import IdpsView
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters

logger = logging.getLogger(__name__)


async def idps_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    admin2_ref: Optional[int] = None,
    # provider_admin1_name: Optional[str] = None,
    # provider_admin2_name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
) -> Sequence[IdpsView]:
    query = select(IdpsView)

    # Query statements
    if admin2_ref:
        query = query.where(IdpsView.admin2_ref == admin2_ref)
    # if provider_admin1_name:
    #     query = query.where(IdpsView.provider_admin1_name.icontains(provider_admin1_name))
    # if provider_admin2_name:
    #     query = query.where(IdpsView.provider_admin2_name.icontains(provider_admin2_name))
    if location_code:
        query = case_insensitive_filter(query, IdpsView.location_code, location_code)
    if location_name:
        query = query.where(IdpsView.location_name.icontains(location_name))
    if has_hrp is not None:
        query = query.where(IdpsView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(IdpsView.in_gho == in_gho)
    if admin1_code:
        query = case_insensitive_filter(query, IdpsView.admin1_code, admin1_code)
    if admin1_name:
        query = query.where(IdpsView.admin1_name.icontains(admin1_name))
    if admin2_code:
        query = case_insensitive_filter(query, IdpsView.admin2_code, admin2_code)
    if admin2_name:
        query = query.where(IdpsView.admin2_name.icontains(admin2_name))

    query = apply_reference_period_filter(query, ref_period_parameters, IdpsView)
    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    idps = result.scalars().all()

    logger.info(f'Retrieved {len(idps)} rows from the database')

    return idps

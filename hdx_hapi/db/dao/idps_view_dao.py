import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import IdpsView
from hdx_hapi.db.dao.util.util import (
    apply_pagination,
    apply_reference_period_filter,
    case_insensitive_filter,
    apply_location_admin_filter,
)
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters

logger = logging.getLogger(__name__)


async def idps_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    admin1_is_unspecified: Optional[bool] = None,
    admin2_is_unspecified: Optional[bool] = None,
    # provider_admin1_name: Optional[str] = None,
    # provider_admin2_name: Optional[str] = None,
    location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
) -> Sequence[IdpsView]:
    query = select(IdpsView)

    # Query statements
    # if provider_admin1_name:
    #     query = query.where(IdpsView.provider_admin1_name.icontains(provider_admin1_name))
    # if provider_admin2_name:
    #     query = query.where(IdpsView.provider_admin2_name.icontains(provider_admin2_name))
    if has_hrp is not None:
        query = query.where(IdpsView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(IdpsView.in_gho == in_gho)

    query = apply_reference_period_filter(query, ref_period_parameters, IdpsView)
    query = apply_pagination(query, pagination_parameters)
    query = apply_location_admin_filter(
        query,
        IdpsView,
        location_ref,
        location_code,
        location_name,
        has_hrp,
        in_gho,
        admin1_ref,
        admin1_code,
        admin1_name,
        admin1_is_unspecified,
        admin2_ref,
        admin2_code,
        admin2_name,
        admin2_is_unspecified,
    )

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    idps = result.scalars().all()

    logger.info(f'Retrieved {len(idps)} rows from the database')

    return idps

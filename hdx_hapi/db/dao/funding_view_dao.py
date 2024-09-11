import logging
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import FundingView
from hdx_hapi.db.dao.util.util import apply_pagination, apply_reference_period_filter, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


logger = logging.getLogger(__name__)


async def funding_view_list(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    appeal_code: Optional[str] = None,
    appeal_type: Optional[str] = None,
    org_acronym: Optional[str] = None,
    org_name: Optional[str] = None,
    sector_name: Optional[str] = None,
    # location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[FundingView]:
    query = select(FundingView)
    if org_acronym:
        query = case_insensitive_filter(query, FundingView.org_acronym, org_acronym)
    if org_name:
        query = query.where(FundingView.org_name.icontains(org_name))
    if sector_name:
        query = query.where(FundingView.sector_name.icontains(sector_name))
    # if location_ref:
    #     query = query.where(FundingView.location_ref == location_ref)
    if location_code:
        query = case_insensitive_filter(query, FundingView.location_code, location_code)
    if location_name:
        query = query.where(FundingView.location_name.icontains(location_name))
    if appeal_code:
        query = case_insensitive_filter(query, FundingView.appeal_code, appeal_code)
    if appeal_type:
        query = case_insensitive_filter(query, FundingView.appeal_type, appeal_type)
    if has_hrp is not None:
        query = query.where(FundingView.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(FundingView.in_gho == in_gho)

    query = apply_reference_period_filter(query, ref_period_parameters, FundingView)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(FundingView.appeal_code, FundingView.location_ref)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    funding = result.scalars().all()

    logger.info(f'Retrieved {len(funding)} rows from the database')

    return funding

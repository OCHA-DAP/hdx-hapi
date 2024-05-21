from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.funding_view_dao import funding_view_list
from hdx_hapi.db.models.views.all_views import FundingView
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_funding_srv(
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
) -> Sequence[FundingView]:
    
    return await funding_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        appeal_code=appeal_code,
        appeal_type=appeal_type,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
    )

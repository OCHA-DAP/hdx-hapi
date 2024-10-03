from typing import Optional, Sequence, Union
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.db_views_as_tables import DBFundingVAT

from hdx_hapi.db.dao.funding_view_dao import funding_view_list
from hdx_hapi.db.models.views.all_views import FundingView
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_funding_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    appeal_code: Optional[str] = None,
    appeal_type: Optional[str] = None,
    # location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Union[Sequence[FundingView], Sequence[DBFundingVAT]]:
    return await funding_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        appeal_code=appeal_code,
        appeal_type=appeal_type,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

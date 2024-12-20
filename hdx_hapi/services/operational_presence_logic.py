from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.base import Base

from hdx_hapi.db.dao.operational_presence_view_dao import operational_presences_view_list
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationParameters,
    PaginationParams,
    ReferencePeriodParameters,
)


async def get_operational_presences_srv(
    common_date_range_params: CommonDateRangeParams,
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    sector_code: Optional[str] = None,
    org_acronym: Optional[str] = None,
    org_name: Optional[str] = None,
    sector_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[Base]:
    return await operational_presences_view_list(
        common_date_range_params=common_date_range_params,
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        sector_code=sector_code,
        org_acronym=org_acronym,
        org_name=org_name,
        sector_name=sector_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

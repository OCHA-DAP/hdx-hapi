from typing import Optional, Sequence, Union
from sqlalchemy.ext.asyncio import AsyncSession
from hapi_schema.db_views_as_tables import DBIDPsVAT
from hdx_hapi.db.dao.idps_view_dao import idps_view_list
from hdx_hapi.db.models.views.all_views import IdpsView
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationParameters,
    PaginationParams,
    ReferencePeriodParameters,
)


async def get_idps_srv(
    common_date_range_params: CommonDateRangeParams,
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Union[Sequence[IdpsView], Sequence[DBIDPsVAT]]:
    return await idps_view_list(
        common_date_range_params=common_date_range_params,
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

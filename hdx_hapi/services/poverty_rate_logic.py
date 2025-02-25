from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.models.views.all_views import PovertyRateView
from hdx_hapi.db.dao.poverty_rate_dao import poverty_rates_view_list
from hdx_hapi.endpoints.util.util import (
    CommonDateRangeParams,
    CommonLocationAdm1Parameters,
    PaginationParams,
    ReferencePeriodParameters,
)


async def get_poverty_rates_srv(
    common_date_range_params: CommonDateRangeParams,
    pagination_parameters: PaginationParams,
    common_location_params: CommonLocationAdm1Parameters,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    mpi_min: Optional[float] = None,
    mpi_max: Optional[float] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[PovertyRateView]:
    return await poverty_rates_view_list(
        common_date_range_params=common_date_range_params,
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        mpi_min=mpi_min,
        mpi_max=mpi_max,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

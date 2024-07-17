from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.models.views.all_views import PovertyRateView
from hdx_hapi.db.dao.poverty_rate_dao import poverty_rates_view_list
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_poverty_rates_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    mpi_min: Optional[float] = None,
    mpi_max: Optional[float] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_name: Optional[str] = None,
) -> Sequence[PovertyRateView]:
    return await poverty_rates_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        mpi_min=mpi_min,
        mpi_max=mpi_max,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_name=admin1_name,
    )

# from datetime import datetime
from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.base import Base
from hdx_hapi.db.dao.humanitarian_needs_view_dao import humanitarian_needs_view_list
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams, ReferencePeriodParameters
from hapi_schema.utils.enums import PopulationStatus


async def get_humanitarian_needs_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters,    
    db: AsyncSession,
    category: Optional[str] = None,
    sector_code: Optional[str] = None,
    population_status: Optional[PopulationStatus] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    sector_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[Base]:
    # admin1_is_unspecified, admin2_is_unspecified, provider_admin1_name_is_unspecified, \
    #     provider_admin2_name_is_unspecified = \
    #         compute_unspecified_values(admin_level, provider_admin1_name, provider_admin2_name)

    return await humanitarian_needs_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        category=category,
        sector_code=sector_code,
        population_status=population_status,
        population_min=population_min,
        population_max=population_max,
        sector_name=sector_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

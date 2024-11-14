from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import Gender

from hdx_hapi.db.dao.population_view_dao import populations_view_list
from hdx_hapi.endpoints.util.util import CommonEndpointParams, CommonLocationParameters, ReferencePeriodParameters


async def get_populations_srv(
    ref_period_parameters: Optional[ReferencePeriodParameters],
    pagination_parameters: CommonEndpointParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    return await populations_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        gender=gender,
        age_range=age_range,
        population_min=population_min,
        population_max=population_max,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

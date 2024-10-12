from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.models.views.all_views import RefugeesView
from hdx_hapi.db.dao.refugees_view_dao import refugees_view_list
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters
from hapi_schema.utils.enums import Gender, PopulationGroup


async def get_refugees_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    population_group: Optional[PopulationGroup] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    origin_location_code: Optional[str] = None,
    origin_location_name: Optional[str] = None,
    origin_has_hrp: Optional[bool] = None,
    origin_in_gho: Optional[bool] = None,
    asylum_location_code: Optional[str] = None,
    asylum_location_name: Optional[str] = None,
    asylum_has_hrp: Optional[bool] = None,
    asylum_in_gho: Optional[bool] = None,
) -> Sequence[RefugeesView]:
    return await refugees_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        population_group=population_group,
        population_min=population_min,
        population_max=population_max,
        gender=gender,
        age_range=age_range,
        origin_location_code=origin_location_code,
        origin_location_name=origin_location_name,
        origin_has_hrp=origin_has_hrp,
        origin_in_gho=origin_in_gho,
        asylum_location_code=asylum_location_code,
        asylum_location_name=asylum_location_name,
        asylum_has_hrp=asylum_has_hrp,
        asylum_in_gho=asylum_in_gho,
    )

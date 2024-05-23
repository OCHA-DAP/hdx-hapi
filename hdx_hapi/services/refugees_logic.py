from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.models.views.all_views import RefugeesView
from hdx_hapi.db.dao.refugees_view_dao import refugees_view_list
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters
from hapi_schema.utils.enums import Gender, PopulationGroup


async def get_refugees_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    population_group: Optional[PopulationGroup] = None,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    origin_location_code: Optional[str] = None,
    origin_location_name: Optional[str] = None,
    asylum_location_code: Optional[str] = None,
    asylum_location_name: Optional[str] = None,
) -> Sequence[RefugeesView]:
    return await refugees_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        population_group=population_group,
        gender=gender,
        age_range=age_range,
        min_age=min_age,
        max_age=max_age,
        origin_location_code=origin_location_code,
        origin_location_name=origin_location_name,
        asylum_location_code=asylum_location_code,
        asylum_location_name=asylum_location_name,
    )

from typing import Optional, Sequence, Union
from hapi_schema.db_views_as_tables import DBReturneesVAT
from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.db.dao.returnees_view_dao import returnees_view_list
from hdx_hapi.db.models.views.all_views import ReturneesView
from hapi_schema.utils.enums import Gender, PopulationGroup
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_returnees_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    population_group: Optional[PopulationGroup] = None,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None,
    origin_location_code: Optional[str] = None,
    origin_location_name: Optional[str] = None,
    origin_has_hrp: Optional[bool] = None,
    origin_in_gho: Optional[bool] = None,
    asylum_location_code: Optional[str] = None,
    asylum_location_name: Optional[str] = None,
    asylum_has_hrp: Optional[bool] = None,
    asylum_in_gho: Optional[bool] = None,
) -> Union[Sequence[ReturneesView], Sequence[DBReturneesVAT]]:
    return await returnees_view_list(
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
        origin_has_hrp=origin_has_hrp,
        origin_in_gho=origin_in_gho,
        asylum_location_code=asylum_location_code,
        asylum_location_name=asylum_location_name,
        asylum_has_hrp=asylum_has_hrp,
        asylum_in_gho=asylum_in_gho,
    )

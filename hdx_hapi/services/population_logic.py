from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import Gender

from hdx_hapi.db.dao.population_view_dao import populations_view_list
from hdx_hapi.endpoints.util.util import AdminLevel, CommonEndpointParams, ReferencePeriodParameters
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_populations_srv(
    ref_period_parameters: Optional[ReferencePeriodParameters],
    pagination_parameters: CommonEndpointParams,
    db: AsyncSession,
    gender: Optional[Gender] = None,
    age_range: Optional[str] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_name: Optional[str] = None,
    admin1_code: Optional[str] = None,
    provider_admin1_name: Optional[str] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    provider_admin2_name: Optional[str] = None,
    admin_level: Optional[AdminLevel] = None,
):
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await populations_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        gender=gender,
        age_range=age_range,
        population_min=population_min,
        population_max=population_max,
        admin1_ref=admin1_ref,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        provider_admin1_name=provider_admin1_name,
        admin2_ref=admin2_ref,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        provider_admin2_name=provider_admin2_name,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_is_unspecified=admin2_is_unspecified,
    )

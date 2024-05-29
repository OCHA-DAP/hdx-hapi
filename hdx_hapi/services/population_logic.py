from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import Gender

from hdx_hapi.db.dao.population_view_dao import populations_view_list
from hdx_hapi.endpoints.util.util import AdminLevel, CommonEndpointParams, ReferencePeriodParameters
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_populations_srv(
    ref_period_parameters: ReferencePeriodParameters,
    pagination_parameters: CommonEndpointParams,
    db: AsyncSession,
    gender: Gender = None,
    age_range: str = None,
    min_age: int = None,
    max_age: int = None,
    population: int = None,
    location_ref: int = None,
    location_code: str = None,
    location_name: str = None,
    admin1_ref: int = None,
    admin1_name: str = None,
    admin1_code: str = None,
    # admin1_is_unspecified: bool = None,
    admin2_ref: int = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin_level: AdminLevel = None,
    # admin2_is_unspecified: bool = None,
):
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await populations_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        gender=gender,
        age_range=age_range,
        population=population,
        admin1_ref=admin1_ref,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin2_ref=admin2_ref,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_is_unspecified=admin2_is_unspecified,
    )

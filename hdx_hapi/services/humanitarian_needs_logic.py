# from datetime import datetime
from typing import Optional, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.base import Base
from hdx_hapi.db.dao.humanitarian_needs_view_dao import humanitarian_needs_view_list
from hdx_hapi.services.admin_level_logic import compute_unspecified_values
from hdx_hapi.endpoints.util.util import AdminLevel, PaginationParams, ReferencePeriodParameters
from hapi_schema.utils.enums import PopulationStatus


async def get_humanitarian_needs_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    admin2_ref: Optional[int] = None,
    category: Optional[str] = None,
    sector_code: Optional[str] = None,
    population_status: Optional[PopulationStatus] = None,
    population_min: Optional[int] = None,
    population_max: Optional[int] = None,
    sector_name: Optional[str] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    location_ref: Optional[int] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_code: Optional[str] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    provider_admin2_name: Optional[str] = None,
    admin1_ref: Optional[int] = None,
    admin1_name: Optional[str] = None,
    provider_admin1_name: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    admin2_is_unspecified: Optional[bool] = None,
    admin_level: Optional[AdminLevel] = None,
) -> Sequence[Base]:
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await humanitarian_needs_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        admin2_ref=admin2_ref,
        category=category,
        sector_code=sector_code,
        population_status=population_status,
        population_min=population_min,
        population_max=population_max,
        sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
        location_ref=location_ref,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_code=admin1_code,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        provider_admin2_name=provider_admin2_name,
        admin1_ref=admin1_ref,
        admin1_name=admin1_name,
        provider_admin1_name=provider_admin1_name,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_is_unspecified=admin2_is_unspecified,
    )

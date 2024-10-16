from typing import Optional, Sequence
from hapi_schema.utils.enums import EventType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.conflict_event_view_dao import conflict_event_view_list
from hapi_schema.utils.base import Base
from hdx_hapi.endpoints.util.util import AdminLevel, PaginationParams, ReferencePeriodParameters
from hdx_hapi.services.admin_level_logic import compute_unspecified_values


async def get_conflict_event_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db: AsyncSession,
    event_type: Optional[EventType] = None,
    location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    provider_admin1_name: Optional[str] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    provider_admin2_name: Optional[str] = None,
    admin_level: Optional[AdminLevel] = None,
) -> Sequence[Base]:
    admin1_is_unspecified, admin2_is_unspecified = compute_unspecified_values(admin_level)

    return await conflict_event_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        event_type=event_type,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        has_hrp=has_hrp,
        in_gho=in_gho,
        admin1_ref=admin1_ref,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        provider_admin1_name=provider_admin1_name,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_ref=admin2_ref,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        provider_admin2_name=provider_admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
    )

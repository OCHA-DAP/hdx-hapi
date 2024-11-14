from typing import Optional, Sequence
from hapi_schema.utils.enums import EventType
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.conflict_event_view_dao import conflict_event_view_list
from hapi_schema.utils.base import Base
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams, ReferencePeriodParameters


async def get_conflict_event_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    common_location_params: CommonLocationParameters, 
    db: AsyncSession,
    event_type: Optional[EventType] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Sequence[Base]:

    return await conflict_event_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        event_type=event_type,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hapi_schema.utils.enums import IPCType, IPCPhase
from hdx_hapi.db.dao.food_security_view_dao import food_security_view_list
from hdx_hapi.endpoints.util.util import CommonEndpointParams, CommonLocationParameters, ReferencePeriodParameters


async def get_food_security_srv(
    ref_period_parameters: Optional[ReferencePeriodParameters],
    pagination_parameters: CommonEndpointParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    ipc_phase: Optional[IPCPhase] = None,
    ipc_type: Optional[IPCType] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
):
    return await food_security_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        common_location_params=common_location_params,
        db=db,
        ipc_phase=ipc_phase,
        ipc_type=ipc_type,
        has_hrp=has_hrp,
        in_gho=in_gho,
    )

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.location_view_dao import locations_view_list
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


async def get_locations_srv(
    pagination_parameters: PaginationParams,
    ref_period_parameters: ReferencePeriodParameters,
    db: AsyncSession,
    id: int = None,
    code: str = None,
    name: str = None,
):
    return await locations_view_list(
        pagination_parameters=pagination_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        id=id,
        code=code,
        name=name,
    )

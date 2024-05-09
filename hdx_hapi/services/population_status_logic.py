from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.population_status_view_dao import population_statuses_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_population_statuses_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
    description: str = None,
):
    return await population_statuses_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description,
    )

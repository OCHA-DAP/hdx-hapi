from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.admin2_view_dao import admin2_view_list
from hdx_hapi.endpoints.util.util import PaginationParams

async def get_admin2_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    admin1_code: str = None,
    admin1_name: str = None,
    location_code: str = None,
    location_name: str = None,
):
    return await admin2_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_code=location_code,
        location_name=location_name,
    )

from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.org_type_view_dao import org_types_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_org_types_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    code: Optional[str] = None,
    description: Optional[str] = None,
):
    return await org_types_view_list(
        pagination_parameters=pagination_parameters, db=db, code=code, description=description
    )

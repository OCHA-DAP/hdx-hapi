from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.org_view_dao import orgs_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_orgs_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    acronym: Optional[str] = None,
    name: Optional[str] = None,
    org_type_code: Optional[str] = None,
    org_type_description: Optional[str] = None,
):
    return await orgs_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        acronym=acronym,
        name=name,
        org_type_code=org_type_code,
        org_type_description=org_type_description,
    )

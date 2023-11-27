from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.org_view_dao import orgs_view_list


async def get_orgs_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    acronym: str = None,
    name: str = None,
    org_type_code: str = None,
    org_type_description: str = None,
):
    return await orgs_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        acronym=acronym,
        name=name,
        org_type_code=org_type_code,
        org_type_description=org_type_description,
    )

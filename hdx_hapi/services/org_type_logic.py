from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.org_type_view_dao import org_types_view_list

from datetime import datetime


async def get_org_types_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    description: str = None
):
    return await org_types_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )

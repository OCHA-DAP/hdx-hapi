from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.gender_view_dao import genders_view_list

async def get_genders_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    description: str = None
):
    return await genders_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )

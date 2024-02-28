from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.population_group_view_dao import population_groups_view_list


async def get_population_groups_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    description: str = None,
):
    return await population_groups_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description,
    )

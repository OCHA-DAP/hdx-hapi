from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.dataset_view_dao import datasets_view_list


async def get_datasets_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    title: str = None,
    provider_code: str = None,
    provider_name: str = None,
):
    return await datasets_view_list(
        pagination_parameters=pagination_parameters, db=db, code=code, title=title, provider_code=provider_code, provider_name=provider_name
    )

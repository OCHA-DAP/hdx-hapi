from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.dataset_view_dao import datasets_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_datasets_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    dataset_hdx_id: Optional[str] = None,
    dataset_hdx_stub: Optional[str] = None,
    dataset_hdx_title: Optional[str] = None,
    hdx_provider_stub: Optional[str] = None,
    hdx_provider_name: Optional[str] = None,
):
    return await datasets_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        dataset_hdx_id=dataset_hdx_id,
        dataset_hdx_stub=dataset_hdx_stub,
        dataset_hdx_title=dataset_hdx_title,
        hdx_provider_stub=hdx_provider_stub,
        hdx_provider_name=hdx_provider_name,
    )

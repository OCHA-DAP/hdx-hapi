from typing import Optional

from datetime import datetime, date
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.resource_view_dao import resources_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_resources_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    resource_hdx_id: Optional[str] = None,
    format: Optional[str] = None,
    update_date_min: Optional[datetime | date] = None,
    update_date_max: Optional[datetime | date] = None,
    is_hxl: Optional[bool] = None,
    dataset_hdx_title: Optional[str] = None,
    dataset_hdx_id: Optional[str] = None,
    dataset_hdx_stub: Optional[str] = None,
    dataset_hdx_provider_stub: Optional[str] = None,
    dataset_hdx_provider_name: Optional[str] = None,
):
    return await resources_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        resource_hdx_id=resource_hdx_id,
        format=format,
        update_date_min=update_date_min,
        update_date_max=update_date_max,
        is_hxl=is_hxl,
        dataset_hdx_id=dataset_hdx_id,
        dataset_hdx_stub=dataset_hdx_stub,
        dataset_hdx_title=dataset_hdx_title,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        dataset_hdx_provider_name=dataset_hdx_provider_name,
    )

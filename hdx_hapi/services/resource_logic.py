from typing import Dict
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.resource_view_dao import resources_view_list


async def get_resources_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    hdx_id: str = None,
    format: str = None,
    update_date_min: datetime = None,
    update_date_max: datetime = None,
    is_hxl: bool = None,
    dataset_title: str = None,
    dataset_hdx_id: str = None,
    dataset_hdx_stub: str = None,
    dataset_hdx_provider_stub: str = None,
    dataset_hdx_provider_name: str = None,
):
    return await resources_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        hdx_id=hdx_id,
        format=format,
        update_date_min=update_date_min,
        update_date_max=update_date_max,
        is_hxl=is_hxl,
        dataset_hdx_id=dataset_hdx_id,
        dataset_hdx_stub=dataset_hdx_stub,
        dataset_title=dataset_title,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        dataset_hdx_provider_name=dataset_hdx_provider_name,
    )

from typing import Dict
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_resource_view import ResourceView
from hdx_hapi.db.dao.util.util import apply_pagination

async def resources_view_list(
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
    dataset_provider_code: str = None,
    dataset_provider_name: str = None,
):

    query = select(ResourceView)
    if hdx_id:
        query = query.where(ResourceView.hdx_id == hdx_id)
    if format:
        query = query.where(ResourceView.format == format)
    if update_date_min:
        query = query.where(ResourceView.update_date >= update_date_min)
    if update_date_max:
        query = query.where(ResourceView.update_date < update_date_max)
    if is_hxl is not None:
        query = query.where(ResourceView.is_hxl == is_hxl)
    if dataset_title:
        query = query.where(ResourceView.dataset_title == dataset_title)
    if dataset_hdx_id:
        query = query.where(ResourceView.dataset_hdx_id == dataset_hdx_id)
    if dataset_hdx_stub:
        query = query.where(ResourceView.dataset_hdx_stub == dataset_hdx_stub)
    if dataset_provider_code:
        query = query.where(ResourceView.dataset_provider_code == dataset_provider_code)
    if dataset_provider_name:
        query = query.where(ResourceView.dataset_provider_name == dataset_provider_name)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    resources = result.scalars().all()
    return resources
from datetime import datetime
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.vat_or_view import ResourceView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams


async def resources_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    resource_hdx_id: Optional[str] = None,
    format: Optional[str] = None,
    update_date_min: Optional[datetime] = None,
    update_date_max: Optional[datetime] = None,
    is_hxl: Optional[bool] = None,
    hapi_updated_date_min: Optional[datetime] = None,
    hapi_updated_date_max: Optional[datetime] = None,
    dataset_hdx_title: Optional[str] = None,
    dataset_hdx_id: Optional[str] = None,
    dataset_hdx_stub: Optional[str] = None,
    dataset_hdx_provider_stub: Optional[str] = None,
    dataset_hdx_provider_name: Optional[str] = None,
):
    query = select(ResourceView)
    if resource_hdx_id:
        query = query.where(ResourceView.resource_hdx_id == resource_hdx_id)
    if format:
        query = query.where(ResourceView.format == format)
    if update_date_min:
        query = query.where(ResourceView.update_date >= update_date_min)
    if update_date_max:
        query = query.where(ResourceView.update_date < update_date_max)
    if is_hxl is not None:
        query = query.where(ResourceView.is_hxl == is_hxl)
    if hapi_updated_date_min:
        query = query.where(ResourceView.hapi_updated_date >= hapi_updated_date_min)
    if hapi_updated_date_max:
        query = query.where(ResourceView.hapi_updated_date < hapi_updated_date_max)
    if dataset_hdx_title:
        query = query.where(ResourceView.dataset_hdx_title.icontains(dataset_hdx_title))
    if dataset_hdx_id:
        query = query.where(ResourceView.dataset_hdx_id == dataset_hdx_id)
    if dataset_hdx_stub:
        query = query.where(ResourceView.dataset_hdx_stub == dataset_hdx_stub)
    if dataset_hdx_provider_stub:
        query = case_insensitive_filter(query, ResourceView.dataset_hdx_provider_stub, dataset_hdx_provider_stub)
    if dataset_hdx_provider_name:
        query = query.where(ResourceView.dataset_hdx_provider_name == dataset_hdx_provider_name)

    query = apply_pagination(query, pagination_parameters)
    query = query.order_by(ResourceView.resource_hdx_id)

    result = await db.execute(query)
    resources = result.scalars().all()
    return resources

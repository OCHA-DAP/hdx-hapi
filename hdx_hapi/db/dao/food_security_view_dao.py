import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_food_security_view import FoodSecurityView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter


async def food_security_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    ipc_phase_code: str = None,
    ipc_type_code: str = None,
    dataset_hdx_provider_stub: str = None,
    resource_update_date_min: datetime = None,
    resource_update_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
    admin1_name: str = None,
    admin1_code: str = None,
    admin1_is_unspecified: bool = None,
    admin2_code: str = None,
    admin2_name: str = None,
    admin2_is_unspecified: bool = None,
):

    query = select(FoodSecurityView)

    if ipc_phase_code:
        query = query.where(FoodSecurityView.ipc_phase_code == ipc_phase_code)
    if ipc_type_code:
        query = case_insensitive_filter(query, FoodSecurityView.ipc_type_code, ipc_type_code)
    if dataset_hdx_provider_stub:
        query = case_insensitive_filter(query, FoodSecurityView.dataset_hdx_provider_stub, dataset_hdx_provider_stub)
    if resource_update_date_min:
        query = query.where(FoodSecurityView.resource_update_date >= resource_update_date_min)
    if resource_update_date_max:
        query = query.where(FoodSecurityView.resource_update_date < resource_update_date_max)
    if location_code:
        query = case_insensitive_filter(query, FoodSecurityView.location_code, location_code)
    if location_name:
        query = query.where(FoodSecurityView.location_name.icontains(location_name))
    if admin1_name:
        query = query.where(FoodSecurityView.admin1_name.icontains(admin1_name))
    if admin1_code:
        query = case_insensitive_filter(query, FoodSecurityView.admin1_code, admin1_code)
    if admin1_is_unspecified is not None:
        query = query.where(FoodSecurityView.admin1_is_unspecified == admin1_is_unspecified)
    if admin2_code:
        query = case_insensitive_filter(query, FoodSecurityView.admin2_code, admin2_code)
    if admin2_name:
        query = query.where(FoodSecurityView.admin2_name.icontains(admin2_name))
    if admin2_is_unspecified is not None:
        query = query.where(FoodSecurityView.admin2_is_unspecified == admin2_is_unspecified)

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    food_security = result.scalars().all()
    return food_security
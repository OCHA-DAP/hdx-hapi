from datetime import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.location_view_dao import locations_view_list


async def get_locations_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
):
    return await locations_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
        hapi_replaced_date_min=hapi_replaced_date_min,
        hapi_replaced_date_max=hapi_replaced_date_max,
    )

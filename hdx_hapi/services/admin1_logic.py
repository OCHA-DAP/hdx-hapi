from datetime import datetime
from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.admin1_view_dao import admin1_view_list



async def get_admin1_srv(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    name: str = None,
    hapi_updated_date_min: datetime = None,
    hapi_updated_date_max: datetime = None,
    hapi_replaced_date_min: datetime = None,
    hapi_replaced_date_max: datetime = None,
    location_code: str = None,
    location_name: str = None,
):
    return await admin1_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
        hapi_replaced_date_min=hapi_replaced_date_min,
        hapi_replaced_date_max=hapi_replaced_date_max,
        location_code=location_code,
        location_name=location_name
    )

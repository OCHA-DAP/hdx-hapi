import datetime
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.db.dao.availability_view_dao import availability_view_list
from hdx_hapi.endpoints.util.util import PaginationParams


async def get_availability_srv(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    location_name: Optional[str] = None,
    location_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_code: Optional[str] = None,
    hapi_updated_date_min: Optional[datetime.datetime] = None,
    hapi_updated_date_max: Optional[datetime.datetime] = None,
):
    return await availability_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        category=category,
        subcategory=subcategory,
        location_name=location_name,
        location_code=location_code,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
    )

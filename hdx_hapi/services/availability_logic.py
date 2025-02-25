import datetime
from typing import Optional, Sequence, Union
from sqlalchemy.ext.asyncio import AsyncSession


from hapi_schema.db_views_as_tables import DBAvailabilityVAT

from hdx_hapi.db.dao.availability_view_dao import availability_view_list
from hdx_hapi.db.models.views.all_views import AvailabilityView
from hdx_hapi.endpoints.util.util import CommonLocationParameters, PaginationParams


async def get_availability_srv(
    pagination_parameters: PaginationParams,
    common_location_params: CommonLocationParameters,
    db: AsyncSession,
    category: Optional[str] = None,
    subcategory: Optional[str] = None,
    hapi_updated_date_min: Optional[datetime.datetime | datetime.date] = None,
    hapi_updated_date_max: Optional[datetime.datetime | datetime.date] = None,
) -> Union[Sequence[AvailabilityView], Sequence[DBAvailabilityVAT]]:
    return await availability_view_list(
        pagination_parameters=pagination_parameters,
        db=db,
        category=category,
        subcategory=subcategory,
        common_location_params=common_location_params,
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
    )

from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter

from ..config import doc_snippets as snip

from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.admin_level import Admin1Response, Admin2Response, LocationResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.admin1_logic import get_admin1_srv
from hdx_hapi.services.admin2_logic import get_admin2_srv
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.location_logic import get_locations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

from datetime import datetime, date

router = APIRouter(
    tags=['Locations and Administrative Divisions'],
)

@router.get('/api/location', response_model=List[LocationResponse], summary='Get the list of locations (typically countries) included in HAPI.')
async def get_locations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description=f'{snip.doc_location_code}')] = None,
    name: Annotated[str, Query(max_length=512, description=f'{snip.doc_location_name}')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    f"""{snip.doc_scope_disclaimer}
    """    
    result = await get_locations_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, LocationResponse)


@router.get('/api/admin1', response_model=List[Admin1Response])
async def get_admin1(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description=snip.doc_admin1_code)] = None,
    name: Annotated[str, Query(max_length=512, description=f'{snip.doc_admin1_name} {snip.doc_see_admin1}')] = None,
    location_code: Annotated[str, Query(max_length=128, description='Location code')] = None,
    location_name: Annotated[str, Query(max_length=512, description='Location name')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """Get the list of admin1 entries.
    """    
    result = await get_admin1_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, Admin1Response)


@router.get('/api/admin2', response_model=List[Admin2Response])
async def get_admin2(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=128, description='Code')] = None,
    name: Annotated[str, Query(max_length=512, description='Name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description='Admin1 name')] = None,
    location_code: Annotated[str, Query(max_length=128, description='Location code')] = None,
    location_name: Annotated[str, Query(max_length=512, description='Location name')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """Get the list of admin2 entries.
    """    
    result = await get_admin2_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        name=name,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, Admin2Response)

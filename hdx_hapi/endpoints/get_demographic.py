from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.age_range_view import AgeRangeViewPydantic
from hdx_hapi.endpoints.models.gender_view import GenderViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters, OutputFormat
from hdx_hapi.services.age_range_logic import get_age_ranges_srv
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.gender_logic import get_genders_srv
from hdx_hapi.services.sql_alchemy_session import get_db


router = APIRouter(
    tags=['demographic'],
)


@router.get('/api/age_range', response_model=List[AgeRangeViewPydantic])
async def get_age_ranges(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, description='Age range code', example='20-24')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """Get the list of all active age ranges.
    """    
    result = await get_age_ranges_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
    )
    
    return transform_result_to_csv_stream_if_requested(result, output_format, AgeRangeViewPydantic)


@router.get('/api/gender', response_model=List[GenderViewPydantic])
async def get_genders(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=1, description='Gender code', example='f')] = None,
    description: Annotated[str, Query(max_length=256, description='Gender description', example='female')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """Get the list of all genders.
    """    
    result = await get_genders_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, GenderViewPydantic)

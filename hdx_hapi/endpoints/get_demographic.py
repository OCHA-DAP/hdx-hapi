from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession
from hdx_hapi.config.doc_snippets import (
    DOC_AGE_RANGE_CODE,
    DOC_AGE_RANGE_SUMMARY,
    DOC_GENDER_CODE,
    DOC_GENDER_DESCRIPTION,
    DOC_GENDER_SUMMARY
)

from hdx_hapi.endpoints.models.demographic import AgeRangeResponse, GenderResponse
from hdx_hapi.endpoints.util.util import pagination_parameters, OutputFormat
from hdx_hapi.services.age_range_logic import get_age_ranges_srv
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.gender_logic import get_genders_srv
from hdx_hapi.services.sql_alchemy_session import get_db


router = APIRouter(
    tags=['Age and Gender Disaggregations'],
)


@router.get('/api/age_range', response_model=List[AgeRangeResponse], summary = f'{DOC_AGE_RANGE_SUMMARY}')
async def get_age_ranges(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=32, example='20-24', description=f'{DOC_AGE_RANGE_CODE}')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """Get the list of age ranges used for disaggregating population data. Age ranges are not standardized across 
    different data sources and instead reflect the age range breakdowns provided by the data source.
    """    
    result = await get_age_ranges_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
    )
    
    return transform_result_to_csv_stream_if_requested(result, output_format, AgeRangeResponse)


@router.get('/api/gender', response_model=List[GenderResponse], summary=f'{DOC_GENDER_SUMMARY}')
async def get_genders(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=1, description=f'{DOC_GENDER_CODE}', example='f')] = None,
    description: Annotated[
        str, Query(max_length=256, description=f'{DOC_GENDER_DESCRIPTION}', example='female')
    ] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    """    
    result = await get_genders_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        code=code,
        description=description
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, GenderResponse)

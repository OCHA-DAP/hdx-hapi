from datetime import datetime, date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN1_CODE, 
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME, 
    DOC_LOCATION_CODE, 
    DOC_LOCATION_NAME, 
    DOC_SCOPE_DISCLAIMER,
    DOC_SEE_ADMIN1,
    DOC_SEE_ADMIN2, 
    DOC_SEE_LOC
)

from hdx_hapi.endpoints.models.population import PopulationResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Baseline Population'],
)


@router.get('/api/themes/population', response_model=List[PopulationResponse], summary='Get baseline population data')
async def get_populations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    gender_code: Annotated[str, Query(max_length=1, description='Gender code')] = None,
    age_range_code: Annotated[str, Query(max_length=32, description='Age range code')] = None,
    population: Annotated[int, Query(description='Population')] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description='Organization(provider) code')] = None,
    resource_update_date_min: Annotated[datetime | date, Query(description='Min date of update date, e.g. 2020-01-01 or 2020-01-01T00:00:00', example='2020-01-01')] = None,
    resource_update_date_max: Annotated[datetime | date, Query(description='Max date of update date, e.g. 2024-12-31 or 2024-12-31T23:59:59', example='2024-12-31')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    admin1_is_unspecified: Annotated[bool, Query(description='Is admin1 specified or not')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description='Admin2 code')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description='Admin2 name')] = None,
    admin2_is_unspecified: Annotated[bool, Query(description='Is admin2 specified or not')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of populations
    """
    result = await get_populations_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        gender_code=gender_code,
        age_range_code=age_range_code,
        population=population,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_code=admin1_code,
        admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_is_unspecified=admin2_is_unspecified,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationResponse)

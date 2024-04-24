from datetime import date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
    DOC_UPDATE_DATE_MAX,
    DOC_UPDATE_DATE_MIN,
    DOC_HAPI_UPDATED_DATE_MIN,
    DOC_HAPI_UPDATED_DATE_MAX,
    DOC_HAPI_REPLACED_DATE_MIN,
    DOC_HAPI_REPLACED_DATE_MAX,
)

from hdx_hapi.endpoints.models.population import PopulationResponse
from hdx_hapi.endpoints.util.util import AdminLevel, OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Baseline Population'],
)


@router.get(
    '/api/themes/population',
    response_model=List[PopulationResponse],
    summary='Get baseline population data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/themes/population', response_model=List[PopulationResponse], summary='Get baseline population data'
)
async def get_populations(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    gender_code: Annotated[str, Query(max_length=1, description='Gender code')] = None,
    age_range_code: Annotated[str, Query(max_length=32, description='Age range code')] = None,
    population: Annotated[int, Query(description='Population')] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description='Organization(provider) code')] = None,
    resource_update_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MIN}', openapi_examples={'2020-01-01': {'value': '2020-01-01'}}),
    ] = None,
    resource_update_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MAX}', openapi_examples={'2024-12-31': {'value': '2024-12-31'}}),
    ] = None,
    hapi_updated_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_UPDATED_DATE_MIN}'),
    ] = None,
    hapi_updated_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_UPDATED_DATE_MAX}'),
    ] = None,
    hapi_replaced_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_REPLACED_DATE_MIN}'),
    ] = None,
    hapi_replaced_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_HAPI_REPLACED_DATE_MAX}'),
    ] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description='Admin1 name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    # admin1_is_unspecified: Annotated[bool, Query(description='Is admin1 specified or not')] = None,
    location_ref: Annotated[int, Query(description='Location reference')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description='Admin2 name')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description='Admin2 code')] = None,
    admin1_ref: Annotated[int, Query(description='Admin1 reference')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level')] = None,
    # admin2_is_unspecified: Annotated[bool, Query(description='Is admin2 specified or not')] = None,
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
        hapi_updated_date_min=hapi_updated_date_min,
        hapi_updated_date_max=hapi_updated_date_max,
        hapi_replaced_date_min=hapi_replaced_date_min,
        hapi_replaced_date_max=hapi_replaced_date_max,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        location_ref=location_ref,
        # admin1_is_unspecified=admin1_is_unspecified,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin1_ref=admin1_ref,
        admin_level=admin_level,
        # admin2_is_unspecified=admin2_is_unspecified,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationResponse)

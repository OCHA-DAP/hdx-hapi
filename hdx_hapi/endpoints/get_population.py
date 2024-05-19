from datetime import date
from typing import Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
)

from hdx_hapi.endpoints.models.base import HapiGenericResponse
from hdx_hapi.endpoints.models.population import PopulationResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    ReferencePeriodParameters,
    common_endpoint_parameters,
    reference_period_parameters,
    AdminLevel,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.population_logic import get_populations_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['Baseline Population'],
)


@router.get(
    '/api/themes/population',
    response_model=HapiGenericResponse[PopulationResponse],
    summary='Get baseline population data',
    include_in_schema=False,
)
@router.get(
    '/api/v1/themes/population',
    response_model=HapiGenericResponse[PopulationResponse],
    summary='Get baseline population data',
)
async def get_populations(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    ref_period_parameters: Annotated[ReferencePeriodParameters, Depends(reference_period_parameters)],
    db: AsyncSession = Depends(get_db),
    gender: Annotated[str, Query(max_length=1, description='Gender')] = None,
    age_range: Annotated[str, Query(max_length=32, description='Age range')] = None,
    min_age: Annotated[int, Query(description='Minimum age')] = None,
    max_age: Annotated[int, Query(description='Maximum age')] = None,
    population: Annotated[int, Query(description='Population')] = None,
    admin1_ref: Annotated[int, Query(description='Admin1 reference')] = None,
    location_ref: Annotated[int, Query(description='Location reference')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    admin1_name: Annotated[str, Query(max_length=512, description='Admin1 name')] = None,
    admin1_code: Annotated[str, Query(max_length=128, description='Admin1 code')] = None,
    # admin1_is_unspecified: Annotated[bool, Query(description='Is admin1 specified or not')] = None,
    admin2_ref: Annotated[int, Query(description='Admin2 reference')] = None,
    admin2_name: Annotated[str, Query(max_length=512, description='Admin2 name')] = None,
    admin2_code: Annotated[str, Query(max_length=128, description='Admin2 code')] = None,
    admin_level: Annotated[AdminLevel, Query(description='Filter the response by admin level')] = None,
    # admin2_is_unspecified: Annotated[bool, Query(description='Is admin2 specified or not')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of populations
    """
    result = await get_populations_srv(
        common_parameters=common_parameters,
        ref_period_parameters=ref_period_parameters,
        db=db,
        gender=gender,
        age_range=age_range,
        min_age=min_age,
        max_age=max_age,
        population=population,
        admin1_ref=admin1_ref,
        location_ref=location_ref,
        location_code=location_code,
        location_name=location_name,
        admin1_name=admin1_name,
        admin1_code=admin1_code,
        admin2_ref=admin2_ref,
        admin2_name=admin2_name,
        admin2_code=admin2_code,
        admin_level=admin_level,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, PopulationResponse)

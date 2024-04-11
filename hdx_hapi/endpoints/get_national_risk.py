from datetime import date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_PROVIDER_STUB,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_LOC,
    DOC_UPDATE_DATE_MAX,
    DOC_UPDATE_DATE_MIN,
)

from hdx_hapi.endpoints.models.national_risk import NationalRiskResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.national_risk_logic import get_national_risks_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['National Risk'],
)


@router.get(
    '/api/themes/national_risk',
    response_model=List[NationalRiskResponse],
    summary='Get national risk data',
    include_in_schema=False,
)
@router.get('/api/v1/themes/national_risk', response_model=List[NationalRiskResponse], summary='Get national risk data')
async def get_national_risks(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    risk_class: Annotated[int, Query(description='Risk class')] = None,
    global_rank: Annotated[int, Query(description='Global rank')] = None,
    overall_risk: Annotated[float, Query(description='Overall risk')] = None,
    hazard_exposure_risk: Annotated[float, Query(description='Hazard exposure risk')] = None,
    vulnerability_risk: Annotated[float, Query(description='Vulnerability risk')] = None,
    coping_capacity_risk: Annotated[float, Query(description='Coping capacity risk')] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_PROVIDER_STUB}')] = None,
    resource_update_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MIN}', openapi_examples={'default': {'value': '2020-01-01'}}),
    ] = None,
    resource_update_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MAX}', openapi_examples={'default': {'value': '2024-12-31'}}),
    ] = None,
    # sector_name: Annotated[str, Query(max_length=512, description=f'{DOC_SECTOR_NAME}')] = None,
    location_code: Annotated[str, Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')] = None,
    location_name: Annotated[str, Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of national risks
    """
    result = await get_national_risks_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        risk_class=risk_class,
        global_rank=global_rank,
        overall_risk=overall_risk,
        hazard_exposure_risk=hazard_exposure_risk,
        vulnerability_risk=vulnerability_risk,
        coping_capacity_risk=coping_capacity_risk,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        resource_update_date_min=resource_update_date_min,
        resource_update_date_max=resource_update_date_max,
        # sector_name=sector_name,
        location_code=location_code,
        location_name=location_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, NationalRiskResponse)

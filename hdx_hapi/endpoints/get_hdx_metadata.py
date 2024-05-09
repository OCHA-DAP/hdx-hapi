from datetime import date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter
from pydantic import NaiveDatetime


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_DATASET_ID,
    DOC_HDX_DATASET_NAME,
    DOC_HDX_DATASET_TITLE,
    DOC_HDX_PROVIDER_NAME,
    DOC_HDX_PROVIDER_STUB,
    DOC_HDX_RESOURCE_FORMAT,
    DOC_HDX_RESOURCE_HXL,
    DOC_HDX_RESOURCE_ID,
    DOC_SEE_DATASET,
    DOC_UPDATE_DATE_MAX,
    DOC_UPDATE_DATE_MIN,
)

from hdx_hapi.endpoints.models.hdx_metadata import DatasetResponse, ResourceResponse
from hdx_hapi.endpoints.util.util import (
    CommonEndpointParams,
    OutputFormat,
    common_endpoint_parameters,
)
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.dataset_logic import get_datasets_srv
from hdx_hapi.services.resource_logic import get_resources_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['HDX Metadata'],
)


@router.get(
    '/api/dataset',
    response_model=List[DatasetResponse],
    summary='Get information about the sources of the data in HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/dataset',
    response_model=List[DatasetResponse],
    summary='Get information about the sources of the data in HAPI',
)
async def get_datasets(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    hdx_id: Annotated[str, Query(max_length=36, description=f'{DOC_HDX_DATASET_ID}')] = None,
    hdx_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_DATASET_NAME}')] = None,
    title: Annotated[str, Query(max_length=1024, description=f'{DOC_HDX_DATASET_TITLE}')] = None,
    hdx_provider_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_PROVIDER_STUB}')] = None,
    hdx_provider_name: Annotated[str, Query(max_length=512, description=f'{DOC_HDX_PROVIDER_NAME}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Get information about the <a href="https://data.humdata.org/dataset">HDX Datasets</a> that are used as data sources
    for HAPI. Datasets contain one or more resources, which are the sources of the data found in HAPI.
    """
    result = await get_datasets_srv(
        pagination_parameters=common_parameters,
        db=db,
        hdx_id=hdx_id,
        hdx_stub=hdx_stub,
        title=title,
        hdx_provider_stub=hdx_provider_stub,
        hdx_provider_name=hdx_provider_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, DatasetResponse)


@router.get(
    '/api/resource',
    response_model=List[ResourceResponse],
    summary='Get information about the sources of the data in HAPI',
    include_in_schema=False,
)
@router.get(
    '/api/v1/resource',
    response_model=List[ResourceResponse],
    summary='Get information about the sources of the data in HAPI',
)
async def get_resources(
    common_parameters: Annotated[CommonEndpointParams, Depends(common_endpoint_parameters)],
    db: AsyncSession = Depends(get_db),
    hdx_id: Annotated[str, Query(max_length=36, description=f'{DOC_HDX_RESOURCE_ID}')] = None,
    format: Annotated[str, Query(max_length=32, description=f'{DOC_HDX_RESOURCE_FORMAT}')] = None,
    update_date_min: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MIN}', openapi_examples={'2020-01-01': {'value': '2020-01-01'}}),
    ] = None,
    update_date_max: Annotated[
        NaiveDatetime | date,
        Query(description=f'{DOC_UPDATE_DATE_MAX}', openapi_examples={'2024-12-31': {'value': '2024-12-31'}}),
    ] = None,
    is_hxl: Annotated[bool, Query(description=f'{DOC_HDX_RESOURCE_HXL}')] = None,
    dataset_hdx_id: Annotated[str, Query(max_length=36, description=f'{DOC_HDX_DATASET_ID} {DOC_SEE_DATASET} ')] = None,
    dataset_hdx_stub: Annotated[
        str, Query(max_length=128, description=f'{DOC_HDX_DATASET_NAME} {DOC_SEE_DATASET}')
    ] = None,
    dataset_title: Annotated[
        str, Query(max_length=1024, description=f'{DOC_HDX_DATASET_TITLE} {DOC_SEE_DATASET}')
    ] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_PROVIDER_STUB}')] = None,
    dataset_hdx_provider_name: Annotated[str, Query(max_length=512, description=f'{DOC_HDX_PROVIDER_NAME}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Get information about the resources that are used as data sources for HAPI. Datasets contain one or more resources,
    which are the sources of the data found in HAPI.
    """
    result = await get_resources_srv(
        pagination_parameters=common_parameters,
        db=db,
        hdx_id=hdx_id,
        format=format,
        update_date_min=update_date_min,
        update_date_max=update_date_max,
        is_hxl=is_hxl,
        dataset_hdx_id=dataset_hdx_id,
        dataset_hdx_stub=dataset_hdx_stub,
        dataset_title=dataset_title,
        dataset_hdx_provider_stub=dataset_hdx_provider_stub,
        dataset_hdx_provider_name=dataset_hdx_provider_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, ResourceResponse)

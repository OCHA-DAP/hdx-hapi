from datetime import datetime, date
from typing import List, Annotated
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_DATASET_ID,
    DOC_HDX_DATASET_NAME,
    DOC_HDX_DATASET_TITLE,
    DOC_HDX_PROVIDER_NAME,
    DOC_HDX_PROVIDER_STUB
)

from hdx_hapi.endpoints.models.hdx_metadata import DatasetResponse, ResourceResponse
from hdx_hapi.endpoints.util.util import OutputFormat, pagination_parameters
from hdx_hapi.services.csv_transform_logic import transform_result_to_csv_stream_if_requested
from hdx_hapi.services.dataset_logic import get_datasets_srv
from hdx_hapi.services.resource_logic import get_resources_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['HDX Metadata'],
)


@router.get('/api/dataset', response_model=List[DatasetResponse], summary='Get information about the sources of the data in HAPI')
async def get_datasets(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    hdx_id: Annotated[str, Query(max_length=36, description=f'{DOC_HDX_DATASET_ID}')] = None,
    hdx_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_DATASET_NAME}')] = None,
    title: Annotated[str, Query(max_length=1024, description=f'{DOC_HDX_DATASET_TITLE}')] = None,
    hdx_provider_stub: Annotated[str, Query(max_length=128, description=f'{DOC_HDX_PROVIDER_STUB}')] = None,
    hdx_provider_name: Annotated[str, Query(max_length=512, description=f'{DOC_HDX_PROVIDER_NAME}')] = None,
    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Get information about the <a href="https://data.humdata.org/dataset">HDX Datasets</a> that are used as data sources for HAPI. Datasets contain one or more resources, which are the sources of the data found in HAPI.
    """
    result = await get_datasets_srv(
        pagination_parameters=pagination_parameters,
        db=db,
        hdx_id=hdx_id,
        hdx_stub=hdx_stub,
        title=title,
        hdx_provider_stub=hdx_provider_stub,
        hdx_provider_name=hdx_provider_name,
    )
    return transform_result_to_csv_stream_if_requested(result, output_format, DatasetResponse)


@router.get('/api/resource', response_model=List[ResourceResponse])
async def get_resources(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    hdx_id: Annotated[str, Query(max_length=36, description='HDX Resource ID')] = None,
    format: Annotated[str, Query(max_length=32, description='HDX Resource format')] = None,
    update_date_min: Annotated[datetime | date, Query(description='Min date of update date, e.g. 2020-01-01 or 2020-01-01T00:00:00', example='2020-01-01')] = None,
    update_date_max: Annotated[datetime | date, Query(description='Max date of update date, e.g. 2024-12-31 or 2024-12-31T23:59:59', example='2024-12-31')] = None,
    is_hxl: Annotated[bool, Query(description='Is Resource HXL')] = None,
    dataset_hdx_id: Annotated[str, Query(max_length=36, description='HDX Dataset ID')] = None,
    dataset_hdx_stub: Annotated[str, Query(max_length=128, description='HDX Dataset name')] = None,
    dataset_title: Annotated[str, Query(max_length=1024, description='HDX Dataset title')] = None,
    dataset_hdx_provider_stub: Annotated[str, Query(max_length=128, description='Organization(provider) code')] = None,
    dataset_hdx_provider_name: Annotated[str, Query(max_length=512, description='Organization(provider) name')] = None,

    output_format: OutputFormat = OutputFormat.JSON,
):
    """
    Return the list of datasets
    """
    result = await get_resources_srv(
        pagination_parameters=pagination_parameters,
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

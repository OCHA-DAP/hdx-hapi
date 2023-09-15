from typing import List, Annotated, Dict
from fastapi import Depends, Query, APIRouter


from sqlalchemy.ext.asyncio import AsyncSession

from hdx_hapi.endpoints.models.dataset_view import DatasetViewPydantic
from hdx_hapi.endpoints.util.util import pagination_parameters
from hdx_hapi.services.dataset_logic import get_datasets_srv
from hdx_hapi.services.sql_alchemy_session import get_db

router = APIRouter(
    tags=['dataset'],
)

@router.get('/api/dataset', response_model=List[DatasetViewPydantic])
async def get_datasets(
    pagination_parameters: Annotated[dict, Depends(pagination_parameters)],
    db: AsyncSession = Depends(get_db),
    code: Annotated[str, Query(max_length=10, description='HDX Dataset ID or name')] = None,
    title: Annotated[str, Query(max_length=10, description='HDX Dataset title or display name')] = None,
    provider_code: Annotated[str, Query(max_length=10, description='Dataset ID given by provider')] = None,
    provider_name: Annotated[str, Query(max_length=10, description='Dataset name given by provider')] = None,
):
    """
    Return the list of datasets
    """
    result = await get_datasets_srv(pagination_parameters=pagination_parameters, db=db, code=code, title=title, provider_code=provider_code, provider_name=provider_name)
    return result

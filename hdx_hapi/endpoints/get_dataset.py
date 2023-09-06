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
    code: Annotated[str, Query(max_length=10)] = None,
    title: Annotated[str, Query(max_length=10)] = None,
    provider_code: Annotated[str, Query(max_length=10)] = None,
    provider_name: Annotated[str, Query(max_length=10)] = None,
):
    """
    This is the most important endpoint
    """
    result = await get_datasets_srv(pagination_parameters=pagination_parameters, db=db, code=code, title=title, provider_code=provider_code, provider_name=provider_name)
    return result

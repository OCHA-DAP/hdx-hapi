from enum import Enum
from typing import Annotated, Optional

from fastapi import Depends, Query
from pydantic import BaseModel, ConfigDict


_LIMIT_DESCRIPTION = 'Maximum number of records to return. The system will not return more than 10,000 records.'
_OFFSET_DESCRIPTION = (
    'Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.'
)
_APP_IDENTIFIER_DESCRIPTION = (
    'base64 encoded application name and email, as in `base64("app_name:email")`. '
    'This value can also be passed in the `X-HDX-HAPI-APP-IDENTIFIER` header. See the *encode_identifier* endpoint.'
)

app_name_identifier_query = Query(max_length=512, min_length=4, description='A name for the calling application')
email_identifier_query = Query(max_length=512, description='An email address')

pagination_limit_query = Query(ge=0, le=10000, example=1000, description=_LIMIT_DESCRIPTION)
pagination_offset_query = Query(ge=0, description=_OFFSET_DESCRIPTION)
common_app_identifier_query = Query(max_length=512, description=_APP_IDENTIFIER_DESCRIPTION)

class PaginationParams(BaseModel):
    offset: int = pagination_offset_query
    limit: int = pagination_limit_query

    model_config = ConfigDict(frozen=True)


class CommonEndpointParams(PaginationParams):
    app_identifier: Optional[str] = common_app_identifier_query


async def pagination_parameters(
    limit: Annotated[int, pagination_limit_query] = 10000,
    offset: Annotated[int, pagination_offset_query] = 0,
) -> PaginationParams:
    return PaginationParams(offset=offset, limit=limit)


async def common_endpoint_parameters(
    pagination_parameters: Annotated[PaginationParams, Depends(pagination_parameters)],
    app_identifier: Annotated[str, common_app_identifier_query] = None,
) -> CommonEndpointParams:
    return CommonEndpointParams(**pagination_parameters.model_dump(), app_identifier=app_identifier)


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'


class AdminLevel(str, Enum):
    ZERO = '0'
    ONE = '1'
    TWO = '2'

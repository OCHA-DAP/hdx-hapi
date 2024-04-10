from enum import Enum
from typing import Annotated

from fastapi import Query


_LIMIT_DESCRIPTION = 'Maximum number of records to return. The system will not return more than 10,000 records.'
_OFFSET_DESCRIPTION = (
    'Number of records to skip in the response. Use in conjunction with the limit parameter ' 'to paginate.'
)


async def pagination_parameters(
    limit: Annotated[int, Query(ge=0, le=10000, examples=[1000], description=_LIMIT_DESCRIPTION)] = 10000,
    offset: Annotated[int, Query(ge=0, description=_OFFSET_DESCRIPTION)] = 0,
):
    return {'offset': offset, 'limit': limit}


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'


class AdminLevel(str, Enum):
    ZERO = '0'
    ONE = '1'
    TWO = '2'

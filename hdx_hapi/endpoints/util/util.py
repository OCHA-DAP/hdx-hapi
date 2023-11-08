from enum import Enum
from typing import Annotated

from fastapi import Query


async def pagination_parameters(
    limit: Annotated[int, Query(ge=0, le=10000, example=1000, description='Maximum number of records to return. The system will not return more than 10,000 records.')] = 10000,
    offset: Annotated[int, Query(ge=0, description='Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.')] = 0
):
    return {"offset": offset, "limit": limit}


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'


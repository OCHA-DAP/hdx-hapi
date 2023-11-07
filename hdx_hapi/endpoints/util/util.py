from enum import Enum
from typing import Annotated

from fastapi import Query


async def pagination_parameters(
    offset: Annotated[int, Query(ge=0, description='Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.')] = 0, 
    limit: Annotated[int, Query(ge=0, le=10000, example=1000, description='Maximum number of records to return, up to 10,000.')] = 10000
):
    return {"offset": offset, "limit": limit}


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'


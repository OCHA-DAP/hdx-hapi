from enum import Enum
from typing import Annotated

from fastapi import Query


async def pagination_parameters(
    offset: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(ge=0, le=10000)] = 10000
):
    return {"offset": offset, "limit": limit}


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'


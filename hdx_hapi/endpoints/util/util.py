from enum import Enum
from re import T
from typing import Annotated

from fastapi import Query


async def pagination_parameters(
    offset: Annotated[int, Query(ge=0)] = 0, limit: Annotated[int, Query(ge=0, le=10000, example=1000)] = 10000
):
    return {"offset": offset, "limit": limit}


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'

class AdminLevel(str, Enum):
    ZERO = "0"
    ONE = "1"
    TWO = "2"

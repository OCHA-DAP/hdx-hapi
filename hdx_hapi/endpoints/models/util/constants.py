from decimal import Decimal
from typing import Annotated
from fastapi import Query
from pydantic import Field, PlainSerializer
from enum import Enum


PERCENTAGE_TYPE = Field(ge=0, le=100)

NON_NEGATIVE_DECIMAL_TYPE = Annotated[
    Decimal, PlainSerializer(lambda x: float(x), return_type=Annotated[float, Query(ge=0)])
]


class AdminLevelInt(int, Enum):
    ZERO = 0
    ONE = 1
    TWO = 2

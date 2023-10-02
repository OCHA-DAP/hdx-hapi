from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel


class AgeRangeViewPydantic(HapiBaseModel):
    code: str = Field(max_length=32)
    age_min: int = None
    age_max: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

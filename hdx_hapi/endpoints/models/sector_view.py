from pydantic import ConfigDict, Field
from typing import Optional
from datetime import datetime

from hdx_hapi.endpoints.models.base import HapiBaseModel


class SectorViewPydantic(HapiBaseModel):
    code: str = Field(max_length=32)
    name: str = Field(max_length=512)
    reference_period_start: datetime
    reference_period_end: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

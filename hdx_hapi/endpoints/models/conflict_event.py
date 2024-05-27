from hapi_schema.utils.enums import EventType
from pydantic import ConfigDict, Field, NaiveDatetime
from typing import Optional

from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class ConflictEventResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36)
    event_type: EventType
    events: Optional[int]
    fatalities: Optional[int]

    reference_period_start: NaiveDatetime
    reference_period_end: Optional[NaiveDatetime]

    model_config = ConfigDict(from_attributes=True)

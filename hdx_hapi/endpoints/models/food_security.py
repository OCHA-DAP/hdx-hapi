import datetime

from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_HDX_RESOURCE_ID,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    DOC_IPC_PHASE,
    DOC_IPC_TYPE,
    DOC_ADMIN2_REF,
    truncate_query_description,
)
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins


class FoodSecurityResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description=DOC_HDX_RESOURCE_ID)
    admin2_ref: int = Field(description=f'{DOC_ADMIN2_REF}')
    ipc_phase: str = Field(max_length=32, description=truncate_query_description(DOC_IPC_PHASE))
    ipc_type: str = Field(max_length=32, description=truncate_query_description(DOC_IPC_TYPE))
    population_in_phase: int = Field(description='The number of people in the IPC phase')
    population_fraction_in_phase: float = Field(description='The fraction of people in the IPC phase')
    reference_period_start: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)

import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hapi_schema.utils.enums import DTMAssessmentType
from hdx_hapi.config.doc_snippets import (
    truncate_query_description,
    DOC_HDX_RESOURCE_ID,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
)


class IdpsResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    # provider_admin1_name: str = Field(max_length=512,
    # description=truncate_query_description(DOC_PROVIDER_ADMIN1_NAME))
    # provider_admin2_name: str = Field(max_length=512,
    # description=truncate_query_description(DOC_PROVIDER_ADMIN2_NAME))
    reporting_round: int = Field(description='Placeholder text')
    assessment_type: DTMAssessmentType = Field(description='Placeholder text')
    population: int = Field(description='The number of people')
    reference_period_start: datetime.datetime = Field(
        description=truncate_query_description(DOC_REFERENCE_PERIOD_START)
    )
    reference_period_end: Optional[datetime.datetime] = Field(
        description=truncate_query_description(DOC_REFERENCE_PERIOD_END)
    )

    model_config = ConfigDict(from_attributes=True)

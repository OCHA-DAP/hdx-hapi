import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hapi_schema.utils.enums import DTMAssessmentType
from hdx_hapi.config.doc_snippets import (
    truncate_query_description,
    DOC_HDX_RESOURCE_ID,
    DOC_ADMIN1_REF,
    DOC_ADMIN2_REF,
    DOC_PROVIDER_ADMIN1_NAME,
    DOC_PROVIDER_ADMIN2_NAME,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
)


class IdpsResponse(HapiBaseModel):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    admin2_ref: int = Field(description=truncate_query_description(DOC_ADMIN2_REF))
    # provider_admin1_name: str = Field(max_length=512, description=truncate_query_description(DOC_PROVIDER_ADMIN1_NAME))
    # provider_admin2_name: str = Field(max_length=512, description=truncate_query_description(DOC_PROVIDER_ADMIN2_NAME))
    reporting_round: int = Field(description='Placeholder text')
    assessment_type: DTMAssessmentType = Field(description='Placeholder text')
    population: int = Field(ge=0, description='The number of people')
    reference_period_start: datetime.datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))
    admin1_code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))
    admin2_code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN2_CODE))
    admin2_name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN2_NAME))
    admin1_ref: int = Field(description=truncate_query_description(DOC_ADMIN1_REF))

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.config.doc_snippets import (
    DOC_LOCATION_NAME,
    DOC_LOCATION_CODE,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    truncate_query_description,
)


class LocationResponse(HapiBaseModel):
    # id: int
    code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_NAME))
    name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_CODE))

    reference_period_start: datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)


class Admin1Response(HapiBaseModel):
    # id: int
    # location_ref: int
    code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))
    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]
    reference_period_start: datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime] = Field(description=DOC_REFERENCE_PERIOD_END)
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    model_config = ConfigDict(from_attributes=True)


class Admin2Response(HapiBaseModel):
    # id: int
    # admin1_ref: int
    code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN2_CODE))
    name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN2_NAME))
    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]
    reference_period_start: datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    admin1_code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))

    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    model_config = ConfigDict(from_attributes=True)

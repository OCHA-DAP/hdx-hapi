from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN1_ID,
    DOC_ADMIN2_ID,
    DOC_ADMIN2_REF,
    DOC_LOCATION_HAS_HRP,
    DOC_LOCATION_ID,
    DOC_LOCATION_IN_GHO,
    DOC_LOCATION_NAME,
    DOC_LOCATION_CODE,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_LOCATION_REF,
    DOC_REFERENCE_PERIOD_START,
    DOC_REFERENCE_PERIOD_END,
    truncate_query_description,
)


class LocationResponse(HapiBaseModel):
    id: int = Field(description=truncate_query_description(DOC_LOCATION_ID))
    code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_NAME))
    name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_CODE))
    has_hrp: bool = Field(description=truncate_query_description(DOC_LOCATION_HAS_HRP))
    in_gho: bool = Field(description=truncate_query_description(DOC_LOCATION_IN_GHO))
    from_cods: bool

    reference_period_start: datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)


class Admin1Response(HapiBaseModel):
    id: int = Field(description=truncate_query_description(DOC_ADMIN1_ID))
    location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))
    code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))
    from_cods: bool
    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]
    reference_period_start: datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime] = Field(description=DOC_REFERENCE_PERIOD_END)
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))

    model_config = ConfigDict(from_attributes=True)


class Admin2Response(HapiBaseModel):
    id: int = Field(description=truncate_query_description(DOC_ADMIN2_ID))
    admin1_ref: int = Field(description=truncate_query_description(DOC_ADMIN2_REF))
    code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN2_CODE))
    name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN2_NAME))
    from_cods: bool
    # hapi_updated_date: datetime
    # hapi_replaced_date: Optional[datetime]
    reference_period_start: datetime = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    admin1_code: str = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: str = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))

    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))
    location_ref: int = Field(description=truncate_query_description(DOC_LOCATION_REF))

    model_config = ConfigDict(from_attributes=True)

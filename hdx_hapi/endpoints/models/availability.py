import datetime
from typing import Optional
from pydantic import ConfigDict, Field
from hdx_hapi.endpoints.models.base import HapiBaseModel
from hdx_hapi.config.doc_snippets import (
    truncate_query_description,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_CODE,
    DOC_ADMIN2_NAME,
)


class AvailabilityResponse(HapiBaseModel):
    category: str = Field(max_length=32, description='HAPI category')
    subcategory: str = Field(max_length=512, description='HAPI subcategory')
    location_code: str = Field(max_length=128, description=truncate_query_description(DOC_LOCATION_CODE))
    location_name: str = Field(max_length=512, description=truncate_query_description(DOC_LOCATION_NAME))
    admin1_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN1_CODE))
    admin1_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN1_NAME))
    admin2_code: Optional[str] = Field(max_length=128, description=truncate_query_description(DOC_ADMIN2_CODE))
    admin2_name: Optional[str] = Field(max_length=512, description=truncate_query_description(DOC_ADMIN2_NAME))
    hapi_updated_date: Optional[datetime.datetime] = Field(
        description='Date that datasets was last updated, e.g. 2020-01-01 or 2020-01-01T00:00:00'
    )

    model_config = ConfigDict(from_attributes=True)

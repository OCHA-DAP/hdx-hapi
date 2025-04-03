import datetime
from pydantic import ConfigDict, Field
from typing import Optional

from hdx_hapi.config.doc_snippets import (
    DOC_AGGREGATION_PERIOD,
    DOC_HDX_RESOURCE_ID,
    DOC_NUMBER_PIXELS,
    DOC_PROVIDER_ADMIN1_CODE,
    DOC_PROVIDER_ADMIN2_CODE,
    DOC_REFERENCE_PERIOD_END,
    DOC_REFERENCE_PERIOD_START,
    DOC_VERSION,
    truncate_query_description,
)
from hapi_schema.utils.enums import AggregationPeriod, Version
from hdx_hapi.endpoints.models.base import HapiBaseModel, HapiModelWithAdmins
from hdx_hapi.endpoints.models.util.constants import NON_NEGATIVE_DECIMAL_TYPE


class RainfallResponse(HapiBaseModel, HapiModelWithAdmins):
    resource_hdx_id: str = Field(max_length=36, description=truncate_query_description(DOC_HDX_RESOURCE_ID))
    aggregation_period: AggregationPeriod = Field(description=truncate_query_description(DOC_AGGREGATION_PERIOD))
    provider_admin1_code: Optional[str] = Field(
        max_length=128, description=truncate_query_description(DOC_PROVIDER_ADMIN1_CODE)
    )
    provider_admin2_code: Optional[str] = Field(
        max_length=128, description=truncate_query_description(DOC_PROVIDER_ADMIN2_CODE)
    )
    rainfall: NON_NEGATIVE_DECIMAL_TYPE
    rainfall_long_term_average: NON_NEGATIVE_DECIMAL_TYPE
    rainfall_anomaly_pct: NON_NEGATIVE_DECIMAL_TYPE

    number_pixels: Optional[int] = Field(description=DOC_NUMBER_PIXELS)
    version: Optional[Version] = Field(description=DOC_VERSION)

    reference_period_start: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_START)
    reference_period_end: Optional[datetime.datetime] = Field(description=DOC_REFERENCE_PERIOD_END)

    model_config = ConfigDict(from_attributes=True)

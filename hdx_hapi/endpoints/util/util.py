import datetime
from enum import Enum
from typing import Annotated, Optional

from fastapi import Depends, Query
from pydantic import BaseModel, ConfigDict, model_validator

from hdx_hapi.config.doc_snippets import (
    DOC_ADMIN_LEVEL_FILTER,
    DOC_ADMIN1_REF,
    DOC_ADMIN1_CODE,
    DOC_ADMIN1_NAME,
    DOC_ADMIN2_REF,
    DOC_ADMIN2_NAME,
    DOC_ADMIN2_CODE,
    DOC_LOCATION_REF,
    DOC_LOCATION_CODE,
    DOC_LOCATION_NAME,
    DOC_SEE_ADMIN1,
    DOC_SEE_LOC,
    DOC_SEE_ADMIN2,
    DOC_PROVIDER_ADMIN1_NAME,
    DOC_PROVIDER_ADMIN2_NAME,
)
from hdx_hapi.endpoints.util.exceptions import RequestParamsValidationError


class OutputFormat(str, Enum):
    CSV = 'csv'
    JSON = 'json'


class AdminLevel(str, Enum):
    ZERO = '0'
    ONE = '1'
    TWO = '2'


_LIMIT_DESCRIPTION = 'Maximum number of records to return. The system will not return more than 10,000 records.'
_OFFSET_DESCRIPTION = (
    'Number of records to skip in the response. Use in conjunction with the limit parameter to paginate.'
)
_APP_IDENTIFIER_DESCRIPTION = (
    'base64 encoded application name and email, as in `base64("app_name:email")`. '
    'This value can also be passed in the `X-HDX-HAPI-APP-IDENTIFIER` header. '
    'See the *encoded_app_identifier* endpoint.'
)


app_name_identifier_query = Query(max_length=512, min_length=4, description='A name for the calling application.')
email_identifier_query = Query(max_length=512, description='An email address.')

pagination_limit_query = Query(ge=0, le=10000, example=100, description=_LIMIT_DESCRIPTION)
pagination_offset_query = Query(ge=0, description=_OFFSET_DESCRIPTION)
common_app_identifier_query = Query(max_length=512, description=_APP_IDENTIFIER_DESCRIPTION)


class PaginationParams(BaseModel):
    offset: int = pagination_offset_query
    limit: int = pagination_limit_query

    model_config = ConfigDict(frozen=True)


class CommonEndpointParams(PaginationParams):
    output_format: OutputFormat = OutputFormat.JSON
    app_identifier: Optional[str] = common_app_identifier_query


async def pagination_parameters(
    limit: Annotated[int, pagination_limit_query] = 10000,
    offset: Annotated[int, pagination_offset_query] = 0,
) -> PaginationParams:
    return PaginationParams(offset=offset, limit=limit)


async def common_endpoint_parameters(
    pagination_parameters: Annotated[PaginationParams, Depends(pagination_parameters)],
    output_format: OutputFormat = OutputFormat.JSON,
    app_identifier: Annotated[Optional[str], common_app_identifier_query] = None,
) -> CommonEndpointParams:
    return CommonEndpointParams(**pagination_parameters.model_dump(), 
                                output_format=output_format, app_identifier=app_identifier)


class ReferencePeriodParameters(BaseModel):
    reference_period_start_min: Optional[datetime.datetime | datetime.date] = None
    reference_period_start_max: Optional[datetime.datetime | datetime.date] = None
    reference_period_end_min: Optional[datetime.datetime | datetime.date] = None
    reference_period_end_max: Optional[datetime.datetime | datetime.date] = None

    model_config = ConfigDict(frozen=True)


async def reference_period_parameters(
    reference_period_start_min: Annotated[
        Optional[datetime.datetime | datetime.date],
        Query(description='Min date of reference start date, e.g. 2020-01-01 or 2020-01-01T00:00:00'),
    ] = None,
    reference_period_start_max: Annotated[
        Optional[datetime.datetime | datetime.date],
        Query(description='Max date of reference start date, e.g. 2020-01-01 or 2020-01-01T00:00:00'),
    ] = None,
    reference_period_end_min: Annotated[
        Optional[datetime.datetime | datetime.date],
        Query(description='Min date of reference end date, e.g. 2020-01-01 or 2020-01-01T00:00:00'),
    ] = None,
    reference_period_end_max: Annotated[
        Optional[datetime.datetime | datetime.date],
        Query(description='Max date of reference end date, e.g. 2020-01-01 or 2020-01-01T00:00:00'),
    ] = None,
) -> ReferencePeriodParameters:
    return ReferencePeriodParameters(
        reference_period_start_min=reference_period_start_min,
        reference_period_start_max=reference_period_start_max,
        reference_period_end_min=reference_period_end_min,
        reference_period_end_max=reference_period_end_max,
    )


class CommonLocationParameters(BaseModel):
    location_code: Optional[str] = None
    location_name: Optional[str] = None
    location_ref: Optional[int] = None
    admin1_code: Optional[str] = None
    admin1_name: Optional[str] = None
    admin1_ref: Optional[int] = None
    provider_admin1_name: Optional[str] = None
    admin2_code: Optional[str] = None
    admin2_name: Optional[str] = None
    admin2_ref: Optional[int] = None
    provider_admin2_name: Optional[str] = None
    admin_level: Optional[AdminLevel] = None

    model_config = ConfigDict(frozen=True)

    @model_validator(mode='after')
    def validate_names(self) -> 'CommonLocationParameters':
        if self.admin_level == AdminLevel.ONE and self.provider_admin2_name:
            raise RequestParamsValidationError('Cannot specify provider_admin2_name and admin level 1 filter')
        elif self.admin_level == AdminLevel.ZERO and self.provider_admin2_name:
            raise RequestParamsValidationError('Cannot specify provider_admin2_name and admin level 0 filter')
        elif self.admin_level == AdminLevel.ZERO and self.provider_admin1_name:
            raise RequestParamsValidationError('Cannot specify provider_admin1_name and admin level 0 filter')
        return self


async def common_location_parameters(
    location_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_LOCATION_CODE} {DOC_SEE_LOC}')
    ] = None,
    location_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_LOCATION_NAME} {DOC_SEE_LOC}')
    ] = None,
    location_ref: Annotated[Optional[int], Query(description=f'{DOC_LOCATION_REF}')] = None,
    admin1_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN1_CODE} {DOC_SEE_ADMIN1}')
    ] = None,
    admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN1_NAME} {DOC_SEE_ADMIN1}')
    ] = None,
    admin1_ref: Annotated[Optional[int], Query(description=f'{DOC_ADMIN1_REF}')] = None,
    provider_admin1_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_PROVIDER_ADMIN1_NAME}')
    ] = None,
    admin2_code: Annotated[
        Optional[str], Query(max_length=128, description=f'{DOC_ADMIN2_CODE} {DOC_SEE_ADMIN2}')
    ] = None,
    admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_ADMIN2_NAME} {DOC_SEE_ADMIN2}')
    ] = None,
    admin2_ref: Annotated[Optional[int], Query(description=f'{DOC_ADMIN2_REF}')] = None,
    provider_admin2_name: Annotated[
        Optional[str], Query(max_length=512, description=f'{DOC_PROVIDER_ADMIN2_NAME}')
    ] = None,
    admin_level: Annotated[Optional[AdminLevel], Query(description=DOC_ADMIN_LEVEL_FILTER)] = None,
) -> CommonLocationParameters:
    return CommonLocationParameters(
        location_code=location_code,
        location_name=location_name,
        location_ref=location_ref,
        admin1_code=admin1_code,
        admin1_name=admin1_name,
        admin1_ref=admin1_ref,
        provider_admin1_name=provider_admin1_name,
        admin2_code=admin2_code,
        admin2_name=admin2_name,
        admin2_ref=admin2_ref,
        provider_admin2_name=provider_admin2_name,
        admin_level=admin_level,
    )

import datetime
from typing import Optional, Protocol, Type
from sqlalchemy import Select, or_, and_
from sqlalchemy.orm import Mapped

from hdx_hapi.config.config import get_config
from hdx_hapi.endpoints.util.util import (
    AdminLevel,
    CommonDateRangeParams,
    CommonLocationParameters,
    PaginationParams,
    ReferencePeriodParameters,
)

CONFIG = get_config()


def apply_pagination(query: Select, pagination_parameters: PaginationParams) -> Select:
    offset = pagination_parameters.offset
    limit = pagination_parameters.limit
    if not offset:
        offset = 0
    if not limit:
        limit = 1000

    return query.limit(limit).offset(offset)


class EntityWithDateRangeFilter(Protocol):
    start_date: Mapped[str]
    end_date: Mapped[str]
    reference_period_start: Mapped[datetime.datetime]
    reference_period_end: Mapped[datetime.datetime]


def apply_date_range_filter(
    query: Select,
    db_class: Type[EntityWithDateRangeFilter],
    common_date_range_params: CommonDateRangeParams,
) -> Select:
    start_date = common_date_range_params.start_date
    end_date = common_date_range_params.end_date

    if start_date:
        query = query.filter(or_(db_class.reference_period_end >= start_date, db_class.reference_period_end.is_(None)))
    if end_date:
        query = query.filter(db_class.reference_period_start < end_date)

    return query


class EntityWithReferencePeriod(Protocol):
    reference_period_start: Mapped[datetime.datetime]
    reference_period_end: Mapped[datetime.datetime]


def apply_reference_period_filter(
    query: Select,
    ref_period_parameters: Optional[ReferencePeriodParameters],
    db_class: Type[EntityWithReferencePeriod],
) -> Select:
    if ref_period_parameters is None:
        return query

    if ref_period_parameters.reference_period_start_min:
        query = query.where(db_class.reference_period_start >= ref_period_parameters.reference_period_start_min)
    if ref_period_parameters.reference_period_start_max:
        query = query.where(db_class.reference_period_start < ref_period_parameters.reference_period_start_max)
    if ref_period_parameters.reference_period_end_min:
        query = query.where(db_class.reference_period_end >= ref_period_parameters.reference_period_end_min)
    if ref_period_parameters.reference_period_end_max:
        query = query.where(db_class.reference_period_end < ref_period_parameters.reference_period_end_max)
    return query


class EntityWithLocationAdmin(Protocol):
    location_ref: Mapped[int]
    location_code: Mapped[str]
    location_name: Mapped[str]
    has_hrp: Mapped[bool]
    in_gho: Mapped[bool]
    admin1_ref: Mapped[int]
    admin1_code: Mapped[str]
    admin1_name: Mapped[str]
    provider_admin1_name: Mapped[str]
    admin1_is_unspecified: Mapped[bool]
    admin2_ref: Mapped[int]
    admin2_code: Mapped[str]
    admin2_name: Mapped[str]
    provider_admin2_name: Mapped[str]
    admin2_is_unspecified: Mapped[bool]


def apply_location_admin_filter(
    query: Select,
    db_class: Type[EntityWithLocationAdmin],
    common_location_parameters: CommonLocationParameters,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
) -> Select:
    location_ref = common_location_parameters.location_ref
    location_code = common_location_parameters.location_code
    location_name = common_location_parameters.location_name
    admin1_ref = common_location_parameters.admin1_ref
    admin1_code = common_location_parameters.admin1_code
    admin1_name = common_location_parameters.admin1_name
    provider_admin1_name = common_location_parameters.provider_admin1_name
    admin2_ref = common_location_parameters.admin2_ref
    admin2_code = common_location_parameters.admin2_code
    admin2_name = common_location_parameters.admin2_name
    provider_admin2_name = common_location_parameters.provider_admin2_name
    admin_level = common_location_parameters.admin_level

    if location_ref:
        query = query.where(db_class.location_ref == location_ref)
    if location_code:
        query = case_insensitive_filter(query, db_class.location_code, location_code)
    if location_name:
        query = query.where(db_class.location_name.icontains(location_name))
    if admin1_ref:
        query = query.where(db_class.admin1_ref == admin1_ref)
    if admin1_code:
        query = case_insensitive_filter(query, db_class.admin1_code, admin1_code)
    if admin1_name:
        query = query.where(db_class.admin1_name.icontains(admin1_name))
    # if provider_admin1_name_is_unspecified:
    #     query = query.where(or_(db_class.provider_admin1_name == '', db_class.provider_admin1_name.is_(None)))
    if provider_admin1_name:
        query = query.where(db_class.provider_admin1_name.icontains(provider_admin1_name))
    if admin2_ref:
        query = query.where(db_class.admin2_ref == admin2_ref)
    if admin2_code:
        query = case_insensitive_filter(query, db_class.admin2_code, admin2_code)
    if admin2_name:
        query = query.where(db_class.admin2_name.icontains(admin2_name))
    # if provider_admin2_name_is_unspecified:
    #     query = query.where(or_(db_class.provider_admin2_name == '', db_class.provider_admin2_name.is_(None)))
    if provider_admin2_name:
        query = query.where(db_class.provider_admin2_name.icontains(provider_admin2_name))
    # if admin1_is_unspecified is not None:
    #     query = query.where(db_class.admin1_is_unspecified == admin1_is_unspecified)
    # if admin2_is_unspecified is not None:
    #     query = query.where(db_class.admin2_is_unspecified == admin2_is_unspecified)
    if has_hrp is not None:
        query = query.where(db_class.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(db_class.in_gho == in_gho)

    if AdminLevel.TWO == admin_level:
        query = query.where(or_(db_class.admin2_is_unspecified == False, db_class.provider_admin2_name != ''))
    elif AdminLevel.ONE == admin_level:
        query = query.where(and_(db_class.admin2_is_unspecified == True, db_class.provider_admin2_name == ''))
        query = query.where(or_(db_class.admin1_is_unspecified == False, db_class.provider_admin1_name != ''))
    elif AdminLevel.ZERO == admin_level:
        query = query.where(and_(db_class.admin1_is_unspecified == True, db_class.provider_admin1_name == ''))

    return query


def case_insensitive_filter(query: Select, column: Mapped[str], value: str) -> Select:
    query = query.where(column.ilike(value))
    return query

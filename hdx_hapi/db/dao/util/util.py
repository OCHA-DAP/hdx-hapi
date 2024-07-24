from typing import Optional, Protocol, Type
from sqlalchemy import DateTime, Select
from sqlalchemy.orm import Mapped

from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


def apply_pagination(query: Select, pagination_parameters: PaginationParams) -> Select:
    offset = pagination_parameters.offset
    limit = pagination_parameters.limit
    if not offset:
        offset = 0
    if not limit:
        limit = 1000

    return query.limit(limit).offset(offset)


class EntityWithReferencePeriod(Protocol):
    reference_period_start: Mapped[DateTime]
    reference_period_end: Mapped[DateTime]


def apply_reference_period_filter(
    query: Select,
    ref_period_parameters: ReferencePeriodParameters,
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
    admin1_is_unspecified: Mapped[bool]
    admin2_ref: Mapped[int]
    admin2_code: Mapped[str]
    admin2_name: Mapped[str]
    admin2_is_unspecified: Mapped[bool]


def apply_location_admin_filter(
    query: Select,
    db_class: Type[EntityWithLocationAdmin],
    location_ref: Optional[int] = None,
    location_code: Optional[str] = None,
    location_name: Optional[str] = None,
    has_hrp: Optional[bool] = None,
    in_gho: Optional[bool] = None,
    admin1_ref: Optional[int] = None,
    admin1_code: Optional[str] = None,
    admin1_name: Optional[str] = None,
    admin1_is_unspecified: Optional[bool] = None,
    admin2_ref: Optional[int] = None,
    admin2_code: Optional[str] = None,
    admin2_name: Optional[str] = None,
    admin2_is_unspecified: Optional[bool] = None,
) -> Select:
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
    if admin2_ref:
        query = query.where(db_class.admin2_ref == admin2_ref)
    if admin2_code:
        query = case_insensitive_filter(query, db_class.admin2_code, admin2_code)
    if admin2_name:
        query = query.where(db_class.admin2_name.icontains(admin2_name))
    if admin1_is_unspecified is not None:
        query = query.where(db_class.admin1_is_unspecified == admin1_is_unspecified)
    if admin2_is_unspecified is not None:
        query = query.where(db_class.admin2_is_unspecified == admin2_is_unspecified)
    if has_hrp is not None:
        query = query.where(db_class.has_hrp == has_hrp)
    if in_gho is not None:
        query = query.where(db_class.in_gho == in_gho)

    return query


def case_insensitive_filter(query: Select, column: Mapped[str], value: str) -> Select:
    query = query.where(column.ilike(value))
    return query

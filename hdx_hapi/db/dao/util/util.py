from typing import Protocol, Type
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
    if ref_period_parameters.reference_period_start_min:
        query = query.where(db_class.reference_period_start >= ref_period_parameters.reference_period_start_min)
    if ref_period_parameters.reference_period_start_max:
        query = query.where(db_class.reference_period_start < ref_period_parameters.reference_period_start_max)
    if ref_period_parameters.reference_period_end_min:
        query = query.where(db_class.reference_period_end >= ref_period_parameters.reference_period_end_min)
    if ref_period_parameters.reference_period_end_max:
        query = query.where(db_class.reference_period_end < ref_period_parameters.reference_period_end_max)
    return query


def case_insensitive_filter(query: Select, column: Mapped[str], value: str) -> Select:
    query = query.where(column.ilike(value))
    return query

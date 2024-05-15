from typing import Type
from sqlalchemy import Column, Select

from hdx_hapi.db.models.views.all_views import Admin1View, Admin2View, LocationView
from hdx_hapi.endpoints.util.util import PaginationParams, ReferencePeriodParameters


def apply_pagination(query: Select, pagination_parameters: PaginationParams) -> Select:
    offset = pagination_parameters.offset
    limit = pagination_parameters.limit
    if not offset:
        offset = 0
    if not limit:
        limit = 1000

    return query.limit(limit).offset(offset)


def apply_reference_period_filter(
    query: Select,
    ref_period_parameters: ReferencePeriodParameters,
    db_class: Type[LocationView] | Type[Admin1View] | Type[Admin2View],
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


def case_insensitive_filter(query: Select, column: Column, value: str) -> Select:
    query = query.where(column.ilike(value))
    return query

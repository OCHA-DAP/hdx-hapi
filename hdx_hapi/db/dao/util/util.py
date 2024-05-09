from sqlalchemy import Column, Select

from hdx_hapi.endpoints.util.util import PaginationParams


def apply_pagination(query: Select, pagination_parameters: PaginationParams) -> Select:
    offset = pagination_parameters.offset
    limit = pagination_parameters.limit
    if not offset:
        offset = 0
    if not limit:
        limit = 1000

    return query.limit(limit).offset(offset)


def case_insensitive_filter(query: Select, column: Column, value: str) -> Select:
    query = query.where(column.ilike(value))
    return query

from typing import Dict
from sqlalchemy import Select

def apply_pagination(query: Select, pagination_parameters: Dict) -> Select:
    offset = pagination_parameters.get('offset')
    limit = pagination_parameters.get('limit')
    if not offset:
        offset = 0
    if not limit:
        limit = 1000

    return query.limit(limit).offset(offset)

def case_insensitive_filter(query: Select, column, value) -> Select:
    query = query.where(column.ilike(value))
    return query

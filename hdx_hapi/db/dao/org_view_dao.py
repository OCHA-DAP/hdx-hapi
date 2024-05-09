import logging

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_org_view import OrgView
from hdx_hapi.db.dao.util.util import apply_pagination, case_insensitive_filter
from hdx_hapi.endpoints.util.util import PaginationParams

logger = logging.getLogger(__name__)


async def orgs_view_list(
    pagination_parameters: PaginationParams,
    db: AsyncSession,
    acronym: str = None,
    name: str = None,
    org_type_code: str = None,
    org_type_description: str = None,
):
    logger.info(
        f'orgs_view_list called with params: acronym={acronym}, name={name}, org_type_code={org_type_code}, '
        f'org_type_description={org_type_description}'
    )

    query = select(OrgView)
    if acronym:
        query = case_insensitive_filter(query, OrgView.acronym, acronym)
    if name:
        query = query.where(OrgView.name.icontains(name))
    if org_type_code:
        query = query.where(OrgView.org_type_code == org_type_code)
    if org_type_description:
        query = query.where(OrgView.org_type_description.icontains(org_type_description))

    query = apply_pagination(query, pagination_parameters)

    logger.debug(f'Executing SQL query: {query}')

    result = await db.execute(query)
    orgs = result.scalars().all()

    logger.info(f'Retrieved {len(orgs)} rows from the database')

    return orgs

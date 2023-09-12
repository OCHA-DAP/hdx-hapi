from typing import Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from hdx_hapi.db.models.views.db_org_type_view import OrgTypeView
from hdx_hapi.db.dao.util.util import apply_pagination

async def org_types_view_list(
    pagination_parameters: Dict,
    db: AsyncSession,
    code: str = None,
    description: str = None,
):

    query = select(OrgTypeView)
    if code:
        query = query.where(OrgTypeView.code == code)
    if description:
        query = query.where(OrgTypeView.description.icontains(description))

    query = apply_pagination(query, pagination_parameters)

    result = await db.execute(query)
    locations = result.scalars().all()
    return locations
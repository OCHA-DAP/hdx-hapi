from enum import Enum

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import IntegrityError

from hdx_hapi.db.models.dbdataset import DBDataset

RESULT_STATES = Enum('RESULT_STATES', ['OK', 'INTEGRITY_ERROR'])

async def delete_dataset_srv(id: int, db: AsyncSession) -> :
    try:
        query = select(DBDataset).options(selectinload(DBDataset.resources)).where(DBDataset.id == id)
        result = await db.execute(query)
        dataset1 = result.scalar_one()
        await db.delete(dataset1)
        await db.commit()
        return RESULT_STATES.OK
        return {'message': 'Deleted'}
    except IntegrityError:
        return RESULT_STATES.INTEGRITY_ERROR
        

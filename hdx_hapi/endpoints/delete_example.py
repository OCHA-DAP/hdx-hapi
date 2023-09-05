
from fastapi import status, Depends, HTTPException

from sqlalchemy.ext.asyncio import AsyncSession

from main import app
from hdx_hapi.services.delete_example_logic import delete_dataset_srv, RESULT_STATES
from hdx_hapi.services.sql_alchemy_session import get_db
from hdx_hapi.endpoints.models.http_409_message import HTTP409Message

@app.get(
    '/dataset_delete/{id}',
    responses={status.HTTP_409_CONFLICT: {'description': 'Db integrity err', 'model': HTTP409Message}},
)
async def delete_dataset(id: int, db: AsyncSession = Depends(get_db)):
    result = await delete_dataset_srv(id, db)
    if result == RESULT_STATES.OK:
        return {'message': 'Deleted'}
    elif result == RESULT_STATES.INTEGRITY_ERROR:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail='Deletion of dataset would cause a db integrity error'
        )
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Unexpected server error'
        )


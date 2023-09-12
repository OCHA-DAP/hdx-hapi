import logging
import logging.config
logging.config.fileConfig('logging.conf')

import uvicorn
from fastapi import FastAPI

from hdx_hapi.services.sql_alchemy_session import init_db

from hdx_hapi.endpoints.get_operational_presence import router as operational_presence_router
from hdx_hapi.endpoints.get_location import router as location_router
from hdx_hapi.endpoints.get_dataset import router as dataset_router
from hdx_hapi.endpoints.get_admin2 import router as admin2_router
from hdx_hapi.endpoints.get_admin1 import router as admin1_router
from hdx_hapi.endpoints.get_org import router as org_router
# from hdx_hapi.endpoints.delete_example import delete_dataset

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(operational_presence_router)
app.include_router(location_router)
app.include_router(dataset_router)
app.include_router(admin2_router)
app.include_router(admin1_router)
app.include_router(org_router)

@app.on_event('startup')
async def startup():
    # await init_db()
    # await populate_db()
    pass

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0',port=8844)

import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from hdx_hapi.config.config import get_config

from hdx_hapi.db.models.base import Base
from hdx_hapi.db.models.db_admin1 import DBAdmin1
from hdx_hapi.db.models.db_admin2 import DBAdmin2
from hdx_hapi.db.models.db_location import DBLocation
from hdx_hapi.db.models.db_age_range import DBAgeRange
from hdx_hapi.db.models.db_gender import DBGender
from hdx_hapi.db.models.db_dataset import DBDataset
from hdx_hapi.db.models.db_resource import DBResource
from hdx_hapi.db.models.db_admin2 import DBAdmin2
from hdx_hapi.db.models.db_org import DBOrg
from hdx_hapi.db.models.db_orgtype import DBOrgType
from hdx_hapi.db.models.db_sector import DBSector

from hdx_hapi.db.models.db_operational_presence import DBOperationalPresence
from hdx_hapi.db.models.db_population import DBPopulation


logger = logging.getLogger(__name__)

CONFIG = get_config()
# Create an AsyncEngine
engine = create_async_engine(
    CONFIG.SQL_ALCHEMY_ASYNCPG_DB_URI,
    echo=True, pool_size=10
)

# Create a custom Session class
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
    future=True
)


async def get_db() -> AsyncSession:
    session = AsyncSessionLocal()
    try:
        # logger.info(f'Using the following sql alchemy uri: {get_config().SQL_ALCHEMY_ASYNCPG_DB_URI}')
        logger.info('Yielding new session')
        yield session
    finally:
        await session.close()
        logger.info('Session closed')


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
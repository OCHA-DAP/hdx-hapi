from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from hdx_hapi.db.models import Base
from hdx_hapi.db.models.dbadmin1 import DBAdmin1
from hdx_hapi.db.models.dbadmin2 import DBAdmin2
from hdx_hapi.db.models.dblocation import DBLocation
from hdx_hapi.db.models.dbagerange import DBAgeRange
from hdx_hapi.db.models.dbgender import DBGender
from hdx_hapi.db.models.dbdataset import DBDataset
from hdx_hapi.db.models.dbresource import DBResource
from hdx_hapi.db.models.dbadmin2 import DBAdmin2
from hdx_hapi.db.models.dborg import DBOrg
from hdx_hapi.db.models.dborgtype import DBOrgType
from hdx_hapi.db.models.dbsector import DBSector

from hdx_hapi.db.models.dboperationalpresence import DBOperationalPresence
from hdx_hapi.db.models.dbpopulation import DBPopulation

# Create an AsyncEngine
engine = create_async_engine(
    "postgresql+asyncpg://hapi:hapi@db:5432/hapi", echo=True, pool_size=10)

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
        yield session
    finally:
        await session.close()


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
import logging

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from hdx_hapi.config.config import get_config

from hdx_hapi.db.models.base import Base

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
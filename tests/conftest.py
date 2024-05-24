import asyncio
import pytest
import os
import logging


from logging import Logger
from sqlalchemy import Engine, MetaData, create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, Session
from typing import List

from hapi_schema.db_admin1 import view_params_admin1
from hapi_schema.db_admin2 import view_params_admin2
from hapi_schema.db_dataset import view_params_dataset
from hapi_schema.db_food_security import view_params_food_security
from hapi_schema.db_funding import view_params_funding
from hapi_schema.db_humanitarian_needs import view_params_humanitarian_needs
from hapi_schema.db_location import view_params_location
from hapi_schema.db_national_risk import view_params_national_risk
from hapi_schema.db_operational_presence import view_params_operational_presence
from hapi_schema.db_org_type import view_params_org_type
from hapi_schema.db_org import view_params_org
from hapi_schema.db_population import view_params_population
from hapi_schema.db_refugees import view_params_refugees
from hapi_schema.db_resource import view_params_resource
from hapi_schema.db_sector import view_params_sector
from hapi_schema.db_conflict_event import view_params_conflict_event
from hapi_schema.db_poverty_rate import view_params_poverty_rate

from hdx_hapi.config.config import get_config
from hdx_hapi.db.models.base import Base
from hdx_hapi.db.models.views.util.util import CreateView

SAMPLE_DATA_SQL_FILES = [
    'tests/sample_data/location_admin.sql',
    'tests/sample_data/sector.sql',
    'tests/sample_data/org_type.sql',
    'tests/sample_data/org.sql',
    'tests/sample_data/dataset_resource.sql',
    'tests/sample_data/population.sql',
    'tests/sample_data/operational_presence.sql',
    'tests/sample_data/funding.sql',
    'tests/sample_data/conflict_event.sql',
    'tests/sample_data/national_risk.sql',
    'tests/sample_data/humanitarian_needs.sql',
    'tests/sample_data/refugees.sql',
    'tests/sample_data/poverty_rate.sql',
    'tests/sample_data/food_security.sql',
]

VIEW_LIST = [
    view_params_admin1,
    view_params_admin2,
    view_params_location,
    view_params_dataset,
    view_params_food_security,
    view_params_funding,
    view_params_humanitarian_needs,
    view_params_national_risk,
    view_params_operational_presence,
    view_params_org_type,
    view_params_org,
    view_params_population,
    view_params_refugees,
    view_params_resource,
    view_params_sector,
    view_params_conflict_event,
    view_params_poverty_rate,
]


def pytest_sessionstart(session):
    os.environ['HAPI_DB_NAME'] = 'hapi_test'
    os.environ['HAPI_IDENTIFIER_FILTERING'] = 'False'
    os.environ['HDX_MIXPANEL_TOKEN'] = 'fake_token'

    engine = create_engine(
        get_config().SQL_ALCHEMY_PSYCOPG2_DB_URI,
    )
    _drop_tables_and_views(engine)
    _create_tables_and_views(engine)


def _create_tables_and_views(engine: Engine):
    Base.metadata.create_all(engine)
    with engine.connect() as conn:
        for v in VIEW_LIST:
            conn.execute(CreateView(v.name, v.selectable))
            conn.commit()


def _drop_tables_and_views(engine: Engine):
    # drop views
    inspector = inspect(engine)
    views = inspector.get_view_names()
    with engine.connect() as conn:
        for view in views:
            conn.execute(text(f'DROP VIEW IF EXISTS {view}'))
            conn.commit()

    # drop tables
    metadata = MetaData()
    metadata.reflect(bind=engine)
    metadata.drop_all(bind=engine)


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session')
def log():
    return logging.getLogger(__name__)


@pytest.fixture(scope='session')
def session_maker() -> sessionmaker[Session]:
    # we don't want to import get_config before env vars are set for tests in pytest_sessionstart method
    from hdx_hapi.config.config import get_config

    engine = create_engine(
        get_config().SQL_ALCHEMY_PSYCOPG2_DB_URI,
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal


@pytest.fixture(scope='session')
def list_of_db_tables(log: Logger, session_maker: sessionmaker[Session]) -> List[str]:
    log.info('Getting list of db tables')
    session = session_maker()
    try:
        result = session.execute(text("SELECT tablename FROM pg_tables WHERE schemaname = 'public'"))
        return [row[0] for row in result if row != 'alembic_version']
    except Exception as e:
        raise e
    finally:
        session.close()


@pytest.fixture(scope='function')
def clear_db_tables(log: Logger, session_maker: sessionmaker[Session], list_of_db_tables: List[str]):
    log.info('Clearing database')
    db_session = session_maker()
    try:
        for table in list_of_db_tables:
            db_session.execute(text(f'TRUNCATE TABLE {table} CASCADE;'))
        db_session.commit()
    except Exception as e:
        log.error(f'Error while clearing test data: {str(e).splitlines()[0]}')
        db_session.rollback()
        raise e
    finally:
        db_session.close()


@pytest.fixture(scope='function')
def populate_test_data(log: Logger, session_maker: sessionmaker[Session]):
    log.info('Populating with test data')
    db_session = session_maker()
    try:
        for sample_file in SAMPLE_DATA_SQL_FILES:
            log.info(f'Starting data insert from {sample_file}')
            with open(sample_file, 'r') as file:
                sql_commands = file.read()
                db_session.execute(text(sql_commands))
                db_session.commit()
                log.info(f'Test data inserted successfully from {sample_file}')
    except Exception as e:
        log.error(f'Error while inserting test data: {str(e).splitlines()[0]}')
        db_session.rollback()
        raise e
    finally:
        db_session.close()


@pytest.fixture(scope='function')
def refresh_db(clear_db_tables, populate_test_data):
    pass


@pytest.fixture(scope='function')
def enable_hapi_identifier_filtering():
    import hdx_hapi.config.config as config

    initial_config_id_filtering = config.CONFIG.HAPI_IDENTIFIER_FILTERING
    config.CONFIG.HAPI_IDENTIFIER_FILTERING = True
    yield
    config.CONFIG.HAPI_IDENTIFIER_FILTERING = initial_config_id_filtering

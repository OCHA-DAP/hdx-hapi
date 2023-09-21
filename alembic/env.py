from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from hdx_hapi.config.helper import create_pg_uri_from_env_without_protocol

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

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
target_metadata = Base.metadata
# target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def _get_db_uri() -> str:
    db_url_dict = context.get_x_argument("sqlalchemy.url")
    db_url = db_url_dict.get('sqlalchemy.url') if db_url_dict else None
    if not db_url:
        db_url = f'postgresql+psycopg2://{create_pg_uri_from_env_without_protocol()}'
    # print(f'My db url is {x_url}')
    return db_url


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    custom_db_url = _get_db_uri()
    url = custom_db_url if custom_db_url else config.get_main_option("sqlalchemy.url")
    # print(f'My db url is {custom_db_url}')
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    # x_url = context.get_x_argument("sqlalchemy.url")
    # db_engine_config = x_url if x_url else config.get_section(config.config_ini_section, {})
    db_engine_config = config.get_section(config.config_ini_section, {})
    custom_db_uri = _get_db_uri()
    if custom_db_uri:
        db_engine_config['sqlalchemy.url'] = custom_db_uri
    # print(f'My db url is {db_engine_config}')
    connectable = engine_from_config(
        db_engine_config,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

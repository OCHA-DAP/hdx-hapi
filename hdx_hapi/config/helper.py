import os


def create_pg_uri_from_env_without_protocol():
    hapi_db_name = os.getenv('HAPI_DB_NAME', 'hapi')
    hapi_db_user = os.getenv('HAPI_DB_USER', 'hapi')
    hapi_db_pass = os.getenv('HAPI_DB_PASS', 'hapi')
    hapi_db_host = os.getenv('HAPI_DB_HOST', 'db')
    hapi_db_port = int(os.getenv('HAPI_DB_PORT', 5432))

    sql_alchemy_asyncypg_db_uri = \
        f'{hapi_db_user}:{hapi_db_pass}@{hapi_db_host}:{hapi_db_port}/{hapi_db_name}'
    return sql_alchemy_asyncypg_db_uri
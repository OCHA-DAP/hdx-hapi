#!/bin/sh
DB_NAME="${HAPI_DB_NAME:-hapi}"
DB_USER="${HAPI_DB_USER:-hapi}"
DB_PASS="${HAPI_DB_PASSWORD:-hapi}"
DB_HOST="${HAPI_DB_HOST:-db}"
DB_PORT="${HAPI_DB_PORT:-5432}"
ALEMBIC_COMMIT="${ALEMBIC_COMMIT:-head}"

DCOMPOSE="${DCOMPOSE:-docker-compose}"

cd docker
$DCOMPOSE exec -T db psql -U postgres -c "create database $DB_NAME with encoding 'UTF8';"
$DCOMPOSE exec -T db psql -U postgres -c "create user $DB_USER with encrypted password '$DB_PASS';"
$DCOMPOSE exec -T db psql -U postgres -c "grant all privileges on database $DB_NAME to $DB_USER;"

$DCOMPOSE exec -T db psql -U postgres $DB_NAME -c "GRANT USAGE, CREATE ON SCHEMA public TO $DB_USER;"
$DCOMPOSE exec -T db psql -U postgres $DB_NAME -c "GRANT ALL ON ALL TABLES IN SCHEMA public TO $DB_USER;"

# DCOMPOSE exec -T hwa sh -c "alembic -x sqlalchemy.url=postgresql+psycopg2://$DB_USER:$DB_PASS@$DB_HOST:$DB_PORT/$DB_NAME upgrade $ALEMBIC_COMMIT"

cd ..
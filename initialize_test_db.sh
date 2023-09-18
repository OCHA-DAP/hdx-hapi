#!/bin/sh
DB_NAME="${1:-hapi_test}"

cd docker
docker-compose exec db psql -U postgres -c "create database $DB_NAME with encoding 'UTF8';"
docker-compose exec db psql -U postgres -c "create user hapi with encrypted password 'hapi';"
docker-compose exec db psql -U postgres -c "grant all privileges on database hapi to hapi;"

docker-compose exec db psql -U postgres $DB_NAME -c "GRANT USAGE, CREATE ON SCHEMA public TO hapi;"
docker-compose exec db psql -U postgres $DB_NAME -c "GRANT ALL ON ALL TABLES IN SCHEMA public TO hapi;"

docker-compose exec hapi sh -c "alembic -x sqlalchemy.url=postgresql+psycopg2://hapi:hapi@db:5432/$DB_NAME upgrade 5ea41"

cd ..
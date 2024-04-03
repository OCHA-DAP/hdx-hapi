#!/bin/bash

# Check if correct number of arguments was passed
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <Dump File URL or Path> <Database Name>"
  echo "Example: ./restore_database.sh https://github.com/OCHA-DAP/hapi-pipelines/raw/db-export/database/hapi_db.pg_restore hapi"
  exit 1
fi

# Assign parameters to variables
DUMP_SOURCE=$1
DATABASE_NAME=$2
DUMP_FILE_NAME="postgres_dump.pg_restore"
HOST_DUMP_FILE_NAME="postgres_dump.pg_restore"
CONTAINER_DB_PATH="/var/lib/pgsql"

# Execute commands inside the ./docker directory
pushd ./docker || exit

# Determine if DUMP_SOURCE is a URL or a local path
if [[ $DUMP_SOURCE == https* ]]; then
  # It's a URL, download the file
  curl -o $HOST_DUMP_FILE_NAME -L $DUMP_SOURCE
else
  HOST_DUMP_FILE_NAME="$DUMP_SOURCE"
fi

# Get the Docker container ID for the db service
CONTAINER_ID=$(docker-compose ps -q db)

# Copy the dump file to the container
docker cp $HOST_DUMP_FILE_NAME "${CONTAINER_ID}:${CONTAINER_DB_PATH}/$DUMP_FILE_NAME"

# Drop the existing database if it exists, then create it
docker-compose exec db psql -U postgres -c "DROP DATABASE IF EXISTS $DATABASE_NAME;"
docker-compose exec db psql -U postgres -c "CREATE DATABASE $DATABASE_NAME with encoding 'UTF8';"

# Restore the database
docker-compose exec db pg_restore --username postgres --no-owner --no-privileges --dbname $DATABASE_NAME $CONTAINER_DB_PATH/$DUMP_FILE_NAME

# Grant privileges
docker-compose exec db psql -U postgres -c "grant all privileges on database $DATABASE_NAME to hapi"
docker-compose exec db psql -U postgres $DATABASE_NAME -c "GRANT USAGE, CREATE ON SCHEMA public TO hapi"
docker-compose exec db psql -U postgres $DATABASE_NAME -c "GRANT ALL ON ALL TABLES IN SCHEMA public TO hapi"

# Delete the dump file from the container
docker-compose exec db rm "${CONTAINER_DB_PATH}/$DUMP_FILE_NAME"

# Return to the original directory
popd

echo "Database restoration and permissions setup complete. The file $HOST_DUMP_FILE_NAME has NOT been deleted from host."
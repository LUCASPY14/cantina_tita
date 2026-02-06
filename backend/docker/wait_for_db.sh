#!/bin/bash
# backend/docker/wait_for_db.sh

set -e

host="$1"
shift
cmd="$@"

until PGPASSWORD=$DB_PASSWORD psql -h "$host" -U "cantina_user" -d "cantina_tita" -c '\q'; do
  >&2 echo "PostgreSQL no está disponible - esperando..."
  sleep 1
done

>&2 echo "PostgreSQL está disponible - ejecutando comando"
exec $cmd
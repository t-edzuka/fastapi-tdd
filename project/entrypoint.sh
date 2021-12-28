#!/bin/sh
# This script is executed in fastapi app docker container
# to connect to PostgreSQL, port=54321
echo "Waiting for postgres..."

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL Started!!"

exec "$@"
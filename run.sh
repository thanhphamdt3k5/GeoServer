#!/usr/bin/with-contenv bashio

set -e

echo "=========================================="
echo " GeoServer v1.0.0"
echo "=========================================="

DB_HOST=$(bashio::config 'db_host')
DB_PORT=$(bashio::config 'db_port')
DB_USER=$(bashio::config 'db_user')
DB_PASSWORD=$(bashio::config 'db_password')
DB_NAME=$(bashio::config 'db_name')
LOG_LEVEL=$(bashio::config 'log_level')

export DB_HOST
export DB_PORT
export DB_USER
export DB_PASSWORD
export DB_NAME
export LOG_LEVEL

echo "Database"
echo "------------------------------------------"
echo "Host : ${DB_HOST}"
echo "Port : ${DB_PORT}"
echo "User : ${DB_USER}"
echo "Name : ${DB_NAME}"
echo "------------------------------------------"

cd /app

exec uvicorn \
    main:app \
    --host 0.0.0.0 \
    --port 8099 \
    --log-level ${LOG_LEVEL}
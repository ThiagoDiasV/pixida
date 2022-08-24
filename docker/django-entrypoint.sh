#!/bin/bash

set -e
set -u
set -o pipefail

DB_ready() {
python << END
import os
import sys
import psycopg2

try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=int(os.getenv('DB_PORT')),
    )
except psycopg2.OperationalError:
    sys.exit(-1)
else:
    conn.close()
    sys.exit(0)
END
}

until DB_ready; do
  >&2 echo 'Waiting for Postgres to become available...'
  sleep 1
done
>&2 echo 'Postgres is available'

exec python manage.py $@

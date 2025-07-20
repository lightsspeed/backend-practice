#!/bin/bash
set -e

# Function to wait for PostgreSQL
wait_for_postgres() {
    echo "Waiting for PostgreSQL..."
    
    while ! python -c "
import sys
import psycopg2
import os
from urllib.parse import urlparse

try:
    # Parse DATABASE_URL
    url = urlparse(os.getenv('DATABASE_URL'))
    conn = psycopg2.connect(
        host=url.hostname,
        port=url.port,
        user=url.username,
        password=url.password,
        database=url.path[1:]  # Remove leading '/'
    )
    conn.close()
    print('PostgreSQL is ready!')
    sys.exit(0)
except Exception as e:
    print(f'PostgreSQL is not ready: {e}')
    sys.exit(1)
    "; do
        sleep 2
    done
}

# Function to run database migrations
run_migrations() {
    echo "Running database migrations..."
    alembic upgrade head
    echo "Migrations completed."
}

# Main execution
main() {
    # Wait for PostgreSQL to be ready
    if [[ -n "${DATABASE_URL}" ]]; then
        wait_for_postgres
    fi
    
    # Run migrations if ENVIRONMENT is not test
    if [[ "${ENVIRONMENT}" != "test" ]]; then
        run_migrations
    fi
    
    # Execute the main command
    exec "$@"
}

# Run main function
main "$@"
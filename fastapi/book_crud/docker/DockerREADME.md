Development Environment
bash# Start development environment
docker-compose -f docker-compose.dev.yml up -d

# View logs

docker-compose -f docker-compose.dev.yml logs -f api

# Run migrations

docker-compose -f docker-compose.dev.yml exec api alembic upgrade head

# Access PostgreSQL

docker-compose -f docker-compose.dev.yml exec db psql -U bookuser -d bookdb

# Access PgAdmin (http://localhost:5050)

# Email: admin@example.com, Password: admin

# Stop development environment

docker-compose -f docker-compose.dev.yml down

Production Environment
bash# Build and start production environment
docker-compose up -d --build

# View logs

docker-compose logs -f

# Scale the API service

docker-compose up -d --scale api=3

# Stop production environment

docker-compose down

# Stop and remove volumes (WARNING: This deletes data)

docker-compose down -v

Useful Docker Commands
bash# Build specific service
docker-compose build api

# Run tests in container

docker-compose -f docker-compose.dev.yml exec api pytest

# Access API container shell

docker-compose -f docker-compose.dev.yml exec api bash

# View database data

docker-compose -f docker-compose.dev.yml exec db psql -U bookuser -d bookdb -c "SELECT \* FROM books;"

# Backup database

docker-compose exec db pg_dump -U bookuser bookdb > backup.sql

# Restore database

docker-compose exec -T db psql -U bookuser -d bookdb < backup.sql

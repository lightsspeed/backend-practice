-- Initialize database with any required setup
-- This file runs when the PostgreSQL container first starts

-- Create additional databases if needed
-- CREATE DATABASE bookdb_test;

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";

-- Create indexes for better search performance
-- (These will be created by Alembic migrations, but can be here as backup)

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE bookdb TO bookuser;
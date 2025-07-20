# Book CRUD API

A RESTful API for managing a collection of books built with FastAPI and PostgreSQL, containerized with Docker.

## Features

- ✅ **Create** - Add new books to the database
- ✅ **Read** - Retrieve all books or individual book details
- ✅ **Update** - Edit existing book information
- ✅ **Delete** - Remove books from the database
- 🔍 **Search & Filter** - Query books by various criteria
- 📚 **Pagination** - Handle large collections efficiently
- 🚀 **Fast Performance** - Built with FastAPI for high performance
- 📝 **Auto Documentation** - Interactive API docs with Swagger UI
- 🐳 **Containerized** - Easy deployment with Docker

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Migration**: Alembic
- **Validation**: Pydantic
- **Containerization**: Docker & Docker Compose
- **Python**: 3.11+

## Prerequisites

- Docker and Docker Compose installed
- Python 3.11+ (for local development)
- Git

## Quick Start

### Using Docker (Recommended)

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd book-crud-api
   ```

2. **Start the application**

   ```bash
   docker-compose up -d
   ```

3. **Access the API**
   - API Base URL: `http://localhost:8000`
   - Interactive Docs: `http://localhost:8000/docs`
   - ReDoc: `http://localhost:8000/redoc`

### Local Development Setup

1. **Create virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**

   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

4. **Run database migrations**

   ```bash
   alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Endpoints

### Books

| Method   | Endpoint        | Description                     |
| -------- | --------------- | ------------------------------- |
| `GET`    | `/books/`       | Get all books (with pagination) |
| `GET`    | `/books/{id}`   | Get book by ID                  |
| `POST`   | `/books/`       | Create a new book               |
| `PUT`    | `/books/{id}`   | Update book by ID               |
| `DELETE` | `/books/{id}`   | Delete book by ID               |
| `GET`    | `/books/search` | Search books by query           |

### Example Requests

#### Create a Book

```bash
curl -X POST "http://localhost:8000/books/" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "The Great Gatsby",
       "author": "F. Scott Fitzgerald",
       "genre": "Fiction",
       "year": 1925,
       "description": "A classic American novel"
     }'
```

#### Get All Books

```bash
curl "http://localhost:8000/books/?page=1&size=10"
```

#### Update a Book

```bash
curl -X PUT "http://localhost:8000/books/1" \
     -H "Content-Type: application/json" \
     -d '{
       "title": "The Great Gatsby - Updated",
       "author": "F. Scott Fitzgerald",
       "genre": "Classic Fiction",
       "year": 1925,
       "description": "A timeless American classic"
     }'
```

#### Delete a Book

```bash
curl -X DELETE "http://localhost:8000/books/1"
```

## Data Models

### Book Schema

```python
{
    "id": 1,
    "title": "string",
    "author": "string",
    "genre": "string",
    "year": 2023,
    "description": "string",
    "created_at": "2024-01-15T10:30:00",
    "updated_at": "2024-01-15T10:30:00"
}
```

### Request/Response Models

- **BookCreate**: Required fields for creating a book
- **BookUpdate**: Optional fields for updating a book
- **BookResponse**: Full book data returned by API
- **PaginatedResponse**: Paginated list of books

## Database Schema

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    year INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## Project Structure

```
book-crud-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application entry point
│   ├── database.py          # Database connection and session
│   ├── models/
│   │   ├── __init__.py
│   │   └── book.py          # SQLAlchemy models
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── book.py          # Pydantic schemas
│   ├── routers/
│   │   ├── __init__.py
│   │   └── books.py         # Book API routes
│   └── crud/
│       ├── __init__.py
│       └── book.py          # Database operations
├── alembic/                 # Database migrations
├── tests/                   # Test files
├── docker-compose.yml       # Docker services configuration
├── Dockerfile              # Docker image configuration
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## Environment Variables

Create a `.env` file with the following variables:

```env
# Database
DATABASE_URL=postgresql://username:password@localhost:5432/bookdb
POSTGRES_USER=bookuser
POSTGRES_PASSWORD=bookpass
POSTGRES_DB=bookdb

# API
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True

# Security (add for production)
SECRET_KEY=your-secret-key-here
```

## Docker Configuration

### docker-compose.yml services:

- **api**: FastAPI application
- **db**: PostgreSQL database
- **pgadmin** (optional): Database management interface

### Useful Docker Commands

```bash
# Build and start services
docker-compose up --build

# View logs
docker-compose logs api
docker-compose logs db

# Run migrations
docker-compose exec api alembic upgrade head

# Access database
docker-compose exec db psql -U bookuser -d bookdb

# Stop services
docker-compose down

# Remove volumes (caution: deletes data)
docker-compose down -v
```

## Testing

### Run Tests

```bash
# With pytest
pytest

# With coverage
pytest --cov=app tests/

# In Docker
docker-compose exec api pytest
```

### Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Test configuration
├── test_books.py        # Book API tests
└── test_database.py     # Database tests
```

## API Documentation

Once the server is running, visit:

- **Swagger UI**: `http://localhost:8000/docs` - Interactive API documentation
- **ReDoc**: `http://localhost:8000/redoc` - Alternative documentation format

## Performance Features

- **Async/Await**: Non-blocking database operations
- **Connection Pooling**: Efficient database connections
- **Pagination**: Handles large datasets efficiently
- **Query Optimization**: Indexed database fields
- **Response Models**: Structured JSON responses

## Production Deployment

### Environment Setup

```bash
# Set production environment variables
export DEBUG=False
export DATABASE_URL=postgresql://user:pass@prod-db:5432/bookdb
```

### Security Considerations

- Use environment variables for sensitive data
- Enable HTTPS in production
- Set up proper CORS policies
- Implement rate limiting
- Use strong database passwords
- Regular security updates

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run tests and ensure they pass
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues and questions:

- Create an issue in the GitHub repository
- Check the API documentation at `/docs`
- Review the logs with `docker-compose logs api`

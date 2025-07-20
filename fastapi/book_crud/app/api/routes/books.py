from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from app.crud.book import book_crud
from app.api.deps import get_database
from app.utils.exceptions import BookNotFoundError, BookAlreadyExistsError

router = APIRouter()

@router.post("/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
async def create_book(
    book: BookCreate,
    db: Session = Depends(get_database)
):
    """Create a new book"""
    try:
        return book_crud.create_book(db=db, book=book)
    except (BookAlreadyExistsError, Exception) as e:
        raise e

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: int,
    db: Session = Depends(get_database)
):
    """Get a specific book by ID"""
    try:
        return book_crud.get_book(db=db, book_id=book_id)
    except (BookNotFoundError, Exception) as e:
        raise e

@router.get("/", response_model=List[BookResponse])
async def get_books(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of records to return"),
    search: Optional[str] = Query(None, description="Search in title, author, or ISBN"),
    db: Session = Depends(get_database)
):
    """Get all books with pagination and search"""
    try:
        books = book_crud.get_books(db=db, skip=skip, limit=limit, search=search)
        return books
    except Exception as e:
        raise e

@router.put("/{book_id}", response_model=BookResponse)
async def update_book(
    book_id: int,
    book_update: BookUpdate,
    db: Session = Depends(get_database)
):
    """Update a specific book"""
    try:
        return book_crud.update_book(db=db, book_id=book_id, book_update=book_update)
    except (BookNotFoundError, Exception) as e:
        raise e

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(
    book_id: int,
    db: Session = Depends(get_database)
):
    """Delete a specific book"""
    try:
        book_crud.delete_book(db=db, book_id=book_id)
        return {"message": "Book deleted successfully"}
    except (BookNotFoundError, Exception) as e:
        raise e

@router.get("/stats/count")
async def get_books_count(
    search: Optional[str] = Query(None, description="Search in title, author, or ISBN"),
    db: Session = Depends(get_database)
):
    """Get total count of books"""
    try:
        count = book_crud.get_books_count(db=db, search=search)
        return {"count": count}
    except Exception as e:
        raise e
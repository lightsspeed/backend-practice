from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate
from app.utils.exceptions import BookNotFoundError, BookAlreadyExistsError, DatabaseError

class BookCRUD:
    
    @staticmethod
    def create_book(db: Session, book: BookCreate) -> Book:
        """Create a new book"""
        try:
            # Check if book with same ISBN already exists
            existing_book = db.query(Book).filter(Book.isbn == book.isbn).first()
            if existing_book:
                raise BookAlreadyExistsError(book.isbn)
            
            db_book = Book(**book.model_dump())
            db.add(db_book)
            db.commit()
            db.refresh(db_book)
            return db_book
        except BookAlreadyExistsError:
            raise
        except Exception as e:
            db.rollback()
            raise DatabaseError(f"Failed to create book: {str(e)}")
    
    @staticmethod
    def get_book(db: Session, book_id: int) -> Book:
        """Get a book by ID"""
        try:
            book = db.query(Book).filter(Book.id == book_id).first()
            if not book:
                raise BookNotFoundError(book_id)
            return book
        except BookNotFoundError:
            raise
        except Exception as e:
            raise DatabaseError(f"Failed to retrieve book: {str(e)}")
    
    @staticmethod
    def get_books(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        search: Optional[str] = None
    ) -> List[Book]:
        """Get all books with optional search"""
        try:
            query = db.query(Book)
            
            if search:
                search_filter = or_(
                    Book.title.ilike(f"%{search}%"),
                    Book.author.ilike(f"%{search}%"),
                    Book.isbn.ilike(f"%{search}%")
                )
                query = query.filter(search_filter)
            
            books = query.offset(skip).limit(limit).all()
            return books
        except Exception as e:
            raise DatabaseError(f"Failed to retrieve books: {str(e)}")
    
    @staticmethod
    def update_book(db: Session, book_id: int, book_update: BookUpdate) -> Book:
        """Update a book"""
        try:
            db_book = db.query(Book).filter(Book.id == book_id).first()
            if not db_book:
                raise BookNotFoundError(book_id)
            
            update_data = book_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_book, field, value)
            
            db.commit()
            db.refresh(db_book)
            return db_book
        except BookNotFoundError:
            raise
        except Exception as e:
            db.rollback()
            raise DatabaseError(f"Failed to update book: {str(e)}")
    
    @staticmethod
    def delete_book(db: Session, book_id: int) -> bool:
        """Delete a book"""
        try:
            db_book = db.query(Book).filter(Book.id == book_id).first()
            if not db_book:
                raise BookNotFoundError(book_id)
            
            db.delete(db_book)
            db.commit()
            return True
        except BookNotFoundError:
            raise
        except Exception as e:
            db.rollback()
            raise DatabaseError(f"Failed to delete book: {str(e)}")
    
    @staticmethod
    def get_books_count(db: Session, search: Optional[str] = None) -> int:
        """Get total count of books"""
        try:
            query = db.query(Book)
            
            if search:
                search_filter = or_(
                    Book.title.ilike(f"%{search}%"),
                    Book.author.ilike(f"%{search}%"),
                    Book.isbn.ilike(f"%{search}%")
                )
                query = query.filter(search_filter)
            
            return query.count()
        except Exception as e:
            raise DatabaseError(f"Failed to count books: {str(e)}")

# Create instance
book_crud = BookCRUD()
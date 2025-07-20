from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float
    isbn: str
    publication_year: Optional[int] = None
    
    @validator('price')
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Price must be greater than 0')
        return round(v, 2)
    
    @validator('isbn')
    def validate_isbn(cls, v):
        # Remove any hyphens or spaces
        isbn = v.replace('-', '').replace(' ', '')
        if len(isbn) not in [10, 13]:
            raise ValueError('ISBN must be 10 or 13 digits')
        if not isbn.isdigit():
            raise ValueError('ISBN must contain only digits')
        return isbn

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    publication_year: Optional[int] = None
    
    @validator('price')
    def validate_price(cls, v):
        if v is not None and v <= 0:
            raise ValueError('Price must be greater than 0')
        return round(v, 2) if v is not None else v

class BookResponse(BookBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
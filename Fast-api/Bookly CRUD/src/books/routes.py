from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi import APIRouter
from src.books.book_data import books
from src.books.schemas import BookCreateModel, BookUpdateModel


book_router = APIRouter()


# @book_router.get('/')

# async def read_root():
#     return {"message" : "Hello World!!"}

# @book_router.get('/greet/{name}')

# async def greet(name: str) -> dict:
#     return {"message" : f"Hello {name}!!"}


# #Query Params@book_router.get('/query') #not mentioned in path

# async def query(name: str, age: int) -> dict:
#     return {"message" : f"Hello {name}", "age": age}


#this is how to test query param
#localhost:8000/query?name=akhi 
#localhost:8000/query?name=akhi&age=30 


#@book_router.get("/profile")
# async def get_profile(name: str, age: int, city: str):
#     return {
#         "name": name,
#         "age": age,
#         "city": city
#     }






@book_router.get('/')
async def get_all_books():
    return books


@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book_data:BookCreateModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@book_router.get('/{book_id}')
async def get_book(book_id:int):
    
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not Found!')



@book_router.patch('/{book_id}')
async def update_book(book_id:int, book_update_data:BookUpdateModel):
    for book in books:
        if book['id'] == book_id:
            book['pages'] = book_update_data.pages
            book['language'] = book_update_data.language

            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'Book not Found!')
@book_router.delete('/{book_id}')
async def delete_book(book_id:int):
    for i, book in enumerate(books):
        if book['id'] == book_id:
             books.pop(i)

             return {"message": f"Book with ID {book_id} deleted successfully"}
        
        raise HTTPException(status_code=404, detail="Book not found")
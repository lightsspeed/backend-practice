from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel


app = FastAPI()

@app.get('/')

async def read_root():
    return {"message" : "Hello World!!"}


@app.get('/greet/{name}')

async def greet(name: str) -> dict:
    return {"message" : f"Hello {name}!!"}


#Query Params
@app.get('/query') #not mentioned in path

async def query(name: str, age: int) -> dict:
    return {"message" : f"Hello {name}", "age": age}


#this is how to test query param
#localhost:8000/query?name=akhi 
#localhost:8000/query?name=akhi&age=30 


# @app.get("/profile")
# async def get_profile(name: str, age: int, city: str):
#     return {
#         "name": name,
#         "age": age,
#         "city": city
#     }


class BookCreateModel(BaseModel):

    id: int
    title: str
    author: str
    genre: str
    pages: int
    language: str

class BookUpdateModel(BaseModel):

    pages: int
    language: str




books = [
{"id": 1, "title": "Chupke Safar", "author": "Priya Sharma", "genre": "Katha", "language": "Hindi", "pages": 234},
{"id": 2, "title": "Rahasya Van", "author": "Arjun Patel", "genre": "Kaalpnik", "language": "Hindi", "pages": 412},
{"id": 3, "title": "Chhupa Tara", "author": "Ananya Gupta", "genre": "Vigyan Katha", "language": "Hindi", "pages": 189},
{"id": 4, "title": "Swarnim Marg", "author": "Vikram Singh", "genre": "Saahasik", "language": "Hindi", "pages": 356},
{"id": 5, "title": "Andhera Nadi", "author": "Neha Verma", "genre": "Rahasya", "language": "Hindi", "pages": 278},
{"id": 6, "title": "Ujjwal Yatra", "author": "Rahul Kumar", "genre": "Thriller", "language": "Hindi", "pages": 521},
{"id": 7, "title": "Khoya Rajya", "author": "Sneha Reddy", "genre": "Prem Kahani", "language": "Hindi", "pages": 145},
{"id": 8, "title": "Pracheen Prakash", "author": "Amit Joshi", "genre": "Gair-Katha", "language": "Hindi", "pages": 399},
{"id": 9, "title": "Gupt Sapna", "author": "Pooja Desai", "genre": "Katha", "language": "Hindi", "pages": 267},
{"id": 10, "title": "Anant Chhaya", "author": "Rohan Malhotra", "genre": "Kaalpnik", "language": "Hindi", "pages": 483}
]


@app.get('/books')
async def get_all_books():
    return books

@app.post('/create_books', status_code=status.HTTP_201_CREATED)
async def create_book(book_data:BookCreateModel) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/books/{book_id}')
async def get_book(book_id:int):
    
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not Found!')




@app.patch('/books/{book_id}')
async def update_book(book_id:int, book_update_data:BookUpdateModel):
    for book in books:
        if book['id'] == book_id:
            book['pages'] = book_update_data.pages
            book['language'] = book_update_data.language

            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= 'Book not Found!')

@app.get('/books/{book_id}')
async def delete_book(book_id:int):
    pass
from fastapi import FastAPI
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

    title: str
    author: str
    genre: str
    pages: int

@app.post('/createbook')

async def create_book(book_data:BookCreateModel):
    return {
        "title" : book_data.title,
        "author" : book_data.author,
        "genre" : book_data.genre,
        "pages" : book_data.pages
    }

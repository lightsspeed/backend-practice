from pydantic import BaseModel







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
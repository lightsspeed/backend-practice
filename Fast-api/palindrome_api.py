from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Palindrome(BaseModel):
    word: str
    cleaned_word: str
    is_palindrome: bool
    

@app.get("/is_palindrome/{word}",response_model=Palindrome)

async def is_palindrome(word: str):

    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())

    is_pal = cleaned_word == cleaned_word[::-1]

    return {
        "word": word,
        "cleaned_word": cleaned_word,
        "is_palindrome": is_pal
        
        
    }

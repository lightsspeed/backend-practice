from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class AddNum(BaseModel):

    num1: int
    num2: int
    

@app.get("/add", response_model=AddNum)

async def adding(num1: int , num2: int):
    
    add_num = num1 + num2

    return {
        "num1": num1,
        "num2": num2,
        "add_num": add_num
    }

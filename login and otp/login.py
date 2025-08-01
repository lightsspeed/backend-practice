from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from uuid import uuid4
import random

app = FastAPI()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

#In memory storage
users_db = {}
used_otp = set()

class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    user_id: str
    username: str
    otp: int

def generate_unique_otp():
    while True:
        otp = random.randint(10000, 99999)
        if otp not in used_otp:
            used_otp.add(otp)
            return otp

@app.post("/register", response_model=UserResponse)
def register_user(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username Already Exists.")
    
    hashed_password = pwd_context.hash(user.password)
    user_id = str(uuid4())
    otp = generate_unique_otp()

    users_db[user.username] = {
        "user_id": user_id,
        "hashed_password": hashed_password,
        "otp": otp,
    }

    return {
        "user_id": user_id,
        "username": user.username,
        "otp": otp,
    }

@app.get("/getdata")
def getdata():
    return users_db, used_otp
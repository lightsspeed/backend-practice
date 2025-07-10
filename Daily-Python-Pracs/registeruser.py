from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):

    username: str
    email: str


@app.post("/register")

def register_user(user: User):

    return {
        "message" : f"user {user.username} registered successfully with email {user.email}"
    }



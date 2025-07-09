from fastapi import FastAPI

app = FastAPI()

@app.get("/Hello")

def say_hello():
    return {"message": "hello, backend "}
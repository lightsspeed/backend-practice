from pydantic_settings import BaseSettings # type: ignore
from typing import Optional
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

class Settings(BaseSettings):
    APP_NAME: str = "Book CRUD API"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() # type: ignore
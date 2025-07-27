from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL = str,
    DEBUG = bool

    class Config: 
        env_file = ".env"

settings = Settings()

from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://user:password@host:port/dbname"

    class Config:
        env_file = ".env"

settings = Settings()

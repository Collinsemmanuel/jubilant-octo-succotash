from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    PROJECT_NAME: str = "FASTAPI CRUD template"

    class config:
        env_file = ".env"

settings = Settings()
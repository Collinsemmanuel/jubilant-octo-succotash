from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./test.db"
    PROJECT_NAME: str = "TODO List API"

    model_config = {"env_file": ".env"}

settings = Settings()
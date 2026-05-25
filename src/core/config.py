from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    TEMPORAL_SERVER: str

    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()
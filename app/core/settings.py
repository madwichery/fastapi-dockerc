from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "FastAPI"
    DOCS_URL: str | None = None
    REDOC_URL: str | None = None
    OPENAPI_URL: str = "/openapi.json"
    SCALAR_URL: str = "/scalar"

    DB_NAME: str = "postgres"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_HOST: str = "db"
    DB_PORT: int = "5432"

    DB_CONNECTION_STRING: str = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    class Config:
        env_file = ".env"
        extra = "ignore" # fungsi sentralisasi konfigurasi

settings = Settings()

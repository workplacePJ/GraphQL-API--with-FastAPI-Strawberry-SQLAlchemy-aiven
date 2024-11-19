from pydantic_settings import BaseSettings
from functools import lru_cache
from typing import Optional

class Settings(BaseSettings):
    # アプリケーション設定
    APP_NAME: str = "Invoice API"
    DEBUG: bool = False
    API_V1_STR: str = "/api/v1"
    
    # データベース設定
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    
    # JWT設定
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 120  # 2時間
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 1週間
    
    # Google Drive設定
    GOOGLE_DRIVE_CREDENTIALS: Optional[dict] = None
    GOOGLE_DRIVE_FOLDER_ID: Optional[str] = None
    
    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()

settings = get_settings()

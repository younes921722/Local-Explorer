from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    openweather_api_key: str
    gemini_api_key: str
    google_maps_api_key: str

    class Config:
        env_file = ".env"

settings = Settings()

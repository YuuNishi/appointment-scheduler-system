from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    token_secret: str = 'FATECTQ_LABES'

settings = Settings()
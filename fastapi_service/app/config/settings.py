from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ELASTIC_HOST: str = "http://elasticsearch:9200"
    TEXTS_INDEX: str = "texts_index"

settings = Settings()

"""
DB configuration module
This script handles loading of .env variables
using Pydantic Settings
"""
import os
from pathlib import Path

from icecream import ic
from pydantic_settings import BaseSettings, SettingsConfigDict


__BASE_PATH__ = Path(os.path.curdir).resolve().parent.parent.parent
__ENV_PATH__ = __BASE_PATH__/ "src"/ "app"/ "db"/ ".env"



#stores data connection
class Settings(BaseSettings):
    #implicit type
    DB_USER: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_PASSWORD: str

    #@property is a method but called like a field
    @property
    def database_url(self):
        #dialect+driver://user:pass@host:port/dbname
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}?charset=utf8mb4"
    #with pydantic (analogy for dotenv) load connection configuration
    model_config = SettingsConfigDict(env_file=__ENV_PATH__)

settings = Settings()

if __name__ == '__main__':
    ic(settings)
    ic(settings.database_url)


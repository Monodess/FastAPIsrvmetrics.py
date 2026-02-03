from pydantic_settings import BaseSettings, SettingsConfigDict

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
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
print (settings)
print (settings.database_url)
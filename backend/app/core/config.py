from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config=SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
    POSTGRES_SERVER:str
    POSTGRES_PORT:int = 5432
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_DB:str

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URL(self) -> PostgresDsn:
        return PostgresDsn.build(scheme="postgresql+psycopg2",host=self.POSTGRES_SERVER,username=self.POSTGRES_USER,password=self.POSTGRES_PASSWORD,port=self.POSTGRES_PORT,path=self.POSTGRES_DB)

    ABC_KEY:str
    SECRET_KEY:str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
setting = Settings()
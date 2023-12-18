from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", case_sensitive=False)

    db_login: str
    db_password: str
    db_port: int
    db_host: str
    db_name: str
    db_echo: bool = True

    @property
    def db_url(self) -> str:
        return f"postgresql://{self.db_login}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings

from typing import Iterator
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from core import config


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_engine(
            url=url,
            echo=echo,
        )
        self.session_factory = sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )

    def session_dependency(self) -> Iterator[Session]:
        session = self.session_factory()
        try:
            yield session
        finally:
            session.close()


@lru_cache
def get_database() -> DatabaseHelper:
    db_helper = DatabaseHelper(
        config.get_settings().db_url, config.get_settings().db_echo
    )
    return db_helper

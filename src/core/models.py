from typing import Annotated

from inflection import underscore
from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column


pk_int = Annotated[int, mapped_column(primary_key=True)]
pk_bitint = Annotated[int, mapped_column(BigInteger, primary_key=True)]


class Base(DeclarativeBase):
    __abstract__ = True

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return underscore(cls.__name__)

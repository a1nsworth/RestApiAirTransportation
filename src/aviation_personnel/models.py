import enum
from typing import List

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import Enum

from core.models import Base, pk_int


class RoleOccupied(enum.Enum):
    PILOT = "PILOT"
    STEWARD = "STEWARD"
    FLIGHT_ENGINEER = "FLIGHT_ENGINEER"


class AviationPersonnel(Base):
    id: Mapped[pk_int]
    first_name: Mapped[str]
    second_name: Mapped[str]
    role: Mapped[List[RoleOccupied] | None] = mapped_column(
        ARRAY(Enum(RoleOccupied)), default=None
    )

from typing import Annotated

from .models import RoleOccupied
from pydantic import BaseModel, ConfigDict


class AviationPersonnelBase(BaseModel):
    first_name: str
    second_name: str
    role: list[RoleOccupied] | None = None


class AviationPersonnelDb(AviationPersonnelBase):
    model_config = ConfigDict(from_attributes=True)


class AviationPersonnelCreate(AviationPersonnelBase):
    pass


class AviationPersonnelUpdate(AviationPersonnelBase):
    pass


class AviationPersonnelUpdatePartial(AviationPersonnelBase):
    first_name: str | None = None
    second_name: str | None = None

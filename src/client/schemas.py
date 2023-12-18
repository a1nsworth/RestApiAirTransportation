from datetime import date
from pydantic import BaseModel, ConfigDict, EmailStr


class ClientOrderBase(BaseModel):
    departure_date: date
    arrival_date: date
    departure_city: str
    arrival_city: str


class ClientOrderUpdatePartial(BaseModel):
    departure_date: date | None = None
    arrival_date: date | None = None
    departure_city: str | None = None
    arrival_city: str | None = None


class ClientOrderDb(ClientOrderBase):
    model_config = ConfigDict(from_attributes=True)


class ClientBase(BaseModel):
    name: str
    number_phone: str
    email: EmailStr | None = None
    telegram_id: str | None = None
    description: str | None = None
    order: ClientOrderBase


class ClientDb(ClientBase):
    model_config = ConfigDict(from_attributes=True)


class ClientCreate(ClientBase):
    pass


class ClientUpdate(ClientBase):
    name: str | None = None
    number_phone: str | None = None
    order: ClientOrderUpdatePartial | None = None


class ClientPartialUpdate(ClientBase):
    pass

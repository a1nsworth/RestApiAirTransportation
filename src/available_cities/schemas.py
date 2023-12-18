from pydantic import BaseModel, ConfigDict


class AvailableCityBase(BaseModel):
    name: str


class AvailableCityDb(AvailableCityBase):
    model_config = ConfigDict(from_attributes=True)


class AvailableCityCreate(AvailableCityBase):
    pass


class AvailableCityUpdate(AvailableCityBase):
    pass


class AvailableCityUpdatePartial(AvailableCityBase):
    pass

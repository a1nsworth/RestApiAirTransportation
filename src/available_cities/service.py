from sqlalchemy.orm import Session
from sqlalchemy import select, Result
from . import models
from . import schemas


def get_cities(session: Session) -> list[models.AvailableCities]:
    stmt = select(models.AvailableCities)
    result: Result = session.execute(stmt)
    available_cities: list[models.AvailableCities] = list(result.scalars().all())
    return available_cities


def retrieve_city(session: Session, city_name: str) -> models.AvailableCities:
    return session.get(models.AvailableCities, city_name)


def create_cities(
    session: Session, cities_create: list[schemas.AvailableCityCreate]
) -> list[models.AvailableCities]:
    cities = [
        models.AvailableCities(**city_create.model_dump())
        for city_create in cities_create
    ]
    session.add_all(cities)
    session.commit()
    return cities


def create_city(
    session: Session, city_create: schemas.AvailableCityCreate
) -> models.AvailableCities:
    city = models.AvailableCities(**city_create.model_dump())
    session.add(city)
    session.commit()
    return city


def update_city(
    session: Session,
    available_city_db: models.AvailableCities,
    available_city_update: schemas.AvailableCityUpdate,
) -> models.AvailableCities:
    for key, value in available_city_update.model_dump().items():
        setattr(available_city_db, key, value)
    session.commit()
    return available_city_db


def delete_city(session: Session, available_city_db: models.AvailableCities) -> None:
    session.delete(available_city_db)
    session.commit()

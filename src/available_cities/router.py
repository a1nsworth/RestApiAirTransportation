from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from core.database import get_database
from . import dependencies
from . import schemas
from . import service

available_cities_router = APIRouter(
    prefix="/available_cities", tags=["Available Cities"]
)


@available_cities_router.get("/", response_model=list[schemas.AvailableCityDb])
def get_available_cities(session: Session = Depends(get_database().session_dependency)):
    return service.get_cities(session)


@available_cities_router.get("/{city_name}/", response_model=schemas.AvailableCityDb)
def retrieve_available_city(city=Depends(dependencies.retrieve_city)):
    return city


@available_cities_router.post(
    "/list/",
    response_model=list[schemas.AvailableCityDb],
    status_code=status.HTTP_201_CREATED,
)
def create_cities(
    cities_create: list[schemas.AvailableCityCreate],
    session: Session = Depends(get_database().session_dependency),
):
    return service.create_cities(session, cities_create)


@available_cities_router.post(
    "/", response_model=schemas.AvailableCityDb, status_code=status.HTTP_201_CREATED
)
def create_city(
    city_create: schemas.AvailableCityCreate,
    session: Session = Depends(get_database().session_dependency),
):
    return service.create_city(session, city_create)


@available_cities_router.delete("/{city_name}/")
def delete_city(
    city_db=Depends(dependencies.retrieve_city),
    session: Session = Depends(get_database().session_dependency),
):
    service.delete_city(session, city_db)

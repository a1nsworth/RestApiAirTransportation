from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core.database import get_database
from . import dependencies
from . import schemas
from . import service

client_router = APIRouter(prefix="/client", tags=["Client"])


@client_router.get("/", response_model=list[schemas.ClientDb])
def get_clients(session: Session = Depends(get_database().session_dependency)):
    return service.get_clients(session)


@client_router.get("/{client_id}/", response_model=schemas.ClientDb)
def retrieve_client(client=Depends(dependencies.retrieve_client)):
    return client


@client_router.post(
    "/", response_model=schemas.ClientDb, status_code=status.HTTP_201_CREATED
)
def create_client(
    client_create: schemas.ClientCreate,
    session: Session = Depends(get_database().session_dependency),
):
    return service.create_client(session, client_create)


@client_router.post(
    "/list/", response_model=list[schemas.ClientDb], status_code=status.HTTP_201_CREATED
)
def create_clients(
    clients_create: list[schemas.ClientCreate],
    session: Session = Depends(get_database().session_dependency),
):
    return service.create_clients(session, clients_create)


@client_router.put("/{client_id}/", response_model=schemas.ClientDb)
def update_client(
    client_update: schemas.ClientUpdate,
    client_db=Depends(dependencies.retrieve_client),
    session: Session = Depends(get_database().session_dependency),
):
    return service.create_clients(session, client_db, client_update)


@client_router.patch("/{client_id}/", response_model=schemas.ClientDb)
def partial_update_client(
    client_partial_update: schemas.ClientPartialUpdate,
    client_db=Depends(dependencies.retrieve_client),
    session: Session = Depends(get_database().session_dependency),
):
    return service.partial_update_client(session, client_db, client_partial_update)


@client_router.delete("/{client_id}/")
def delete_client(
    client_db=Depends(dependencies.retrieve_client),
    session: Session = Depends(get_database().session_dependency),
):
    service.delete_client(session, client_db)

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select, Result

from . import models
from . import schemas


def get_clients(session: Session) -> list[models.Client]:
    stmt = select(models.Client).options(joinedload(models.Client.order))
    result: Result = session.execute(stmt)
    clients: list[models.Client] = list(result.scalars().all())
    return clients


def retrieve_client(
    session: Session,
    client_id: int,
) -> models.Client | None:
    return session.get(models.Client, client_id)


def create_clients(
    session: Session,
    clients_create: list[schemas.ClientCreate],
) -> list[models.Client]:
    clients = [models.Client(**client.model_dump()) for client in clients_create]
    session.add_all(clients)
    session.commit()
    return clients


def create_client(
    session: Session,
    client_create: schemas.ClientCreate,
) -> models.Client:
    client = models.Client(**client_create.model_dump())
    session.add(client)
    session.commit()
    return client


def update_client(
    session: Session, client_db: models.Client, client_update: schemas.ClientUpdate
) -> models.Client:
    for key, value in client_update.model_dump().items():
        setattr(client_db, key, value)
    session.commit()
    return client_db


def partial_update_client(
    session: Session,
    client_db: models.Client,
    client_update: schemas.ClientPartialUpdate,
) -> models.Client:
    for key, value in client_update.model_dump(exclude_unset=True).items():
        setattr(client_db, key, value)
    session.commit()
    return client_db


def delete_client(session: Session, client_db: models.Client) -> None:
    session.delete(client_db)
    session.commit()

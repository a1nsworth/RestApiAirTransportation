from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from core import database
from . import dependencies
from . import service
from . import models
from . import schemas

aviation_personnel_router = APIRouter(
    prefix="/aviation_personnel", tags=["Aviation Personnel"]
)


@aviation_personnel_router.get("/", response_model=list[schemas.AviationPersonnelDb])
def get_all_aviation_personnel(
    session: Session = Depends(database.get_database().session_dependency),
):
    return service.get_aviation_personnel_list(session)


@aviation_personnel_router.get(
    "/{aviation_personnel_id}/", response_model=schemas.AviationPersonnelDb
)
def retrieve_aviation_personnel(
    aviation_personnel=Depends(dependencies.retrieve_aviation_personnel),
):
    return aviation_personnel


@aviation_personnel_router.post(
    "/", response_model=schemas.AviationPersonnelDb, status_code=status.HTTP_201_CREATED
)
def create_aviation_personnel(
    aviation_personnel: schemas.AviationPersonnelCreate,
    session: Session = Depends(database.get_database().session_dependency),
):
    return service.create_aviation_personnel(
        session=session, aviation_personnel_create=aviation_personnel
    )


@aviation_personnel_router.post(
    "/list/",
    response_model=list[schemas.AviationPersonnelDb],
    status_code=status.HTTP_201_CREATED,
)
def create_list_aviation_personnel(
    list_aviation_personnel: list[schemas.AviationPersonnelCreate],
    session: Session = Depends(database.get_database().session_dependency),
):
    return service.create_list_aviation_personnel(session, list_aviation_personnel)


@aviation_personnel_router.put(
    "/{aviation_personnel_id}/", response_model=schemas.AviationPersonnelDb
)
def update_aviation_personnel(
    aviation_personnel_update: schemas.AviationPersonnelUpdate,
    aviation_personnel_db: models.AviationPersonnel = Depends(
        dependencies.retrieve_aviation_personnel
    ),
    session: Session = Depends(database.get_database().session_dependency),
):
    return service.update_aviation_personnel(
        session, aviation_personnel_db, aviation_personnel_update, partial=False
    )


@aviation_personnel_router.patch(
    "/{aviation_personnel_id}/", response_model=schemas.AviationPersonnelDb
)
def partial_update_aviation_personnel(
    aviation_personnel_update: schemas.AviationPersonnelUpdatePartial,
    aviation_personnel_db: models.AviationPersonnel = Depends(
        dependencies.retrieve_aviation_personnel
    ),
    session: Session = Depends(database.get_database().session_dependency),
):
    return service.update_aviation_personnel(
        session, aviation_personnel_db, aviation_personnel_update, partial=True
    )


@aviation_personnel_router.delete("/{aviation_personnel_id}/")
def delete_aviation_personnel(
    aviation_personnel_db: models.AviationPersonnel = Depends(
        dependencies.retrieve_aviation_personnel
    ),
    session: Session = Depends(database.get_database().session_dependency),
):
    service.delete_aviation_personnel(session, aviation_personnel_db)

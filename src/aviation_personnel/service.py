from sqlalchemy import select, Result
from sqlalchemy.orm import Session

from .models import AviationPersonnel
from .schemas import (
    AviationPersonnelCreate,
    AviationPersonnelUpdate,
    AviationPersonnelUpdatePartial,
)


def get_aviation_personnel_list(session: Session) -> list[AviationPersonnel]:
    stmt = select(AviationPersonnel)
    result: Result = session.execute(stmt)
    aviation_personnel = result.scalars().all()
    return list(aviation_personnel)


def retrieve_aviation_personnel(
    session: Session, aviation_personnel_id: int
) -> AviationPersonnel | None:
    return session.get(AviationPersonnel, aviation_personnel_id)


def create_aviation_personnel(
    session: Session, aviation_personnel_create: AviationPersonnelCreate
) -> AviationPersonnel:
    aviation_personnel = AviationPersonnel(**aviation_personnel_create.model_dump())
    session.add(aviation_personnel)
    session.commit()
    return aviation_personnel


def create_list_aviation_personnel(
    session: Session, aviation_personnel_create: list[AviationPersonnelCreate]
) -> list[AviationPersonnel]:
    list_aviation_personnel = [
        AviationPersonnel(**personnel.model_dump())
        for personnel in aviation_personnel_create
    ]

    session.add_all(list_aviation_personnel)
    session.commit()
    return list_aviation_personnel


def update_aviation_personnel(
    session: Session,
    aviation_personnel_db: AviationPersonnel,
    aviation_personnel_update: AviationPersonnelUpdate | AviationPersonnelUpdatePartial,
    *,
    partial: bool,
) -> AviationPersonnel | None:
    for key, value in aviation_personnel_update.model_dump(
        exclude_none=partial
    ).items():
        setattr(aviation_personnel_db, key, value)
    session.commit()
    return aviation_personnel_db


def delete_aviation_personnel(
    session: Session,
    aviation_personnel_db: AviationPersonnel,
) -> None:
    session.delete(aviation_personnel_db)
    session.commit()

from typing import Annotated
from fastapi import Depends, status, HTTPException, Path
from sqlalchemy.orm import Session

from core.database import get_database
from . import service
from . import models


def retrieve_aviation_personnel(
    aviation_personnel_id: Annotated[int, Path],
    session: Session = Depends(get_database().session_dependency),
) -> models.AviationPersonnel:
    aviation_personnel: models.AviationPersonnel = service.retrieve_aviation_personnel(
        session, aviation_personnel_id
    )
    if aviation_personnel is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aviation Personnel with id = {aviation_personnel_id} not found",
        )

    return aviation_personnel

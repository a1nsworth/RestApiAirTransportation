from fastapi import HTTPException, status, Path, Depends
from core.database import get_database
from sqlalchemy.orm import Session

from typing import Annotated
from . import models
from . import service


def retrieve_city(
    city_name: Annotated[str, Path],
    session: Session = Depends(get_database().session_dependency),
) -> models.AvailableCities:
    city = service.retrieve_city(session, city_name)
    if city is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"City with name = {city_name} not found",
        )

    return city

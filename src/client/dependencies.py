from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.orm import Session

from core.database import get_database
from . import models
from . import service


def retrieve_client(
    client_id: Annotated[int, Path],
    session: Session = Depends(get_database().session_dependency),
) -> models.Client:
    client = service.retrieve_client(session, client_id)
    if client is None:
        raise HTTPException(
            detail=f"Client with id = {client_id} not found",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return client

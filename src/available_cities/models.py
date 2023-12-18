from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class AvailableCities(Base):
    name: Mapped[str] = mapped_column(primary_key=True)

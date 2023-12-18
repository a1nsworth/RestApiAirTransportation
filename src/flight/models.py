from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class AvailableCities(Base):
    __tablename__ = "available_cities"

    name: Mapped[str] = mapped_column(primary_key=True)

from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base


class Plane(Base):
    id: Mapped[int] = mapped_column(primary_key=True)

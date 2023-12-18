import datetime

from sqlalchemy import ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base, pk_int, pk_bitint


class Client(Base):
    id: Mapped[pk_bitint]
    name: Mapped[str]
    number_phone: Mapped[str]
    email: Mapped[str | None] = None
    telegram_id: Mapped[str | None] = None
    description: Mapped[str | None] = None

    order: Mapped["ClientOrder"] = relationship(back_populates="client", uselist=False)


class ClientOrder(Base):
    id: Mapped[pk_int]
    departure_date: Mapped[datetime.date]
    arrival_date: Mapped[datetime.date]
    departure_city: Mapped[str]
    arrival_city: Mapped[str]

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), unique=True)
    client: Mapped["Client"] = relationship(
        back_populates="order", uselist=False
    )

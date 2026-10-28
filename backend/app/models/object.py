# -*- coding: utf-8 -*-
"""objects — узлы учёта, принадлежат одной компании (ТЗ п.10–11)."""
from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Object(Base):
    __tablename__ = "objects"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("scada.companies.id"), nullable=False, index=True)
    external_id: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)  # {object_id} в MQTT-топике
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str | None] = mapped_column(String(512))
    # TODO: геолокация, тип узла, произвольные атрибуты (JSONB)

    devices: Mapped[list["Device"]] = relationship(back_populates="obj")  # noqa: F821

# -*- coding: utf-8 -*-
"""devices — приборы и датчики, привязаны к одному объекту (ТЗ п.10–11).

Тип устройства, модель и схема данных задаются конфигурацией device_type
(ТЗ п.7: добавление нового оборудования не меняет логику приёма).
"""
from datetime import datetime

from sqlalchemy import BigInteger, Boolean, DateTime, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Device(Base):
    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    object_id: Mapped[int] = mapped_column(ForeignKey("scada.objects.id"), nullable=False, index=True)
    external_id: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)  # {device_id} в топике
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    device_type: Mapped[str] = mapped_column(String(64), nullable=False)   # gas_meter|electricity_meter|temperature|...
    model: Mapped[str | None] = mapped_column(String(128))
    unit: Mapped[str | None] = mapped_column(String(32))                   # основная единица измерения
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))  # мониторинг offline (ТЗ п.14)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    # TODO: credential_ref — ссылка на креды MQTT (сами секреты в БД не храним)

    obj: Mapped["Object"] = relationship(back_populates="devices")  # noqa: F821

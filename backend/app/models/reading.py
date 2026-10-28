# -*- coding: utf-8 -*-
"""readings — показания; создаётся миграцией как TimescaleDB hypertable
по времени measured_at (ТЗ п.9, п.11).

Долгие времена измерений и приёма хранятся раздельно (ТЗ п.8).
Первичный ключ включает measured_at — требование сегментации hypertable.
"""
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, Numeric, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base
from app.models.quality import QualityCode


class Reading(Base):
    __tablename__ = "readings"  # -> hypertable в миграции 0001

    device_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("scada.devices.id"), primary_key=True)
    measured_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), primary_key=True)
    received_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)  # серверное UTC
    parameter: Mapped[str] = mapped_column(String(64), primary_key=True)  # напр. volume, temperature, pressure
    value: Mapped[float] = mapped_column(Numeric, nullable=False)         # исходное значение без изменений (ТЗ п.8)
    unit: Mapped[str | None] = mapped_column(String(32))
    quality: Mapped[QualityCode] = mapped_column(nullable=False, default=QualityCode.UNKNOWN)
    message_id: Mapped[str] = mapped_column(Text, nullable=False, index=True)  # дедупликация QoS1 (ТЗ п.5)
    sequence: Mapped[int | None] = mapped_column(BigInteger)

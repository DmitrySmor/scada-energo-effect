# -*- coding: utf-8 -*-
"""device_state — текущее состояние устройств (ТЗ п.11).

Обновляется только более новыми данными: поздние показания не перезаписывают
текущие значения (ТЗ п.8).
"""
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class DeviceState(Base):
    __tablename__ = "device_state"

    device_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("scada.devices.id"), primary_key=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    last_message_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    status: Mapped[str | None] = mapped_column(String(32))          # online/offline/error по статусам устройства
    current_values: Mapped[dict | None] = mapped_column(JSONB)       # последние значения по параметрам
    # TODO: service-логика сравнивает measured_at перед обновлением (защита от поздних данных)

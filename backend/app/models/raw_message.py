# -*- coding: utf-8 -*-
"""raw_messages — исходные сообщения, статусы обработки и причины ошибок
(ТЗ п.8, 11). Ошибочные сообщения сохраняются вместе с причиной отказа.
"""
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class RawMessageStatus:
    STORED = "stored"        # обработано и сохранено
    REJECTED = "rejected"    # отклонено (валидация/права/схема)
    DUPLICATE = "duplicate"  # повторная доставка того же message_id
    ERROR = "error"          # внутренняя ошибка обработки


class RawMessage(Base):
    __tablename__ = "raw_messages"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    message_id: Mapped[str] = mapped_column(Text, nullable=False, unique=True)  # дедупликация QoS 1 (ТЗ п.5)
    topic: Mapped[str] = mapped_column(Text, nullable=False)
    device_external_id: Mapped[str | None] = mapped_column(String(64))
    object_external_id: Mapped[str | None] = mapped_column(String(64))
    message_type: Mapped[str | None] = mapped_column(String(32))
    payload: Mapped[str] = mapped_column(Text, nullable=False)      # исходный JSON как есть (аудит, ТЗ п.7)
    status: Mapped[str] = mapped_column(String(16), nullable=False)
    error_code: Mapped[str | None] = mapped_column(String(64))
    error_reason: Mapped[str | None] = mapped_column(Text)
    received_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True))
    ack_published: Mapped[bool] = mapped_column(default=False)      # фиксируем отправку подтверждения (ТЗ п.5.1)

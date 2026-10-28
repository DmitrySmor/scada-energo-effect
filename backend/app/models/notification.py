# -*- coding: utf-8 -*-
"""notifications — уведомления компании (ТЗ п.14, 11).

Видимость только соответствующей компании, кроме admin. Повторяющиеся
уведомления подавляются/объединяются (dedup_key + окно подавления).
"""
from datetime import datetime

from sqlalchemy import BigInteger, DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Notification(Base):
    __tablename__ = "notifications"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    company_id: Mapped[int | None] = mapped_column(ForeignKey("scada.companies.id"), index=True)  # NULL — системные для admin
    device_id: Mapped[int | None] = mapped_column(BigInteger, ForeignKey("scada.devices.id"))
    kind: Mapped[str] = mapped_column(String(64), nullable=False)   # offline|connection_restored|processing_error|...
    severity: Mapped[str] = mapped_column(String(16), default="info")
    dedup_key: Mapped[str | None] = mapped_column(String(255), index=True)  # подавление повторов (ТЗ п.14)
    message: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    # TODO: delivered_at / delivery channels (расширение — ТЗ п.14)

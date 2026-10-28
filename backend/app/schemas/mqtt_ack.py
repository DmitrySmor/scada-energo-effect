# -*- coding: utf-8 -*-
"""Прикладное подтверждение обработки (ТЗ, п.5.1, 7.1).

stored  — данные зафиксированы в БД (публикуется только после commit!);
rejected— сообщение не принято, есть error_code/error_message.
TODO: полный перечень кодов результатов — docs/mqtt-error-codes.md (ТЗ п.21).
"""
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AckStatus(str, Enum):
    STORED = "stored"
    REJECTED = "rejected"


class MqttAck(BaseModel):
    schema_version: str = "1.0"
    message_id: str
    device_id: str
    status: AckStatus
    error_code: str | None = None
    error_message: str | None = None
    processed_at: datetime

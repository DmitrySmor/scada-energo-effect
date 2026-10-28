# -*- coding: utf-8 -*-
"""Общая схема входящего MQTT-сообщения (ТЗ, раздел 7).

Поле data валидируется отдельно — по JSON-схеме типа устройства
(schemas/device_data/), поэтому общая логика приёма не меняется при
добавлении нового оборудования (ТЗ п.7).
"""
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

ALLOWED_MESSAGE_TYPES = {"telemetry", "status", "diagnostics", "event"}


class MqttMessage(BaseModel):
    schema_version: str = Field(min_length=1)          # обязательно
    message_id: str = Field(min_length=1)              # уникален, не меняется при повторах
    device_id: str = Field(min_length=1)               # обязательно
    message_type: str = Field(min_length=1)            # обязательно
    data: dict[str, Any] = Field(default_factory=dict) # обязательно, схема по типу устройства
    measured_at: datetime | None = None                # необязательно
    sequence: int | None = None                        # необязательно (контроль разрывов)

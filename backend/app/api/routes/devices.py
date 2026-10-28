# -*- coding: utf-8 -*-
"""Устройства и данные (ТЗ, п.12):

  POST      /api/v1/devices                 — регистрация устройства (admin);
  GET/PATCH /api/v1/devices/{id}            — карточка устройства;
  GET       /api/v1/devices/{id}/readings   — история показаний (фильтры по
              времени/параметру/качеству + пагинация, ТЗ п.12);
  GET       /api/v1/devices/{id}/state      — текущее состояние (device_state);
  GET       /api/v1/devices/{id}/events     — события (device_events).

API возвращает только сохранённые данные и НЕ рассчитывает показатели (ТЗ, п.1).
"""
from fastapi import APIRouter

router = APIRouter()

# TODO(реализация): проверка принадлежности устройства компании пользователя


@router.post("", status_code=201)
async def register_device() -> None:
    raise NotImplementedError("TODO: регистрация устройства (admin), генерация кредов MQTT")


@router.get("/{device_id}")
async def get_device(device_id: int) -> None:
    raise NotImplementedError("TODO: карточка устройства с проверкой прав")


@router.patch("/{device_id}")
async def update_device(device_id: int) -> None:
    raise NotImplementedError("TODO: изменение устройства (admin)")


@router.get("/{device_id}/readings")
async def list_readings(device_id: int) -> None:
    raise NotImplementedError("TODO: запрос к hypertable readings + фильтры + пагинация")


@router.get("/{device_id}/state")
async def get_state(device_id: int) -> None:
    raise NotImplementedError("TODO: device_state")


@router.get("/{device_id}/events")
async def list_events(device_id: int) -> None:
    raise NotImplementedError("TODO: device_events")

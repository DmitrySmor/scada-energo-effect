# -*- coding: utf-8 -*-
"""Объекты учёта (ТЗ, п.12):

  GET/POST  /api/v1/objects            — список и создание (создание — admin);
  GET/PATCH /api/v1/objects/{id}       — получение и изменение;
  GET       /api/v1/objects/{id}/devices.

Правила доступа (ТЗ, п.10): role=user видит только объекты своей компании,
проверка на сервере при каждом запросе; подмена id не даёт доступ к чужим данным.
"""
from fastapi import APIRouter

router = APIRouter()

# TODO(реализация): эндпоинты + фильтрация по company_id через deps.require_company_scope


@router.get("")
async def list_objects() -> None:
    raise NotImplementedError("TODO: список объектов компании (или всех — для admin)")


@router.post("", status_code=201)
async def create_object() -> None:
    raise NotImplementedError("TODO: создание объекта (только admin)")


@router.get("/{object_id}")
async def get_object(object_id: int) -> None:
    raise NotImplementedError("TODO: получить объект с проверкой прав компании")


@router.patch("/{object_id}")
async def update_object(object_id: int) -> None:
    # Согласовано (2026-10-29): PATCH объекта доступен только роли admin.
    raise NotImplementedError("TODO: изменить объект (только admin)")


@router.get("/{object_id}/devices")
async def list_object_devices(object_id: int) -> None:
    raise NotImplementedError("TODO: приборы объекта")

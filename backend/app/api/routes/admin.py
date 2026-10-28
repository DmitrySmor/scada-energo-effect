# -*- coding: utf-8 -*-
"""Администрирование пользователей (ТЗ, п.12): GET/POST/PATCH /api/v1/admin/users.

Доступно только роли admin (ТЗ, п.10). Логировать административные действия (п.15).
"""
from fastapi import APIRouter

router = APIRouter()

# TODO(реализация): require_role("admin") + CRUD users/companies


@router.get("/users")
async def list_users() -> None:
    raise NotImplementedError("TODO: список пользователей (admin)")


@router.post("/users", status_code=201)
async def create_user() -> None:
    raise NotImplementedError("TODO: создать компанию/аккаунт user или admin (admin)")


@router.patch("/users/{user_id}")
async def update_user(user_id: int) -> None:
    raise NotImplementedError("TODO: изменить пользователя/роль (admin)")

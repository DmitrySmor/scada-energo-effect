# -*- coding: utf-8 -*-
"""Схемы пользователей и GET /me (ТЗ п.10, 12)."""
from pydantic import BaseModel


class MeResponse(BaseModel):
    id: int
    login: str
    role: str                      # admin | user
    company_id: int | None
    company_name: str | None


class UserCreate(BaseModel):
    login: str
    role: str
    company_id: int | None = None  # обязателен для роли user
    password: str                  # хешируется перед сохранением (ТЗ п.15)

# -*- coding: utf-8 -*-
"""Схема ответа аутентификации (POST /api/v1/auth/login)."""
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in_minutes: int

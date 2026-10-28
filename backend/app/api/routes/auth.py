# -*- coding: utf-8 -*-
"""Аутентификация (ТЗ, п.12): POST /api/v1/auth/login.

Механизм — JWT (выбран по умолчанию, окончательное согласование — ТЗ п.21).
"""
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.security import create_access_token, verify_password
from app.db.session import get_session
from app.models.user import User
from app.schemas.token import Token

router = APIRouter()


@router.post("/login", response_model=Token)
async def login(
    form: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
) -> Token:
    """Выдача короткоживущего JWT по логину/паролю.

    TODO(реализация): загрузка пользователя, проверка хеша пароля,
    ограничение частоты попыток входа (ТЗ, п.15), лог событий безопасности.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="TODO: реализовать проверку учётных данных",
    )

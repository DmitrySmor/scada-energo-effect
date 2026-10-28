# -*- coding: utf-8 -*-
"""Зависимости FastAPI: аутентификация и авторизация (ТЗ, п.10, 12, 15).

Все бизнес-эндпоинты требуют аутентификацию; административные — роль admin;
role=user получает доступ только к данным своей компании (проверка на сервере
при каждом защищённом запросе, подмена ID блокируется).
"""
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from app.core.security import decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    """Разбор JWT и загрузка пользователя. TODO: проверка существования в БД."""
    try:
        payload = decode_access_token(token)
    except Exception:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Недействительный токен")
    # TODO: SELECT user WHERE id = payload["sub"]; вернуть ORM-объект User
    return payload


CurrentUserDep = Annotated[dict, Depends(get_current_user)]


def require_admin(current_user: CurrentUserDep) -> dict:
    """Доступ только для роли admin (ТЗ, п.10)."""
    if current_user.get("role") != "admin":
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Требуются права администратора")
    return current_user


AdminDep = Annotated[dict, Depends(require_admin)]

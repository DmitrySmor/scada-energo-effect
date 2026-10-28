# -*- coding: utf-8 -*-
"""Безопасность: хеширование паролей и JWT (ТЗ, п.15).

Пароли хранятся только в виде безопасных хешей (bcrypt/argon2 через passlib).
Секреты — только из окружения.
"""
from datetime import datetime, timedelta, timezone
from typing import Any

from jose import jwt

from app.core.config import settings

ALGORITHM = "HS256"


def hash_password(password: str) -> str:
    """Хеш пароля для таблицы users. TODO: passlib[bcrypt]."""
    raise NotImplementedError("TODO: passlib CryptContext(bcrypt)")


def verify_password(plain: str, hashed: str) -> bool:
    """Проверка пароля по хешу."""
    raise NotImplementedError("TODO: passlib verify")


def create_access_token(subject: dict[str, Any], expires_minutes: int | None = None) -> str:
    """Выпуск JWT с claims: sub (user id), role, company_id (ТЗ, п.10)."""
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    payload = {**subject, "exp": expire}
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str) -> dict[str, Any]:
    """Проверка подписи и срока действия токена; ошибки -> 401 на уровне deps."""
    return jwt.decode(token, settings.SECRET_KEY, algorithms=[ALGORITHM])

# -*- coding: utf-8 -*-
"""Эндпоинты проверки здоровья (ТЗ, п.12).

Доступны без аутентификации:
  GET /api/v1/health/live  — процесс жив;
  GET /api/v1/health/ready — сервисы (БД, MQTT) доступны.
"""
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_session

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/live")
async def live() -> dict:
    """Проверка работоспособности процесса (без внешних зависимостей)."""
    return {"status": "ok"}


@router.get("/ready")
async def ready(session: AsyncSession = Depends(get_session)) -> dict:
    """Проверка готовности: доступность PostgreSQL/TimescaleDB."""
    from sqlalchemy import text

    await session.execute(text("SELECT 1"))
    # TODO: добавить проверку подключения к MQTT (broker connected flag).
    return {"status": "ready", "database": "ok"}

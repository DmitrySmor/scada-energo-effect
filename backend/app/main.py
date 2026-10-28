# -*- coding: utf-8 -*-
"""Точка входа FastAPI приложения (ТЗ, раздел 12).

Запуск в контейнере api:
    uvicorn app.main:app --host 0.0.0.0 --port 8000
"""
from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="0.1.0",
    docs_url="/docs",           # Swagger UI (ТЗ, п.12)
    openapi_url="/openapi.json",
)

# Все бизнес-эндпоинты под префиксом /api/v1/
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def root() -> dict:
    """Корневой маршрут — только служебная информация."""
    return {"service": settings.PROJECT_NAME, "status": "ok"}

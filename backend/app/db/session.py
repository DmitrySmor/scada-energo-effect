# -*- coding: utf-8 -*-
"""Сессии SQLAlchemy (asyncpg) для PostgreSQL/TimescaleDB."""
from collections.abc import AsyncIterator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

engine = create_async_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_session() -> AsyncIterator[AsyncSession]:
    """DI-зависимость: одна транзакционная сессия на запрос (ТЗ, п.9)."""
    async with SessionLocal() as session:
        yield session

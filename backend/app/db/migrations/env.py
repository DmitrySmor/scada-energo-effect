# -*- coding: utf-8 -*-
"""Окружение Alembic для миграций SCADA Backend.

Запуск (из контейнера migrate):  alembic upgrade head
URL БД берётся из настроек приложения (env), не из alembic.ini.
"""
from alembic import context

from app.core.config import settings
from app.models.base import Base
import app.models  # noqa: F401  — регистрация всех моделей в metadata

config = context.config
config.set_main_option("sqlalchemy.url", settings.database_url.replace("%", "%%"))

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(url=settings.database_url, target_metadata=target_metadata,
                      literal_binds=True, schema="scada")
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    from sqlalchemy import create_engine
    engine = create_engine(settings.database_url.replace("+asyncpg", "+psycopg2"))
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata, schema="scada")
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

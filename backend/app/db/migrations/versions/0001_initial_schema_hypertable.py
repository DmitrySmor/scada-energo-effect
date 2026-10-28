# -*- coding: utf-8 -*-
"""0001 — начальная схема и hypertable readings (ТЗ п.9, 11).

Заготовка первой миграции. Таблицы создаются по metadata моделей;
после создания readings обязательно превращение в hypertable TimescaleDB
по колонке measured_at + индексы под сценарии запросов (устройство,
параметр, диапазон времени).

TODO(разработчик): сгенерировать ops через `alembic revision --autogenerate`
и дополнить секцию TimescaleDB ниже.
"""
from alembic import op

revision = "0001"
down_revision = None

CHUNK_INTERVAL = "7 days"   # размер chunk-changes согласовать с объёмом данных (ТЗ п.18)


def upgrade() -> None:
    # 1. Обычные таблицы: companies, users, objects, devices, device_state,
    #    device_events, raw_messages, notifications (metadata моделей).
    # TODO: op.create_table(...) или autogenerate.

    # 2. readings — обычная таблица на этапе создания...
    # TODO: op.create_table("readings", ... из app.models.reading)

    # 3. ...затем превращаем в hypertable TimescaleDB (ТЗ п.9, критерий 5):
    op.execute(
        f"SELECT create_hypertable('scada.readings', 'measured_at', "
        f"chunk_time_interval => INTERVAL '{CHUNK_INTERVAL}')"
    )

    # 4. Индексы под основные запросы (ТЗ п.9):
    op.execute("CREATE INDEX IF NOT EXISTS ix_readings_device_param_time "
               "ON scada.readings (device_id, parameter, measured_at DESC)")
    op.execute("CREATE INDEX IF NOT EXISTS ix_readings_message_id "
               "ON scada.readings (message_id)")


def downgrade() -> None:
    # Гипертаблицу удаляем как обычную таблицу; остальное — по metadata.
    op.execute("DROP TABLE IF EXISTS scada.readings")
    # TODO: удаление остальных таблиц

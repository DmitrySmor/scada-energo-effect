# backend/ — код SCADA Backend (FastAPI)

Структура (соответствие разделам ТЗ):

```
app/
  main.py        — точка входа FastAPI (раздел 12)
  core/          — настройки из env (config.py), безопасность (security.py),
                   аутентификация/авторизация (deps.py)   [разделы 10, 12, 15]
  db/            — сессии SQLAlchemy; migrations/ — Alembic (гипертаблица readings) [раздел 9]
  models/        — ORM: companies, users, objects, devices, readings,
                   device_state, device_events, raw_messages, notifications [раздел 11]
  schemas/       — Pydantic-схемы API и MQTT; device_data/ — JSON-схемы оборудования [разделы 7, 12]
  mqtt/          — worker (приём QoS 1), client, services: message_processor,
                   ack_publisher (прикладные подтверждения) [разделы 4–8]
  services/      — device_registry, data_validator, monitoring [разделы 8, 13, 14]
  api/routes/    — auth, me, objects, devices, admin, health [раздел 12]
tests/           — pytest
```

Все заглушки помечены `TODO(реализация)` — каркас показывает, где что lives,
не содержа рабочей бизнес-логики.

Локальный запуск: `poetry install && poetry run uvicorn app.main:app --reload`
(нужны доступные PostgreSQL/TimescaleDB и Mosquitto — см. корневой compose.yaml).

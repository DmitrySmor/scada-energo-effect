# Архитектура (каркас по ТЗ)

Сервисы (compose.yaml):

| Сервис        | Назначение                                             | Раздел ТЗ |
|---------------|--------------------------------------------------------|-----------|
| postgres      | PostgreSQL + TimescaleDB (hypertable readings)         | 9         |
| mosquitto     | MQTT-брокер: TLS :8883, аутентификация, ACL           | 4–6       |
| api           | FastAPI REST /api/v1/ + Swagger                        | 12        |
| mqtt-worker   | приём QoS1, валидация, дедупликация, запись, ack      | 5–8       |
| scheduler     | мониторинг offline, уведомления, ротация               | 14        |
| migrate       | Alembic upgrade head (профиль tools)                   | 9, 11     |
| backup        | pg_dump в отдельный диск (профиль backup)              | 17        |

Поток данных: устройство -> mqtts://:8883 -> mosquitto -> mqtt-worker
(валидация схемы устройства, реестр устройств, транзакция) -> postgres/TimescaleDB
-> commit -> ack "stored" в scada/v1/{object}/{device}/ack -> устройство.

REST читает только сохранённые данные; расчёты не выполняются (ТЗ п.1).

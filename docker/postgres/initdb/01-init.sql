-- =============================================================================
-- Первоначальная настройка PostgreSQL/TimescaleDB (выполняется автоматически
-- при первом создании кластера, ТЗ п.9). Скрипты из этого каталога запускаются
-- docker-entrypoint образа timescaledb в алфавитном порядке.
-- =============================================================================

-- Включаем расширение TimescaleDB для базы проекта
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Схема приложения (миграции Alembic будут работать внутри неё)
CREATE SCHEMA IF NOT EXISTS scada;

-- Полезные расширения для работы с JSON и UUID
CREATE EXTENSION IF NOT EXISTS pgcrypto;   -- gen_random_uuid()
CREATE EXTENSION IF NOT EXISTS citext;     -- регистронезависимые строки (email/логины)

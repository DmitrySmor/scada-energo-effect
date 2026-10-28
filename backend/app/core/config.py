# -*- coding: utf-8 -*-
"""Настройки приложения из переменных окружения (Pydantic Settings, ТЗ п.15).

Все секреты приходят только из окружения (.env), никогда из кода/Git.
"""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # --- Общее -------------------------------------------------------------
    PROJECT_NAME: str = "SCADA Backend"
    LOG_LEVEL: str = "INFO"

    # --- PostgreSQL / TimescaleDB ------------------------------------------
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    # --- REST API / безопасность --------------------------------------------
    SECRET_KEY: str                       # подпись JWT (согласование — ТЗ п.21)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    RATE_LIMIT_PER_MINUTE: int = 60
    FIRST_ADMIN_EMAIL: str = "admin@example.com"
    FIRST_ADMIN_PASSWORD: str             # создаётся при первоначальной настройке

    # --- MQTT ----------------------------------------------------------------
    MQTT_HOST: str = "mosquitto"
    MQTT_PORT: int = 1883                 # внутренняя сеть; снаружи TLS :8883
    MQTT_USERNAME: str
    MQTT_PASSWORD: str
    MQTT_BASE_TOPIC: str = "scada/v1"     # scada/v1/{object_id}/{device_id}/{type}
    MQTT_ACK_SUFFIX: str = "ack"          # топик прикладных подтверждений

    # --- Мониторинг устройств (ТЗ п.14) ----------------------------------------
    DEVICE_OFFLINE_AFTER_MINUTES: int = 60


@lru_cache
def get_settings() -> Settings:
    """Кэш настроек: читается один раз за процесс."""
    return Settings()  # type: ignore[call-arg]


settings = get_settings()

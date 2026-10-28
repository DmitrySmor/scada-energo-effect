#!/usr/bin/env bash
# =============================================================================
# Деплой проекта на сервер (Debian 13). Репозиторий = /opt/docker/iot-project/.
# Использование: sudo ./deploy/deploy.sh
# =============================================================================
set -euo pipefail

PROJECT_DIR="/opt/docker/iot-project"
cd "$PROJECT_DIR"

echo "[1/5] Обновление кода из main..."
git pull --ff-only origin main

echo "[2/5] Проверка внешней сети proxy (проект её не создаёт — ТЗ п.3)..."
docker network inspect proxy >/dev/null 2>&1 || {
  echo "ОШИБКА: сеть 'proxy' не найдена. Создайте её вне проекта: docker network create proxy"; exit 1; }

echo "[3/5] Каталоги данных /data/<container_name> и права (UID/GID контейнеров)..."
install -d -o 999  -g 999  /data/postgres                       # postgres/timescaledb
install -d -o 100  -g 100  /data/mosquitto/data /data/mosquitto/log  # mosquitto
[ -f .env ] || { echo "ОШИБКА: отсутствует .env (cp .env.example .env и заполните)"; exit 1; }

echo "[4/5] Сборка образов и запуск сервисов..."
docker compose build
docker compose up -d

echo "[5/5] Миграции БД (создание схемы и hypertable readings)..."
docker compose --profile tools run --rm migrate

echo "Готово. Проверка: curl https://<хост>/api/v1/health/ready"

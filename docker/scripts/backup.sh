#!/bin/sh
# =============================================================================
# Резервное копирование PostgreSQL/TimescaleDB (ТЗ, п.17).
# Запускается контейнером backup:
#   docker compose --profile backup run --rm backup
# или из cron на хосте (рекомендуется nightly).
#
# Результат: /backups/scada_<дата>.dump — дамп в формате custom (-Fc),
# пригодный для pg_restore. Каталог /backups — bind mount отдельного диска!
# =============================================================================
set -eu

TIMESTAMP=$(date -u +%Y%m%d_%H%M%S)
OUT="/backups/scada_${TIMESTAMP}.dump"
RETAIN_DAYS="${BACKUP_RETAIN_DAYS:-30}"    # срок хранения копий (согласовать RPO/RTO)

echo "[$(date -u -Is)] Начало резервного копирования ${POSTGRES_DB} -> ${OUT}"

# Дамп всей базы с учётом hypertables TimescaleDB
pg_dump \
  -h postgres -U "${POSTGRES_USER}" -d "${POSTGRES_DB}" \
  -Fc -Z gzip:6 \
  -f "${OUT}"

# Контрольная сумма для проверки целостности при восстановлении
sha256sum "${OUT}" > "${OUT}.sha256"

# Удаление старых копий (проще всего; ротацию можно вынести в отдельную задачу)
find /backups -name 'scada_*.dump*' -mtime "+${RETAIN_DAYS}" -delete

echo "[$(date -u -Is)] Готово: ${OUT} ($(du -h "${OUT}" | cut -f1))"

# ВАЖНО (ТЗ, п.17): копии должны храниться вне основного диска с данными.
# На сервере смонтируйте отдельный диск в BACKUP_DIR из .env (по умолчанию
# /backups/iot-project) и настройте репликацию копий в удалённое хранилище.

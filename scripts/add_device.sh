#!/usr/bin/env bash
# =============================================================================
# Регистрация MQTT-учётных данных устройства в файле passwd брокера.
# Использование:  ./scripts/add_device.sh <device_id> [пароль]
# Пароль генерируется, если не передан. Устройство получает индивидуальные
# креды; ACL (docker/mosquitto/acl) ограничивает его собственными топиками.
# Отзыв/замена: удалить строку пользователя из passwd и перегенерировать.
# =============================================================================
set -euo pipefail
DEVICE_ID="${1:?usage: add_device.sh <device_id> [password]}"
PASSWORD="${2:-$(openssl rand -base64 24)}"
PASSWD_FILE="$(dirname "$0")/../docker/mosquitto/passwd"

if id -u mosquitto >/dev/null 2>&1 || docker ps --format '{{.Names}}' | grep -q '^mosquitto$'; then
  # хеш внутри контейнера брокера — корректный формат mosquitto_passwd
  docker exec mosquitto mosquitto_passwd -b /mosquitto/config/passwd "$DEVICE_ID" "$PASSWORD" \
    && docker exec mosquitto kill 1 2>/dev/null || true
else
  touch "$PASSWD_FILE"
  docker run --rm -v "$PASSWD_FILE":/passwd eclipse-mosquitto:2 \
    mosquitto_passwd -b /passwd "$DEVICE_ID" "$PASSWORD"
fi

echo "Устройство '$DEVICE_ID' добавлено. Пароль (передать монтажнику, в Git не сохранять!): $PASSWORD"

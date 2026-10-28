# -*- coding: utf-8 -*-
"""MQTT-воркер: приём сообщений от брокера (ТЗ, разделы 5–8).

Запуск в контейнере mqtt-worker:  python -m app.mqtt.worker

Обработка одного сообщения (app.mqtt.services.message_processor):
  1. парсинг JSON и общей схемы;
  2. проверка регистрации устройства, объекта учёта и права публикации в топик;
  3. валидация data по схеме типа устройства;
  4. идемпотентная запись (дедупликация по message_id) в транзакции;
  5. commit -> публикация прикладного подтверждения stored (только после фиксации!);
     при отказе — rejected с error_code.
TODO(реализация): цикл reconnect/backoff, graceful shutdown, метрики обработки.
"""
import asyncio
import logging

logger = logging.getLogger("scada.mqtt.worker")


async def main() -> None:
    logger.info("MQTT worker стартует...")
    # TODO: создать MQTT-клиник (aiomqtt), подписаться на scada/v1/#/+/{telemetry|status|diagnostics|event}
    #       c QoS 1 и передавать сообщения в MessageProcessor.
    raise NotImplementedError("TODO: подключить aiomqtt и MessageProcessor")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

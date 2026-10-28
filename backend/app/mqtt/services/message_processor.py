# -*- coding: utf-8 -*-
"""Обработчик входящего MQTT-сообщения (ТЗ, раздел 8).

Псевдокод конвейера:
    raw = parse_json(payload)                        -> иначе rejected PARSE_ERROR
    msg = MqttMessage.validate(raw)                  -> иначе rejected SCHEMA_ERROR
    device = registry.check(msg.device_id, topic)    -> иначе rejected UNKNOWN_DEVICE / TOPIC_MISMATCH
    schema = device_data.get_schema(device.type)     -> data валидация, иначе VALIDATION_ERROR
    with transaction():
        if dedup.exists(msg.message_id): return согласованный результат (без дублей!)
        store raw_messages + readings/events/device_state (поздние данные не перезаписывают current)
        commit()                                     -> только теперь публикуем ack "stored"
"""

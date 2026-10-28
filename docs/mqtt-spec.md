# Спецификация MQTT (заготовка; точные значения — согласование, ТЗ п.21)

* Topics publish: `scada/v1/{object_id}/{device_id}/{telemetry|status|diagnostics|event}` (QoS 1)
* Topics ack:     `scada/v1/{object_id}/{device_id}/ack` (QoS 1, только своё устройство по ACL)
* Формат сообщения и подтверждения — ТЗ разделы 7 и 7.1
* TLS обязателен снаружи (:8883), анонимный доступ запрещён
* message_id — уникальный идентификатор логического сообщения, ключ идемпотентности

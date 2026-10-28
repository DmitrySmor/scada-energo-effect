# -*- coding: utf-8 -*-
"""MQTT-клиент backend'а (aiomqtt) — подключение к брокеру по внутренней сети.

Используется воркером (подписка scada/v1/#, QoS 1) и сервисом ack_publisher
(публикация подтверждений в scada/v1/{object_id}/{device_id}/ack, QoS 1).
TODO(реализация): reconnect с экспоненциальным backoff, общий клиент для процессов.
"""

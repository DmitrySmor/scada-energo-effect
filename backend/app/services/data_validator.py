# -*- coding: utf-8 -*-
"""Валидация поля data по JSON-схеме типа устройства (ТЗ, п.7–8).

Реестр схем: schemas/device_data/*.json, ключ — device_type.message_type.
Добавление нового оборудования = новый файл схемы, без изменения кода приёма.
Здесь же — правила присвоения quality (valid/invalid/suspect/unknown, ТЗ п.13)
и нарушения sequence (ТЗ п.8).
"""

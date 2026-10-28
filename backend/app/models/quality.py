# -*- coding: utf-8 -*-
"""Статусы качества показаний (ТЗ, раздел 13)."""
import enum


class QualityCode(str, enum.Enum):
    VALID = "valid"      # корректные данные
    INVALID = "invalid"  # не прошли обязательную проверку
    SUSPECT = "suspect"  # приняты, но есть признаки некорректности
    UNKNOWN = "unknown"  # качество не определено

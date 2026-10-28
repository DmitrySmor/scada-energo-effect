# -*- coding: utf-8 -*-
"""Declarative-база всех ORM-моделей (схема scada, ТЗ п.11)."""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    __table_args__ = {"schema": "scada"}

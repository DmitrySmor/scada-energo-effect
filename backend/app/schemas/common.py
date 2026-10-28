# -*- coding: utf-8 -*-
"""Общие схемы: пагинация и ответы с ошибками (ТЗ п.12, 15)."""
from pydantic import BaseModel, Field


class PageMeta(BaseModel):
    page: int = Field(ge=1)
    per_page: int = Field(ge=1, le=1000)
    total: int | None = None


class ErrorDetail(BaseModel):
    """Единый формат ошибок API; коды документируются в OpenAPI (ТЗ п.12)."""
    code: str
    message: str

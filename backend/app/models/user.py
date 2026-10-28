# -*- coding: utf-8 -*-
"""users — учётные записи и роли admin/user (ТЗ п.10–11).

role=user — аккаунт компании (не сотрудника), ровно одна компания.
Пароли — только безопасные хеши (ТЗ п.15).
"""
import enum

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Role(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    login: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[Role] = mapped_column(nullable=False, default=Role.USER)
    company_id: Mapped[int | None] = mapped_column(ForeignKey("scada.companies.id"))
    # Для admin company_id NULL; для user — обязателен (проверка на уровне сервиса/миграции)

    company: Mapped["Company | None"] = relationship(back_populates="users")  # noqa: F821

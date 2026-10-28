# -*- coding: utf-8 -*-
"""companies — компании-клиенты (юридические лица), ТЗ п.10–11."""
from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    inn: Mapped[str | None] = mapped_column(String(12))
    # TODO: реквизиты, контакты, признаки активности

    users: Mapped[list["User"]] = relationship(back_populates="company")  # noqa: F821
    objects: Mapped[list["Object"]] = relationship(back_populates="company")  # noqa: F821

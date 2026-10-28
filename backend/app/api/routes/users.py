# -*- coding: utf-8 -*-
"""GET /api/v1/me — текущий пользователь, компания и роль (ТЗ, п.12)."""
from fastapi import APIRouter, Depends

from app.core.deps import CurrentUserDep
from app.schemas.user import MeResponse

router = APIRouter()


@router.get("/me", response_model=MeResponse)
async def me(current_user: CurrentUserDep) -> MeResponse:
    """Возвращает данные аутентифицированного пользователя.

    TODO(реализация): собрать роль и company_id из токена и БД.
    """
    raise NotImplementedError("TODO: вернуть MeResponse из current_user")

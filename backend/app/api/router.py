# -*- coding: utf-8 -*-
"""Сводный роутер API (ТЗ, раздел 12).

| Методы           | Путь                             | Модуль              |
|------------------|----------------------------------|---------------------|
| POST             | /auth/login                      | routes/auth.py      |
| GET              | /me                              | routes/users.py     |
| GET/POST         | /objects                         | routes/objects.py   |
| GET/PATCH        | /objects/{id}                    | routes/objects.py   |
| GET              | /objects/{id}/devices            | routes/objects.py   |
| POST             | /devices                         | routes/devices.py   |
| GET/PATCH        | /devices/{id}                    | routes/devices.py   |
| GET              | /devices/{id}/readings|state|events | routes/devices.py   |
| GET/POST/PATCH   | /admin/users                     | routes/admin.py     |
| GET              | /health/live, /health/ready      | routes/health.py    |
"""
from fastapi import APIRouter

from app.api.routes import admin, auth, devices, health, objects, users

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, tags=["users"])
api_router.include_router(objects.router, prefix="/objects", tags=["objects"])
api_router.include_router(devices.router, prefix="/devices", tags=["devices"])
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])

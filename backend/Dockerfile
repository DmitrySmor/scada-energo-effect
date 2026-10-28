# ============================================================================
# Образ backend для сервисов api / mqtt-worker / scheduler / migrate
# (один образ, разные команды запуска в compose.yaml).
# ============================================================================
FROM python:3.12-slim

# Только чтение + отсутствие кэша pip — быстрее и безопаснее
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /srv/scada

# Копируем файлы зависимостей раньше кода — слой кешируется
COPY pyproject.toml README.md ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-interaction

# Код приложения
COPY app ./app

# Небольшой непривилегированный пользователь (ТЗ п.15)
RUN useradd -m -u 10001 appuser
USER appuser

EXPOSE 8000
# По умолчанию — API; остальные сервисы переопределяют command в compose.yaml
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

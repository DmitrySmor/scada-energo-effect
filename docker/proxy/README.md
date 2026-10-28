# Интеграция с reverse-proxy (сеть `proxy`)

REST API должен быть доступен по HTTPS через существующий reverse-proxy
(Трафик: локальная сеть/VPN, публичные маршруты — только согласованные, ТЗ п.15).

Пример фрагмента конфигурации прокси (Caddy/Traefik/nginx — как в вашем стеке):

```
# upstream: http://api:8000 (сервис доступен по имени в docker-сети proxy)
location /api/ {
    proxy_pass http://api:8000;
    proxy_set_header X-Forwarded-Proto https;
    proxy_set_header X-Real-IP $remote_addr;   # для rate limiting (ТЗ п.15)
}
```

Swagger UI: https://<хост>/docs ; OpenAPI: /openapi.json.
Сетевой порт MQTT 8883 публикуется контейнером mosquitto напрямую на хост.

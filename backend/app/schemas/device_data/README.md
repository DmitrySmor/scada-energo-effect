# JSON-схемы данных оборудования (ТЗ, п.7)

Ключ схемы: `<device_type>.<message_type>.json`, например `gas_meter.telemetry.json`.

Правила:
* каждая схема описывает параметры, типы значений и единицы измерения;
* валидацию выполняет `app/services/data_validator.py` (библиотека jsonschema);
* добавление нового типа оборудования = новый файл здесь + регистрация device_type
  в БД; общая логика приёма MQTT не меняется (ТЗ, п.7).

Пример (газовый счётчик, телеметрия):

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "required": ["total_volume"],
  "properties": {
    "total_volume": {"type": "number", "minimum": 0, "description": "м3"},
    "temperature":  {"type": "number", "description": "°C"}
  },
  "additionalProperties": false
}

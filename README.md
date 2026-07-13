# Weather Forecast Analyzer

Навчальний Python-проєкт для збору, збереження та порівняння прогнозів погоди з фактичними погодними даними.

Головна ідея проєкту: отримати прогноз на майбутню дату, зберегти його разом із датою збору, а пізніше завантажити фактичні дані за ту саму дату та порахувати похибку прогнозу залежно від `lead_days`.

> Проєкт перебуває в активній розробці. Архітектура та окремі частини ще можуть змінюватися.

## Що вже вміє проєкт

- знаходити міста через Open-Meteo Geocoding API;
- отримувати погодинний прогноз через Open-Meteo Forecast API;
- отримувати архівні фактичні погодні дані через Open-Meteo Archive API;
- розділяти погодинні дані по окремих датах;
- створювати об'єкти `City`, `Forecast` та `Observation`;
- зберігати історію прогнозів у JSON;
- відновлювати об'єкти з JSON;
- знаходити пари `forecast` / `observation` за однаковою `target_date`;
- порівнювати прогнозовану і фактичну температуру;
- рахувати `error`, `abs_error` та зведення за `lead_days`;
- зберігати результати порівняння у CSV;
- зберігати одиниці вимірювання погодних метрик окремо від погодинних рядків.

## Логіка роботи

```text
City
  |
  +--> Forecast API
  |       |
  |       +--> hourly data
  |       +--> hourly_units
  |       |
  |       +--> Forecast objects by target_date
  |       |
  |       +--> JSON history
  |
  +--> Archive API
          |
          +--> hourly data
          +--> hourly_units
          |
          +--> Observation objects by target_date

Forecast + Observation
          |
          +--> match by target_date
          |
          +--> comparison DataFrame
          |
          +--> error / abs_error
          |
          +--> lead_days summary
          |
          +--> CSV
```

## Основні погодні метрики

Наразі в `settings.py` використовуються такі погодинні змінні:

- `temperature_2m`
- `apparent_temperature`
- `precipitation`
- `precipitation_probability`
- `relative_humidity_2m`
- `dew_point_2m`
- `rain`
- `showers`
- `snowfall`
- `shortwave_radiation`
- `wet_bulb_temperature_2m`
- `cape`
- `lifted_index`

Одиниці вимірювання з `hourly_units` не дублюються у кожному рядку DataFrame. Вони зберігаються окремо в атрибуті `units` об'єктів `Forecast` та `Observation`.

## Основні класи

### `City`

Зберігає дані міста, список прогнозів та список фактичних спостережень.

### `Forecast`

Один об'єкт представляє прогноз для конкретної `target_date`.

Основні поля:

- `city_name`
- `source`
- `latitude`
- `longitude`
- `collected_date`
- `target_date`
- `weather_data`
- `units`

Властивість `lead_days` показує, за скільки днів до цільової дати був отриманий прогноз.

### `Observation`

Один об'єкт представляє фактичні погодні дані для конкретної `target_date`.

Основні поля:

- `city_name`
- `source`
- `latitude`
- `longitude`
- `target_date`
- `weather_data`
- `units`

## Структура проєкту

```text
Weather-forecast-analyzer/
├── analytics/          # Порівняння прогнозів та фактичних даних
├── api_clients/        # Запити до Open-Meteo API
├── behavior_scripts/   # Сценарії створення City / Observation
├── models/             # City, Forecast, Observation
├── parsers/            # Перетворення API-відповідей у DataFrame
├── storage/            # Збереження та завантаження JSON / CSV
├── support_item/       # Допоміжні функції та перевірки стану прогнозів
├── test/               # Місце для майбутніх тестів
├── main.py             # Поточний сценарій запуску
├── settings.py         # URL, шляхи та список погодних параметрів
└── requirements.txt    # Залежності проєкту
```

## Встановлення

Клонувати репозиторій та перейти до папки проєкту:

```bash
git clone https://github.com/bardo-sama/Weather-forecast-analyzer.git
cd Weather-forecast-analyzer
```

Створити віртуальне середовище:

```bash
python -m venv .venv
```

Активувати його.

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
source .venv/Scripts/activate
```

Встановити залежності:

```bash
pip install -r requirements.txt
```

## Запуск

Поточний сценарій запускається через:

```bash
python main.py
```

`main.py` зараз використовується як робоча точка зборки пайплайна та ручної перевірки результатів.

## Результати

Прогнози зберігаються приблизно за схемою:

```text
data/
└── forecasts/
    └── <city>/
        └── <source>/
            └── <collected_date>.json
```

Результати порівняння:

```text
data/
└── comparison/
    └── <city>/
        └── <source>/
            ├── comparison_<date>.csv
            └── lead_days_summary_<date>.csv
```

## Метрики похибки

Для температури зараз використовуються:

```text
error = forecast_temp - observed_temp
abs_error = abs(error)
```

Додатково формується зведення за `lead_days`:

- `mean_error`
- `mean_abs_error`
- `max_abs_error`
- `rows_compared`

## Поточний напрям розвитку

Наступні логічні кроки проєкту:

- розширити порівняння на додаткові погодні метрики;
- додати графіки залежності похибки від `lead_days`;
- доробити завантаження та повторне використання результатів;
- додати автоматизовані тести після стабілізації основної логіки.

## Технології

- Python
- pandas
- requests
- requests-cache
- matplotlib
- pathlib
- JSON / CSV
- Open-Meteo API

## Примітка

Це навчальний проєкт, який розвивається поступово: спочатку робоча логіка, потім спрощення, тести та рефакторинг. Так код має шанс залишитися зрозумілим своєму автору хоча б довше за один вечір.

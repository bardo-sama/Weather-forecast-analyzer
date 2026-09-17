from pathlib import Path

BASE_DIR_CACHE = Path('cache')
BASE_DIR_DATA = Path('data')


CITY_CACHE = BASE_DIR_CACHE / 'city_name_cache'
FORECAST_CACHE = BASE_DIR_CACHE / 'forecast_weather_cache'
OBSERVATION_CACHE = BASE_DIR_CACHE / 'observation_weather_cache'


REQUEST_NAME_URL = "https://geocoding-api.open-meteo.com/v1/search"
REQUEST_WEATHER_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
REQUEST_WEATHER_OBSERVATION_URL = "https://archive-api.open-meteo.com/v1/archive"

PARAMS = ["temperature_2m", "apparent_temperature", "precipitation", "precipitation_probability",
          "relative_humidity_2m", "dew_point_2m", "rain", "showers", "snowfall", "shortwave_radiation",
          "wet_bulb_temperature_2m", "cape", "lifted_index"]

GEONAMES_CITY_ALIASES = {
    "Zaporizhzhia": "Zaporizhzhya",
    "Mykolaiv": "Mykolayiv",
}

weather_variables = [
    {"name": "temperature_2m", "translation": "Температура повітря (на висоті 2 метри)"},
    {"name": "apparent_temperature", "translation": "Відчувана температура («відчується як»)"},
    {"name": "precipitation", "translation": "Опади (сумарна кількість: дощ + зливи + сніг)"},
    {"name": "precipitation_probability", "translation": "Ймовірність опадів (у відсотках)"},
    {"name": "relative_humidity_2m", "translation": "Відносна вологість повітря (на висоті 2 метри)"},
    {"name": "dew_point_2m", "translation": "Точка роси (на висоті 2 метри)"},
    {"name": "rain", "translation": "Дощ (крупномасштабні, обложні дощі)"},
    {"name": "showers", "translation": "Зливи (короткочасні, інтенсивні дощі)"},
    {"name": "snowfall", "translation": "Снігопад (кількість снігу)"},
    {"name": "shortwave_radiation", "translation": "Короткохвильова сонячна радіація (загальна сонячна енергія, GHI)"},
    {"name": "wet_bulb_temperature_2m", "translation": "Температура вологого термометра (на висоті 2 метри)"},
    {"name": "cape", "translation": "CAPE (індекс конвективної доступної потенційної енергії — паливо для гроз)"},
    {"name": "lifted_index", "translation": "Індекс підйому (показник нестабільності атмосфери для прогнозування штормів)"}]



"apparent_temperature", "precipitation", "precipitation_probability", "relative_humidity_2m", "dew_point_2m", "rain", "showers","snowfall","shortwave_radiation", "wet_bulb_temperature_2m", "cape", "lifted_index"]
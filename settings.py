from pathlib import Path

BASE_DIR_CACHE = Path('cache')

CITY_CACHE = BASE_DIR_CACHE / 'city_name_cache'
FORECAST_CACHE = BASE_DIR_CACHE / 'forecast_weather_cache'

REQUEST_NAME_URL = "https://geocoding-api.open-meteo.com/v1/search"
REQUEST_WEATHER_FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

PARAMS = ["temperature_2m"]

GEONAMES_CITY_ALIASES = {
    "Zaporizhzhia": "Zaporizhzhya",
    "Mykolaiv": "Mykolayiv",
}
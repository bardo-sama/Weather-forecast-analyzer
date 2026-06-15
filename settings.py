from pathlib import Path

BASE_DIR_CACHE = Path('cache')

CITY_CACHE = BASE_DIR_CACHE / 'cache_city'

REQUEST_NAME_URL = "https://geocoding-api.open-meteo.com/v1/search"


GEONAMES_CITY_ALIASES = {
    "Zaporizhzhia": "Zaporizhzhya",
    "Mykolaiv": "Mykolayiv",
}
import requests
import requests_cache
from settings import CITY_CACHE, REQUEST_NAME_URL
from datetime import timedelta
from support_item.helpers import get_geonames
from api_clients.get_request_api import fetch_json

session_name = requests_cache.CachedSession(CITY_CACHE, expire_after=timedelta(hours=1))



def fetch_city(city_name, country_code, language='en'):
    """
    Searches for a city via the Open-Meteo Geocoding API
    and returns a list of found cities.
    -----------------------------------------------------
    Шукає місто через Open-Meteo Geocoding API.
    Повертає список знайдених міст.
    """

    city_name = city_name.strip()
    country_code = country_code.strip().upper()
    language = language.strip().lower()

    if country_code == 'UA':
        api_request_name = get_geonames(city_name)
    else:
        api_request_name = city_name

    params = {
        'name': api_request_name,
        'count': 2,
        'format': 'json',
        'countryCode': country_code,
        'language': language
    }

    result = fetch_json(session=session_name, url=REQUEST_NAME_URL, params=params)
    if result is None:
        return []

    return result.get('results', [])
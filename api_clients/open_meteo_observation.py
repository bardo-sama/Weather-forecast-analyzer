import requests_cache
from datetime import timedelta
from settings import OBSERVATION_CACHE, REQUEST_WEATHER_OBSERVATION_URL, PARAMS
from api_clients.get_request_api import fetch_json

session_observation = requests_cache.CachedSession(OBSERVATION_CACHE, expire_after=timedelta(hours=24))

def fetch_observation(city, start_date, end_date):

    params = {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": PARAMS,
    }

    result = fetch_json(session=session_observation, url=REQUEST_WEATHER_OBSERVATION_URL, params=params)

    return result
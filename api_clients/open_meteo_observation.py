import requests_cache
from datetime import timedelta
from settings import OBSERVATION_CACHE, REQUEST_WEATHER_OBSERVATION_URL, PARAMS
from api_clients.get_request_api import fetch_json
from support_item.forecasts_status import get_preparation_to_observation_requests

session_observation = requests_cache.CachedSession(OBSERVATION_CACHE, expire_after=timedelta(hours=24))

def fetch_observation(city):

    dates = get_preparation_to_observation_requests(city)

    if not dates:
        print("No available observation dates.")
        return False

    start_date = dates[0]
    end_date = dates[-1]

    params = {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": PARAMS,
        "models": "best_match"
    }

    result = fetch_json(session=session_observation, url=REQUEST_WEATHER_OBSERVATION_URL, params=params)

    if not result:
        return {}

    return {
        'source': 'open_meteo',
        'data': result
    }
import requests_cache
from datetime import timedelta
from settings import OBSERVATION_CACHE, REQUEST_WEATHER_OBSERVATION_URL, PARAMS
from api_clients.get_request_api import fetch_json
from support_item.helpers import is_observation_available

session_observation = requests_cache.CachedSession(OBSERVATION_CACHE, expire_after=timedelta(hours=24))

def fetch_observation(city, forecast):

    start_date = forecast.period_start
    end_date = forecast.period_end
    check_date = is_observation_available(forecast)
    if check_date is False:
        print("Uncorrected observations date.")
        return False

    params = {
        "latitude": city.latitude,
        "longitude": city.longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": PARAMS,
    }

    result = fetch_json(session=session_observation, url=REQUEST_WEATHER_OBSERVATION_URL, params=params)

    return result
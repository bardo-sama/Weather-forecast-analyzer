import requests_cache
from datetime import timedelta, datetime, timezone
from settings import FORECAST_CACHE, REQUEST_WEATHER_FORECAST_URL, PARAMS
from api_clients.get_request_api import fetch_json

session_forecast = requests_cache.CachedSession(FORECAST_CACHE, expire_after=timedelta(hours=1))

def fetch_forecast(city):
    # Параметри запиту
    params = {
        'latitude': city.latitude,
        'longitude': city.longitude,
        'hourly': PARAMS,
        "forecast_days": 2  # max = 16 days
    }
    # Час початку запиту
    requests_time = datetime.now(timezone.utc)
    # Запит
    result = fetch_json(session=session_forecast, url=REQUEST_WEATHER_FORECAST_URL, params=params)
    # Час завершення запиту
    received_time = datetime.now(timezone.utc)

    if not result:
        return {}

    return {
        'requested_time': requests_time.isoformat(),
        'received_time': received_time.isoformat(),
        'data': result
    }



from datetime import datetime, timedelta

def is_observation_available(forecast, delay_day=2):
    """Перевірка валідности запиту на фактичну погоду"""

    # Змінна з поточною датою
    today = datetime.now().date()
    # Змінна з датою доступу
    available_until = today - timedelta(days=delay_day)
    # Змінна з атрибутом класу Forecast
    target_date = datetime.strptime(forecast.target_date, "%Y-%m-%d").date()


    return target_date <= available_until

def get_forecasts_ready_for_observation(city):
    """Прогнози для яких доступні фактичні дані"""
    ready_forecasts = []

    for forecast in city.forecasts:
        if is_observation_available(forecast):
            ready_forecasts.append(forecast)

    return ready_forecasts

def get_pending_forecasts(city):
    """Прогнози в очікуванні"""
    pending = []

    for forecast in city.forecasts:
        if not is_observation_available(forecast):
            pending.append(forecast)
    return pending
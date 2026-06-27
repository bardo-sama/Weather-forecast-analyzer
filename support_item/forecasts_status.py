from datetime import datetime, timedelta
import pandas as pd


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
            current_date = {'collected_date': forecast.collected_date,
                            'target_date': forecast.target_date}
            ready_forecasts.append(current_date)


    return ready_forecasts

def get_pending_forecasts(city):
    """Прогнози в очікуванні"""
    pending = []

    for forecast in city.forecasts:
        if not is_observation_available(forecast):
            current_date = {'collected_date': forecast.collected_date,
                            'target_date': forecast.target_date}
            pending.append(current_date)

    df = pd.DataFrame(pending)
    df = df.drop(columns='collected_date')
    df = df.drop_duplicates(subset=['target_date'])
    df = df.sort_values(by='target_date')
    pending_date = df['target_date'].tolist()

    print(f'Pending period: {pending_date[0]} - {pending_date[-1]}')
    return pending_date

def get_preparation_to_observation_requests(city):
    """Підготовка дат для запиту"""

    ready = get_forecasts_ready_for_observation(city)
    if not ready:
        return []
    df = pd.DataFrame(ready)
    df = df.drop(columns='collected_date')
    df = df.drop_duplicates(subset=['target_date'])
    df = df.sort_values(by='target_date')

    return df['target_date'].tolist()

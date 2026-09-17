import pandas as pd
from support_item.others_items import pretty_date

# Перетворюємо відповідь API з прогнозом у DataFrame.
def parse_forecast(forecast, city):

    # Без коректного міста прогноз немає до чого прив'язати.
    if not city or city is None:
        return False

    # Погодинні значення та їх одиниці вимірювання приходять окремими словниками.
    weather = forecast.get('data', {}).get('hourly', None)
    hourly_units = forecast.get('data', {}).get('hourly_units', {})
    source = forecast.get('source')

    if weather is None:
        return False

    # Зберігаємо дату отримання прогнозу та створюємо робочий DataFrame.
    request_time = pretty_date(forecast, 'requested_time')
    forecast_df = pd.DataFrame(weather)

    # Одиниці не дублюємо в кожному рядку, а тримаємо в метаданих DataFrame.
    forecast_df.attrs['units'] = hourly_units

    # Додаємо службові дані міста та джерела прогнозу.
    forecast_df['name'] = city.name
    forecast_df['source'] = source
    forecast_df['latitude'] = city.latitude
    forecast_df['longitude'] = city.longitude


    # Готуємо окремі колонки дати й години для подальшого поділу прогнозу по днях.
    forecast_df['datetime'] = pd.to_datetime(forecast_df['time'])
    forecast_df['date'] = forecast_df['datetime'].dt.strftime("%Y-%m-%d")
    forecast_df['hour'] = forecast_df['datetime'].dt.hour
    forecast_df['datetime'] = forecast_df['datetime'].dt.strftime("%Y-%m-%dT%H:%M")
    forecast_df['collected_date'] = request_time

    # Службові колонки ставимо попереду, погодні метрики залишаємо після них.
    front_columns = ['name', 'source', 'latitude', 'longitude', 'collected_date',
                     'datetime', 'date', 'hour']

    other_columns = [column for column in forecast_df.columns
                     if column not in front_columns]

    forecast_df = forecast_df[front_columns + other_columns]

    # Початкова колонка time більше не потрібна після створення datetime/date/hour.
    forecast_df = forecast_df.drop(columns=['time'])

    return forecast_df

# Розділяємо загальний прогноз на окремий DataFrame для кожної дати.
def split_forecast_by_date(forecast_df):

    forecasts = []
    units = forecast_df.attrs.get('units', {})

    for target_date, day_df in forecast_df.groupby('date'):
        # groupby створює окремі DataFrame, тому явно переносимо одиниці вимірювання.
        day_df.attrs['units'] = units
        forecasts.append(day_df)

    return forecasts






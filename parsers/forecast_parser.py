import pandas as pd
from support_item.helpers import pretty_date

def parse_forecast(forecast, city):

    if not city or city is None:
        return False

    weather = forecast.get('data', {}).get('hourly', None)
    source = forecast.get('source')

    if weather is None:
        return False

    request_time = pretty_date(forecast, 'requested_time')
    forecast_df = pd.DataFrame(weather)

    forecast_df['name'] = city.name
    forecast_df['source'] = source
    forecast_df['latitude'] = city.latitude
    forecast_df['longitude'] = city.longitude


    forecast_df['datetime'] = pd.to_datetime(forecast_df['time'])
    forecast_df['date'] = forecast_df['datetime'].dt.strftime("%Y-%m-%d")
    forecast_df['hour'] = forecast_df['datetime'].dt.hour
    forecast_df['datetime'] = forecast_df['datetime'].dt.strftime("%Y-%m-%dT%H:%M")
    forecast_df['collected_date'] = request_time

    front_columns = ['name', 'source', 'latitude', 'longitude', 'collected_date',
                     'datetime', 'date', 'hour']

    other_columns = [column for column in forecast_df.columns
                     if column not in front_columns]

    forecast_df = forecast_df[front_columns + other_columns]

    forecast_df = forecast_df.drop(columns=['time'])

    return forecast_df

def split_forecast_by_date(forecast_df):

    forecasts = []

    for target_date, day_df in forecast_df.groupby('date'):
        forecasts.append(day_df)

    return forecasts








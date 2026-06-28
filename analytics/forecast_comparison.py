from models.city import City
import pandas as pd

def get_one_data_set(city):

    raw_weather_data = []

    forecast = city.forecasts[0]
    observation = city.observations[0]

    if forecast.target_date != observation.target_date:
        print('Different target date.')
        return False

    raw_weather_data.append(forecast)
    raw_weather_data.append(observation)

    return raw_weather_data


def compare_forecast_with_observation(city):

    weather_data = get_one_data_set(city)

    if weather_data is False:
        print("List is empty.")
        return pd.DataFrame()

    forecast = weather_data[0]
    observation = weather_data[-1]

    forecast_df = forecast.weather_data
    observation_df = observation.weather_data

    forecast_df.rename(columns={'temperature_2m': 'forecast_temp'}, inplace=True)
    observation_df.rename(columns={'temperature_2m':'observ_temp'}, inplace=True)


    compare_df = pd.merge(
        forecast_df,
        observation_df[['datetime', 'observ_temp']],
        on='datetime',
        how='left'
    )

    return compare_df
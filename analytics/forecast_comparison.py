import pandas as pd

def get_matched_pair(city):

    matched_pair_list = []

    for observation in city.observations:
        for forecast in city.forecasts:
            if observation.target_date == forecast.target_date:
                current_data = (forecast, observation)
                matched_pair_list.append(current_data)


    return matched_pair_list


def compare_forecast_with_observation(forecast, observation):




    forecast = weather_data[0]
    observation = weather_data[-1]

    forecast_df = forecast.weather_data.copy()
    observation_df = observation.weather_data.copy()

    forecast_df = forecast_df.rename(columns={'temperature_2m': 'forecast_temp'}, inplace=False)
    observation_df = observation_df.rename(columns={'temperature_2m':'observed_temp'}, inplace=False)

    compare_df = pd.merge(
        forecast_df,
        observation_df[['datetime', 'observed_temp']],
        on='datetime',
        how='inner'
    )
    compare_df['city'] = forecast.city_name
    compare_df['source'] = forecast.source
    compare_df['collected_date'] = forecast.collected_date
    compare_df['target_date'] = forecast.target_date
    compare_df['lead_days'] = forecast.lead_days

    front_columns = ['city', 'source', 'collected_date', 'target_date', 'lead_days']

    others_columns = [column for column in compare_df.columns
                      if column not in front_columns]

    compare_df = compare_df[front_columns + others_columns]

    compare_df['error'] = compare_df['forecast_temp'] - compare_df['observed_temp']

    compare_df['abs_error'] = compare_df['error'].abs()


    return compare_df
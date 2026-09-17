import pandas as pd


def get_matched_pair(city):
    """Збираємо список пар по target_date"""

    matched_pair_list = []

    # Цикл через фактичні дані погоди
    for observation in city.observations:
        for forecast in city.forecasts:
            # Перебір по відповідній даті
            if observation.target_date == forecast.target_date:
                # Відсіємо все що менше нуля
                if forecast.lead_days >= 0:
                    current_data = (forecast, observation)
                    matched_pair_list.append(current_data)


    return matched_pair_list


def compare_forecast_with_observation(pair):
    """
        Об'єднання однієї пари у дата-фрейм.
    ------------------------------------------
        Створення стовпців 'error' та 'abs_error'.
    '"""

    forecast, observation = pair
    forecast_df = forecast.weather_data.copy()
    observation_df = observation.weather_data.copy()

    forecast_df = forecast_df.rename(columns={'temperature_2m': 'forecast_temp'})
    observation_df = observation_df.rename(columns={'temperature_2m':'observed_temp'})

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
    compare_df['error'] = (compare_df['forecast_temp'] - compare_df['observed_temp']).round(2)
    compare_df['abs_error'] = compare_df['error'].abs().round(2)

    return compare_df

def compare_all_matched_pairs(city):
    """Збираємо все пари у дата-фрейм."""

    current_df_list = [ ]
    pairs = get_matched_pair(city)

    # Повертаємо пустий ДТ, якщо get_matched_pair не впорався.
    if not pairs:
        print('List is empty')
        return pd.DataFrame()

    for pair in pairs:
        current = compare_forecast_with_observation(pair)
        current_df_list.append(current)

    result = pd.concat(current_df_list, ignore_index=True)
    return result

def get_lead_days_summary(compare_df):

    if compare_df.empty:
        print('DataFrame is empty.')
        return pd.DataFrame()

    current_list = []

    max_lead_days = compare_df['lead_days'].max()
    max_lead_range = range(0, max_lead_days + 1)

    for  value in max_lead_range:

         if (compare_df['lead_days'] == value).any():
             current_df = compare_df[compare_df['lead_days'] == value]

             if not current_df.empty:
                current_dict = {
                    'city': current_df.iloc[0]['city'],
                    'source': current_df.iloc[0]['source'],
                    'lead_days': value,
                    'mean_error':  current_df['error'].mean().round(2),
                    'mean_abs_error': current_df['abs_error'].mean().round(2),
                    'max_abs_error': current_df['abs_error'].max().round(2),
                    'rows_compared': len(current_df)
                }
                current_list.append(current_dict)

    result = pd.DataFrame(current_list)
    return result




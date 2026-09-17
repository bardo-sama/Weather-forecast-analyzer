import pandas as pd

# Перетворюємо відповідь API з фактичними погодними даними у DataFrame.
def parse_observation(observation, city):

    # Без коректного міста фактичні дані немає до чого прив'язати.
    if not city or city is None:
        return False

    # Погодинні значення та їх одиниці вимірювання приходять окремими словниками.
    weather = observation.get('data', {}).get('hourly', None)
    hourly_units = observation.get('data', {}).get('hourly_units', {})
    source = observation.get('source')

    if weather is None:
        return False

    # Створюємо робочий DataFrame з погодинних значень.
    observation_df = pd.DataFrame(weather)

    # Одиниці не дублюємо в кожному рядку, а тримаємо в метаданих DataFrame.
    observation_df.attrs['units'] = hourly_units

    # Додаємо службові дані міста та джерела фактичних даних.
    observation_df['name'] = city.name
    observation_df['source'] = source
    observation_df['latitude'] = city.latitude
    observation_df['longitude'] = city.longitude

    # Готуємо окремі колонки дати й години для подальшого поділу по днях.
    observation_df['datetime'] = pd.to_datetime(observation_df['time'])
    observation_df['date'] = observation_df['datetime'].dt.strftime("%Y-%m-%d")
    observation_df['hour'] = observation_df['datetime'].dt.hour
    observation_df['datetime'] = observation_df['datetime'].dt.strftime("%Y-%m-%dT%H:%M")

    # Службові колонки ставимо попереду, погодні метрики залишаємо після них.
    front_columns = ['name', 'source', 'latitude', 'longitude', 'datetime', 'date', 'hour']

    other_columns = [column for column in observation_df.columns
                     if column not in front_columns]

    observation_df = observation_df[front_columns + other_columns]
    observation_df = observation_df.drop(columns=['time'])

    return observation_df

# Розділяємо загальні фактичні дані на окремий DataFrame для кожної дати.
def split_observation_by_date(observation_df):

    observations = []
    units = observation_df.attrs.get('units', {})

    for target_date, day_df in observation_df.groupby('date'):
        # groupby створює окремі DataFrame, тому явно переносимо одиниці вимірювання.
        day_df.attrs['units'] = units
        observations.append(day_df)

    return observations

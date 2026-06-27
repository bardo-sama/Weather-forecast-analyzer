import pandas as pd

def parse_observation(observation, city):

    if not city or city is None:
        return False

    weather = observation.get('data', {}).get('hourly', None)
    source = observation.get('source')

    if weather is None:
        return False

    observation_df = pd.DataFrame(weather)

    observation_df['name'] = city.name
    observation_df['source'] = source
    observation_df['latitude'] = city.latitude
    observation_df['longitude'] = city.longitude

    observation_df['datetime'] = pd.to_datetime(observation_df['time'])
    observation_df['date'] = observation_df['datetime'].dt.strftime("%Y-%m-%d")
    observation_df['hour'] = observation_df['datetime'].dt.hour
    observation_df['datetime'] = observation_df['datetime'].dt.strftime("%Y-%m-%dT%H:%M")

    front_columns = ['name', 'source', 'latitude', 'longitude', 'datetime', 'date', 'hour']

    other_columns = [column for column in observation_df.columns
                     if column not in front_columns]

    observation_df = observation_df[front_columns + other_columns]
    observation_df = observation_df.drop(columns=['time'])

    return observation_df

def split_observation_by_date(observation_df):

    observations = []

    for target_date, day_df in observation_df.groupby('date'):
        observations.append(day_df)

    return observations
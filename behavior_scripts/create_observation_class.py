from storage.load_json import load_city_forecast_history
from support_item.forecasts_status import get_preparation_to_observation_requests, get_pending_forecasts
from api_clients.open_meteo_observation import fetch_observation
from parsers.observation_parser import parse_observation, split_observation_by_date
from support_item.helpers import add_observation_obj

def create_observation_class(city):

    ready = get_preparation_to_observation_requests(city)

    if not ready:
        pending_dates = get_pending_forecasts(city)
        print('Pending dates.')
        return pending_dates

    print(f'Available period: {ready[0]} - {ready[-1]}')

    observation = fetch_observation(city)

    observation = parse_observation(observation, city)

    if observation is False:
        print("Observation data is empty.")
        return city

    observations = split_observation_by_date(observation)

    for observation in observations:
        observation_obj = add_observation_obj(observation)
        city.add_observation(observation_obj)

    return city






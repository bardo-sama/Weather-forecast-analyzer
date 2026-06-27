from scenarios.behavior_scripts import create_city_class
from storage.load_json import load_json, load_city_forecast_history
from support_item.forecasts_status import get_forecasts_ready_for_observation, get_preparation_to_observation_requests


def test_forecasts_default_obj():
    city_list = ['zaporizhzhia', 'dnipro', 'kyiv', 'lviv']
    cities = []
    for city in city_list:
        current_data = create_city_class(city, 'ua')
        cities.append(current_data)

if __name__ == '__main__':
    pass
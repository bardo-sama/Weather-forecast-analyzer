from scenarios.behavior_scripts import create_city_class
from storage.load_json import load_json
from models.city import City


def test_forecasts_default_obj():
    city_list = ['zaporizhzhia', 'dnipro', 'kyiv', 'lviv']
    cities = []
    for city in city_list:
        current_data = create_city_class(city, 'ua')
        cities.append(current_data)

if __name__ == '__main__':

    filename = "data/forecasts/zaporizhzhia/open_meteo/2026-06-23.json"

    data = load_json(filename)

    city = City.from_dict(data)

    city.show_city()

    for forecast in city.forecasts:
        forecast.show_summary()

from models.city import City
from models.forecast import Forecast
from parsers.forecast_parser import parse_forecast
from parsers.data_parse import parse_datetime

def get_geonames(city_name):
    """
    Validate the city name.
    ----------------------------------
    Перевірка коректності назви міста.
    """
    if city_name == 'Zaporizhzhia':
        return 'Zaporizhzhya'
    elif city_name == 'Mykolayiv':
        return 'Mykolaiv'

    return city_name.strip().upper()

def return_right_name(name):

    if name == 'Zaporizhzhya':
        name = 'Zaporizhzhia'
        return name

    elif name == 'Mykolayiv':
        name = 'Mykolaiv'
        return name

    return name.strip().upper()


def add_city_obj(city_data):

    return City(city_data.get('name'), city_data.get('latitude'), city_data.get('longitude'),
                city_data.get('country_code'), city_data.get('timezone'))

def add_forecast_obj(data, city):

    datetime = parse_datetime(data)

    forecast = parse_forecast(data, city)

    forecast_obj = Forecast(forecast.loc(0, 'name'))
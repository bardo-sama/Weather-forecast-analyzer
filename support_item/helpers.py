from settings import GEONAMES_CITY_ALIASES
from models.city import City

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

    return city_name

def return_right_name(name):

    if name == 'Zaporizhzhya':
        name = 'Zaporizhzhia'
        return name

    elif name == 'Mykolayiv':
        name = 'Mykolaiv'
        return name

    return name


def add_city_obj(city_data):

    return City(city_data.get('name'), city_data.get('latitude'), city_data.get('longitude'),
                city_data.get('country_code'), city_data.get('timezone'))
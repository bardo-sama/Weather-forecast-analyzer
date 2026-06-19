from datetime import datetime
from models.city import City
from models.forecast import Forecast



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

    return city_name.strip().title()

def return_right_name(name):

    if name == 'Zaporizhzhya':
        name = 'Zaporizhzhia'
        return name

    elif name == 'Mykolayiv':
        name = 'Mykolaiv'
        return name

    return name.strip().title()

def pretty_date(date):

    raw_date = date.get('requested_time', None)
    if raw_date is None:
        return False
    dt = datetime.fromisoformat(raw_date)

    dt_clean = dt.strftime("%Y-%m-%d")
    return dt_clean



def add_city_obj(city_data):

    return City(city_data.get('name'), city_data.get('latitude'), city_data.get('longitude'),
                city_data.get('country_code'), city_data.get('timezone'))

def add_forecast_obj(data):

    return Forecast(data.iloc[0]['name'], 'open_meteo', data.iloc[0]['latitude'],
                    data.iloc[0]['longitude'], data.iloc[0]['request_t'],
                    data.iloc[0]['datetime'], data.iloc[-1]['datetime'], data[['date', 'hour', 'temperature_2m']])




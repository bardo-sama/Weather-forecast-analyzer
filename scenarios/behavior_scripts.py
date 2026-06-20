from api_clients.open_meteo_city_name import fetch_city
from api_clients.open_meteo_forecast import fetch_forecast
from parsers.city_parser import city_parser
from parsers.forecast_parser import parse_forecast
from support_item.helpers import add_city_obj, add_forecast_obj
from storage.save_to_json import save_city_to_json

def create_city_class(city_name, country_code):

    # Робимо запит міста
    request = fetch_city(city_name, country_code)
    # Чистимо дані міста
    city = city_parser(request)
    # Створ. об'єкт класу - City
    city = add_city_obj(city)
    # Робимо запит на прогноз погоди
    forecast = fetch_forecast(city)
    # Чистимо отримані дані
    forecast = parse_forecast(forecast, city)
    # Створ. об'єкт класу - Forecast
    forecast_data = add_forecast_obj(forecast)
    # Додаємо прогноз до міста
    city.add_forecast(forecast_data)

    # Вивід результату
    city.show_city()
    city_forecast = [forecast.show_summary() for forecast in city.forecasts]

    return city
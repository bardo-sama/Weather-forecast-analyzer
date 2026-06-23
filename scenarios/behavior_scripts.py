from api_clients.open_meteo_city_name import fetch_city
from api_clients.open_meteo_forecast import fetch_forecast
from parsers.city_parser import city_parser
from parsers.forecast_parser import parse_forecast, split_forecast_by_date
from support_item.helpers import add_city_obj, add_forecast_obj
from storage.save_to_json import save_city_to_json

def create_city_class(city_name, country_code):

    # Робимо запит міста
    request = fetch_city(city_name, country_code)

    # Чистимо дані міста
    city = city_parser(request)

    if city is False:
        print(f'City not found: {city} ({country_code})')
        return None

    # Створ. об'єкт класу - City
    city = add_city_obj(city)

    # Робимо запит на прогноз погоди
    forecast = fetch_forecast(city)

    # Чистимо отримані дані
    forecast = parse_forecast(forecast, city)

    if forecast is False:
        print(f"Forecast data is empty")
        return city

    forecasts = split_forecast_by_date(forecast)
    forecasts_obj = []
    # Створ. об'єкт класу - Forecast
    for forecast in forecasts:
        current_obj = add_forecast_obj(forecast)
        forecasts_obj.append(current_obj)
    # Додаємо прогноз до міста
    city.add_forecast(forecasts_obj)

    # Вивід результату
    city.show_city()
    city_forecasts = city.forecasts

    for forecast in city_forecasts:
        forecast.show_summary()

    return city
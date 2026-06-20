from api_clients.open_meteo_city_name import fetch_city
from api_clients.open_meteo_forecast import fetch_forecast
from parsers.city_parser import city_parser
from parsers.forecast_parser import parse_forecast
from support_item.helpers import add_city_obj, add_forecast_obj
from storage.save_to_json import save_city_to_json

def test_main():

    # Робимо запит міста
    zp_test_request = fetch_city('zaporizhzhia', 'ua')
    # Чистимо дані міста
    clean_city_name = city_parser(zp_test_request)
    # Створ. об'єкт класу - City
    zaporizhzhia = add_city_obj(clean_city_name)
    # Робимо запит на прогноз погоди
    zaporizhzhia_forecast = fetch_forecast(zaporizhzhia)
    # Чистимо отримані дані
    test_parse_forecast = parse_forecast(zaporizhzhia_forecast, zaporizhzhia)
    # Створ. об'єкт класу - Forecast

    if test_parse_forecast is not False and not test_parse_forecast.empty:

        zaporizhzhia_forecast_data = add_forecast_obj(test_parse_forecast)
        zaporizhzhia.add_forecast(zaporizhzhia_forecast_data)

    zaporizhzhia.show_city()
    zp_forecast = zaporizhzhia.forecasts[0]
    zp_forecast.show_summary()


if __name__ == '__main__':
    test_main()


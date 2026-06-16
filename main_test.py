from api_clients.open_meteo_city_name import fetch_city
from api_clients.open_meteo_forecast import fetch_forecast
from parsers.city_parser import city_parser
from support_item.helpers import add_city_obj

zp_test_request = fetch_city('zaporizhzhia', 'ua')
clean_city_name = city_parser(zp_test_request)

zaporizhzhia = add_city_obj(clean_city_name)

lviv_test_request = fetch_city('lviv', 'ua')

clean_city_lviv = city_parser(lviv_test_request)

lviv = add_city_obj(clean_city_lviv)

zaporizhzhia.show_city()
lviv.show_city()

zaporizhzhia_forecast = fetch_forecast(zaporizhzhia)

print(type(zaporizhzhia_forecast))
for key, value in zaporizhzhia_forecast.items():
    print(f'{key}: {value}')
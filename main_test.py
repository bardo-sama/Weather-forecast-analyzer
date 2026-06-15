from api_clients.open_meteo_geo import fetch_city
from parsers.city_parser import city_parser
from models.city import City
from support_item.helpers import add_city_obj

zp_test_request = fetch_city('zaporizhzhia', 'ua')
clean_city_name = city_parser(zp_test_request)

zaporizhzhia = add_city_obj(clean_city_name)

lviv_test_request = fetch_city('lviv', 'ua')

clean_city_lviv = city_parser(lviv_test_request)

lviv = add_city_obj(clean_city_lviv)

zaporizhzhia.show_city()
lviv.show_city()


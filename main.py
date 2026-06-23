from scenarios.behavior_scripts import create_city_class
from api_clients.open_meteo_observation import fetch_observation

if __name__ == '__main__':
    zp = create_city_class('zaporizhzhia', 'ua')


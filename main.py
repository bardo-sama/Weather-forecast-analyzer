from scenarios.behavior_scripts import create_city_class
from api_clients.open_meteo_observation import fetch_observation

if __name__ == '__main__':
    lviv = create_city_class('lviv', 'ua')
    lviv_weather = lviv.forecasts[0]

    observation_lviv = fetch_observation(lviv, lviv_weather)

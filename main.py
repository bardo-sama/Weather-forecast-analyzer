from behavior_scripts.create_city_class import create_city_class
from behavior_scripts.create_observation_class import create_observation_class
from storage.load_json import load_json, load_city_forecast_history
from support_item.forecasts_status import get_pending_forecasts
from analytics.forecast_comparison import get_matched_pair, compare_forecast_with_observation



def test_forecasts_default_obj():
    city_list = ['zaporizhzhia', 'dnipro', 'kyiv', 'lviv']
    cities = []
    for city in city_list:
        current_data = create_city_class(city, 'ua')
        cities.append(current_data)

if __name__ == '__main__':
    test_forecasts_default_obj()

    zp = load_city_forecast_history('zaporizhzhia', 'open_meteo')
    dnipro = load_city_forecast_history('dnipro', 'open_meteo')
    kyiv = load_city_forecast_history('kyiv', 'open_meteo')
    lviv = load_city_forecast_history('lviv', 'open_meteo')

    zp_city = create_observation_class(zp)
    dnipro_city = create_observation_class(dnipro)
    kyiv_city = create_observation_class(kyiv)
    lviv_city = create_observation_class(lviv)

    test = get_matched_pair(zp_city)
    test_pair = test[0]
    compare_df = compare_forecast_with_observation(test_pair)

    print(compare_df[['datetime', 'forecast_temp', 'observed_temp', 'error', 'abs_error']])

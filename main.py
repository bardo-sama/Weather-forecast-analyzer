

from behavior_scripts.create_city_class import create_city_class
from behavior_scripts.create_observation_class import create_observation_class
from storage.load_json import load_json, load_city_forecast_history
from storage.save_comparison_to_csv import comparison_to_csv
from support_item.forecasts_status import get_pending_forecasts
from analytics.forecast_comparison import compare_all_matched_pairs, get_lead_days_summary



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

    zp_test = compare_all_matched_pairs(zp_city)
    dnipro_test = compare_all_matched_pairs(dnipro_city)
    kyiv_test = compare_all_matched_pairs(kyiv_city)
    lviv_test = compare_all_matched_pairs(lviv_city)

    zp_test_1 = get_lead_days_summary(zp_test)
    dnipro_test_1 = get_lead_days_summary(dnipro_test)
    kyiv_test_1 = get_lead_days_summary(kyiv_test)
    lviv_test_1 = get_lead_days_summary(lviv_test)
    test_data_list = [zp_test, zp_test_1, dnipro_test, dnipro_test_1,
                      kyiv_test, kyiv_test_1, lviv_test, lviv_test_1]

    save_all_compare = [comparison_to_csv(df) for df in test_data_list]





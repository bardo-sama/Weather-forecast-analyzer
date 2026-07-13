from datetime import datetime
from models.city import City
from models.forecast import Forecast
from models.observation import Observation
from settings import BASE_DIR_DATA

from pathlib import Path

# Нормалізуємо назву міста під формат, який очікує Geonames/Open-Meteo.
def get_geonames(city_name):
    """
    Validate the city name.
    ----------------------------------
    Перевірка коректності назви міста.
    """
    city_name = city_name.strip().title()

    if city_name == 'Zaporizhzhia':
        return 'Zaporizhzhya'
    elif city_name == 'Mykolayiv':
        return 'Mykolaiv'

    return city_name.strip().title()

# Повертаємо назву міста до внутрішнього формату проєкту.
def return_right_name(name):

    if name == 'Zaporizhzhya':
        name = 'Zaporizhzhia'
        return name

    elif name == 'Mykolayiv':
        name = 'Mykolaiv'
        return name
    else:
        return name.strip().title()

# Перетворюємо ISO-дату з відповіді API у формат YYYY-MM-DD.
def pretty_date(date, key):

    raw_date = date.get(key, None)
    if raw_date is None:
        return False
    dt = datetime.fromisoformat(raw_date)

    dt_clean = dt.strftime("%Y-%m-%d")
    return dt_clean

# Створюємо об'єкт City з уже очищених даних міста.
def add_city_obj(city_data):

    return City(
        city_data.get('name'),
        city_data.get('latitude'),
        city_data.get('longitude'),
        city_data.get('country_code'),
        city_data.get('timezone'))


# Створюємо Forecast для одного дня та передаємо йому погодні дані разом з units.
def add_forecast_obj(data):

    return Forecast(
        data.iloc[0]['name'],
        data.iloc[0]['source'],
        data.iloc[0]['latitude'],
        data.iloc[0]['longitude'],
        data.iloc[0]['collected_date'],
        data.iloc[0]['date'],
        data[["datetime", "date", "hour", "temperature_2m",
              "apparent_temperature", "precipitation",
              "precipitation_probability", "relative_humidity_2m",
              "dew_point_2m", "rain",  "showers", "snowfall",
              "shortwave_radiation", "wet_bulb_temperature_2m",
              "cape", "lifted_index",]],
        data.attrs.get('units', {}))

# Створюємо Observation для одного дня та передаємо йому погодні дані разом з units.
def add_observation_obj(data):
    """Створення класу з факт. погодними даними """

    return Observation(
        data.iloc[0]["name"],
        data.iloc[0]["source"],
        data.iloc[0]["latitude"],
        data.iloc[0]["longitude"],
        data.iloc[0]["date"],
        data[["datetime", "date", "hour", "temperature_2m",
              "apparent_temperature", "precipitation",
              "precipitation_probability", "relative_humidity_2m",
              "dew_point_2m", "rain", "showers", "snowfall",
              "shortwave_radiation", "wet_bulb_temperature_2m",
              "cape", "lifted_index",]],
        data.attrs.get('units', {}))

# Формуємо шлях для JSON з історією прогнозів міста.
def name_for_json(data):
    """Створення шаблону директорії"""

    city_name = data['name']
    source = data['forecasts'][0]['source']
    collected_date = data['forecasts'][0]['collected_date']

    return BASE_DIR_DATA / "forecasts" / city_name / source / f"{collected_date}.json"

# Формуємо шлях для CSV з погодинним порівнянням прогнозу та фактичних даних.
def name_for_comparison_df(df):

    city_name = df['city'].iloc[0]
    source = df['source'].iloc[0]
    filename = BASE_DIR_DATA / 'comparison' / city_name / source / f"comparison_{datetime.now().date()}.csv"

    return filename

# Формуємо шлях для CSV зі зведенням похибки за lead_days.
def name_for_lead_days_summary(df):

    city_name = df['city'].iloc[0]
    source = df['source'].iloc[0]
    filename = BASE_DIR_DATA / 'comparison' / city_name / source / f"lead_days_summary_{datetime.now().date()}.csv"


    return filename

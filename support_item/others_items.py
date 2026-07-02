from datetime import datetime
from models.city import City
from models.forecast import Forecast
from models.observation import Observation
from settings import BASE_DIR_DATA

from pathlib import Path

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

def return_right_name(name):

    if name == 'Zaporizhzhya':
        name = 'Zaporizhzhia'
        return name

    elif name == 'Mykolayiv':
        name = 'Mykolaiv'
        return name
    else:
        return name.strip().title()

def pretty_date(date, key):

    raw_date = date.get(key, None)
    if raw_date is None:
        return False
    dt = datetime.fromisoformat(raw_date)

    dt_clean = dt.strftime("%Y-%m-%d")
    return dt_clean

def add_city_obj(city_data):

    return City(
        city_data.get('name'),
        city_data.get('latitude'),
        city_data.get('longitude'),
        city_data.get('country_code'),
        city_data.get('timezone'))


def add_forecast_obj(data):

    return Forecast(
        data.iloc[0]['name'],
        data.iloc[0]['source'],
        data.iloc[0]['latitude'],
        data.iloc[0]['longitude'],
        data.iloc[0]['collected_date'],
        data.iloc[0]['date'],
        data[['datetime', 'date', 'hour', 'temperature_2m']])

def add_observation_obj(data):
    """Створення класу з факт. погодними даними """

    return Observation(
        data.iloc[0]["name"],
        data.iloc[0]["source"],
        data.iloc[0]["latitude"],
        data.iloc[0]["longitude"],
        data.iloc[0]["date"],
        data[["datetime", "date", "hour", "temperature_2m"]]
    )

def name_for_json(data):
    """Створення шаблону директорії"""

    city_name = data['name']
    source = data['forecasts'][0]['source']
    collected_date = data['forecasts'][0]['collected_date']

    return BASE_DIR_DATA / "forecasts" / city_name / source / f"{collected_date}.json"

def name_for_comparison_df(df):

    city_name = df['city'].iloc[0]
    source = df['source'].iloc[0]
    filename = BASE_DIR_DATA / 'comparison' / city_name / source / f"lead_days_summary_{datetime.now().date()}.csv"
    filename.parent.mkdir(parents=True, exist_ok=True)
    return BASE_DIR_DATA / 'comparison' / city_name / source / f"comparison_{datetime.now().date()}.csv"

def name_for_lead_days_summary(df):

    city_name = df['city'].iloc[0]
    source = df['source'].iloc[0]
    filename = BASE_DIR_DATA / 'comparison' / city_name / source / f"lead_days_summary_{datetime.now().date()}.csv"
    filename.parent.mkdir(parents=True, exist_ok=True)

    return filename



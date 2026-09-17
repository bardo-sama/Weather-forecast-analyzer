from datetime import datetime
import pandas as pd

# Один об'єкт Forecast зберігає прогноз для конкретної target_date.
class Forecast:
    def __init__(self, city_name, source, latitude, longitude, collected_date, target_date, weather_data, units):
        self.city_name = city_name
        self.source = source
        self.latitude = latitude
        self.longitude = longitude
        self.collected_date = collected_date
        self.target_date = target_date
        self.weather_data = weather_data
        self.units = units

    def __repr__(self):
        return f'Class: Forecast, collected date: {self.collected_date}, target date: {self.target_date}'

    # Короткий текстовий опис прогнозу для ручної перевірки.
    def show_summary(self):
        print('-' * 21)
        print(f'Джерело: {self.source}')
        print(f'Дата збору даних: {self.collected_date}')
        print(f'Прогноз за датою: {self.target_date}')
        print('-' * 21)

    @property
    def lead_days(self):
        # Різниця між датою прогнозу та датою його отримання.
        collected = datetime.strptime(self.collected_date, "%Y-%m-%d").date()
        target = datetime.strptime(self.target_date, "%Y-%m-%d").date()

        return (target - collected).days

    # Перетворюємо об'єкт у словник для подальшого збереження в JSON.
    def to_dict(self):
        obj_datafile = {
            'city_name': self.city_name,
            'source': self.source,
            "coordinates": {
                "latitude": self.latitude,
                "longitude": self.longitude,
            },
            'collected_date': self.collected_date,
            'target_date': self.target_date,
            'lead_days': self.lead_days,
            'units': self.units,
            'weather_data': self.weather_data.to_dict('records')
        }
        return obj_datafile

    # Відновлюємо Forecast зі словника, завантаженого з JSON.
    @classmethod
    def from_dict(cls, data):

        if not isinstance(data, dict):
            return None

        coordinates = data.get('coordinates', {})

        # Погодні записи з JSON повертаємо назад у DataFrame.
        weather_data = pd.DataFrame(data.get('weather_data', []))

        return cls(
            city_name=data.get('city_name'),
            source=data.get('source'),
            latitude=coordinates.get('latitude'),
            longitude=coordinates.get('longitude'),
            collected_date=data.get('collected_date'),
            target_date=data.get('target_date'),
            weather_data=weather_data,
            units=data.get('units', {})
        )

import pandas as pd

# Один об'єкт Observation зберігає фактичні погодні дані для конкретної target_date.
class Observation:
    def __init__(self, city_name, source, latitude, longitude, target_date, weather_data, units):
        self.city_name = city_name
        self.source = source
        self.latitude = latitude
        self.longitude = longitude
        self.target_date = target_date
        self.weather_data = weather_data
        self.units = units

    def __repr__(self):
        return f"Class: Observation, target date: {self.target_date}"

    # Короткий текстовий опис фактичних погодних даних для ручної перевірки.
    def show_summary(self):
            print('-' * 21)
            print(f'Джерело: {self.source}')
            print(f'Дата: {self.target_date}')
            print('-' * 21)

    # Перетворюємо об'єкт у словник для подальшого збереження в JSON.
    def to_dict(self):
        return {
            'city_name': self.city_name,
            'source': self.source,
            'coordinates':{
                'latitude': self.latitude,
                'longitude': self.longitude
                },
            'target_date': self.target_date,
            'units': self.units,
            'weather_data': self.weather_data.to_dict('records')
        }

    # Відновлюємо Observation зі словника, завантаженого з JSON.
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
            target_date=data.get('target_date'),
            weather_data=weather_data,
            units=data.get('units', {}))

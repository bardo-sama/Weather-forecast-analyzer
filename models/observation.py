import pandas as pd

class Observation:
    def __init__(self, city_name, source, latitude, longitude, target_date, weather_data):
        self.city_name = city_name
        self.source = source
        self.latitude = latitude
        self.longitude = longitude
        self.target_date = target_date
        self.weather_data = weather_data

    def show_summary(self):
            print('-' * 21)
            print(f'Джерело: {self.source}')
            print(f'Дата: {self.target_date}')
            print('-' * 21)

    def to_dict(self):
        return {
            'city_name': self.city_name,
            'source': self.source,
            'coordinates':{
                'latitude': self.latitude,
                'longitude': self.longitude
                },
            'target_date': self.target_date,
            'weather_data': self.weather_data.to_dict('records')
        }

    @classmethod
    def from_dict(cls, data):

        if not isinstance(data, dict):
            return None

        coordinates = data.get('coordinates', {})

        weather_data = pd.DataFrame(data.get('weather_data', []))

        return cls(
            city_name=data.get('city_name'),
            source=data.get('source'),
            latitude=coordinates.get('latitude'),
            longitude=coordinates.get('longitude'),
            target_date=data.get('target_date'),
            weather_data=weather_data)
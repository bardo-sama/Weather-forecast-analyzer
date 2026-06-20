class Observation:
    def __init__(self, city_name, source, latitude, longitude, observation_from, observation_to, weather_data):
        self.city_name = city_name
        self.source = source
        self.latitude = latitude
        self.longitude = longitude
        self.observation_from = observation_from
        self.observation_to = observation_to
        self.weather_data = weather_data

    def show_summary(self):
            print('-' * 21)
            print(f'Джерело: {self.source}')
            print(f'Період:\n\t{self.observation_from}\n\t{self.observation_to}')
            print(f"Кількість записів: {len(self.weather_data['date'])} записів.")
            print('-' * 21)

    def to_dict(self):
        return {
            'city_name': self.city_name,
            'source': self.source,
            'coordinates':{
                'latitude': self.latitude,
                'longitude': self.longitude
                },
            'period': {
                'observation_from': self.observation_from,
                'observation_to': self.observation_to
                },
            'weather_data': self.weather_data.to_dict('records')
        }
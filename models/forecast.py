class Forecast:
    def __init__(self, city_name, source, latitude, longitude, collected_date, target_date, weather_data):
        self.city_name = city_name
        self.source = source
        self.latitude = latitude
        self.longitude = longitude
        self.collected_date = collected_date
        self.target_date = target_date
        self.weather_data = weather_data

    def show_summary(self):
        print('-' * 21)
        print(f'Джерело: {self.source}')
        print(f'Дата збору даних: {self.collected_date}')
        print(f'Прогноз за датою: {self.target_date}')
        print(f"Кількість записів: {len(self.weather_data['date'])} записів.")
        print('-' * 21)
    def to_dict(self):

        obj_datafile = {
            'city_name': self.city_name,
            'source': self.source,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'collected_date': self.collected_date,
            'target_date': self.target_date,
            'weather_data': self.weather_data.to_dict('records')
        }

        return obj_datafile

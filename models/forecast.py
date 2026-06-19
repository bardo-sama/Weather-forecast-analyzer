class Forecast:
    def __init__(self, city_name, source, latitude, longitude, collected_date, period_start, period_end, weather_data):
        self.city_name = city_name
        self.source = source
        self.latitude = latitude
        self.longitude = longitude
        self.collected_date = collected_date
        self.period_start = period_start
        self.period_end = period_end
        self.weather_data = weather_data

    def show_summary(self):

        print(f'Джерело: {self.source}')
        print(f'Дата збору даних: {self.collected_date}')
        print(f'Період:\n\t{self.period_start}\n\t{self.period_end}')
        print(f'Кількість записів: {len(self.weather_data['date'])}')

    def to_dict(self):

        obj_datafile = {
            'city_name': self.city_name,
            'source': self.source,
            'coordinates':{
                'latitude': self.latitude,
                'longitude': self.longitude
                },
            'collected_date': self.collected_date,
            'period': {
                'start_date': self.period_start,
                'end_date': self.period_end
                },
            'weather_data': self.weather_data.to_dict('records')
        }
        if not obj_datafile:
            print('FIle is empty.')
            return False
        return obj_datafile

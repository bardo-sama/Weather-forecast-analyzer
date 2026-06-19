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

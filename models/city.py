class City:
    def __init__(self, name, latitude, longitude, country_code=None, timezone=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = country_code
        self.timezone = timezone

    def show_city(self):

        print('-' * 18)
        print(f'Назва міста: {self.name}')
        print(f'Координати:')
        print(f'\tШирота: {self.latitude}')
        print(f'\tДовгота: {self.longitude}')
        print(f'Регіон: {self.timezone} - ({self.country_code})')
        print('-' * 18)

    def to_small_dict(self):
        return {
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }
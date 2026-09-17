from models.forecast import Forecast
from models.observation import Observation

class City:
    def __init__(self, name, latitude, longitude, country_code=None, timezone=None, forecasts=None, observations=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = country_code
        self.timezone = timezone
        if forecasts is None:
            self.forecasts = []
        else:
            self.forecasts = list(forecasts)
        if observations is None:
            self.observations = []
        else:
            self.observations = list(observations)

    def __repr__(self):
        return (f"class: City\n"
                f"name: {self.name!r}\n"
                f"timezone: {self.timezone!r}\t({self.country_code!r})")


    def show_city(self):

        print('-' * 21)
        print(f'Назва міста: {self.name}')
        print(f'Координати:')
        print(f'\tШирота: {self.latitude}')
        print(f'\tДовгота: {self.longitude}')
        print(f'Регіон: {self.timezone} - ({self.country_code})')
        if self.forecasts:
            print('Прогноз: доступний.')
        else:
            print('Прогноз: дані відсутні.')
        if self.observations:
            print('Фактичні дані: доступні.')
        else:
            print('Фактичні дані: відсутні.')
        print('-' * 21)

    def add_forecast(self, forecast):
        if forecast is None:
            return False
        else:
            self.forecasts.append(forecast)
            return True

    def add_forecasts(self, forecasts):
        for forecast in forecasts:
            self.add_forecast(forecast)

    def add_observation(self, observation):
        if observation is None:
            return False
        else:
            self.observations.append(observation)
            return True

    def add_observations(self, observations):

        for observation in observations:
            self.add_observation(observation)

    def to_min_dict(self):
        return {
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'country_code': self.country_code,
            'timezone': self.timezone
        }

    def to_dict(self):

        return  {
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'country_code': self.country_code,
            'timezone': self.timezone,
            'forecasts': [forecast.to_dict() for forecast in self.forecasts],
            'observations': [observation.to_dict() for observation in self.observations]
            }



    @classmethod
    def from_dict(cls, data):

        if not isinstance(data, dict):
            return None

        forecasts = [Forecast.from_dict(forecast_data)
                    for forecast_data in data.get('forecasts', [])]

        observations = [Observation.from_dict(observation_data)
                        for observation_data in data.get('observations', [])]

        return cls(
            name=data.get('name'),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            country_code=data.get('country_code'),
            timezone=data.get('timezone'),
            forecasts=forecasts,
            observations=observations,
        )
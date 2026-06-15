import requests
import requests_cache
from settings import CITY_CACHE, REQUEST_NAME_URL
from datetime import timedelta
from support_item.helpers import get_geonames

session_name = requests_cache.CachedSession(CITY_CACHE, expire_after=timedelta(hours=1))

def fetch_json(session, url, params):
    """
    A GET request to the API passed through the request cache.
    -------------------------------------------------
    Робить GET-запит через передану кеш-сесію.
    """

    print('\nStart.')
    print('-' * 21)

    try:
        response = session.get(url, params=params, timeout=5)
        response.raise_for_status()

    except requests.exceptions.HTTPError as error:
        print(f"HTTP-error: {error}")
        return None

    except requests.exceptions.Timeout:
        print("Connection timeout.")
        return None

    except requests.exceptions.RequestException as error:
        print(f'Error: {error}')
        return None

    else:
        print("\nThe function has successfully.")
        print(f"URL: {response.url}")
        if response.from_cache:
            print(f"Response from cache.\n")
        else:
            print('\n')

        return response.json()

    finally:
        print('-' * 21)
        print('Finished.\n')


def fetch_city(city_name, country_code, language='en'):
    """
    Searches for a city via the Open-Meteo Geocoding API
    and returns a list of found cities.
    -----------------------------------------------------
    Шукає місто через Open-Meteo Geocoding API.
    Повертає список знайдених міст.
    """

    city_name = city_name.strip()
    country_code = country_code.strip().upper()
    language = language.strip().lower()

    if country_code == 'UA':
        api_request_name = get_geonames(city_name)
    else:
        api_request_name = city_name

    params = {
        'name': api_request_name,
        'count': 2,
        'format': 'json',
        'countryCode': country_code,
        'language': language
    }

    result = fetch_json(session=session_name, url=REQUEST_NAME_URL, params=params)
    if result is None:
        return []

    return result.get('results', [])
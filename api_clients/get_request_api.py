import requests
from datetime import datetime, timezone

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
        print("The function has successfully.")
        print(f"URL: {response.url}")

        if response.from_cache:
            print(f"Response from cache.")
        else:
            print('')

        return response.json()

    finally:
        print('-' * 21)
        print('Finished.\n')
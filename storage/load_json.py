import json
from pathlib import Path
from models.city import City

def load_json(filename):

    try:
        filename = Path(filename)
        with filename.open('r', encoding='utf-8') as file:
            data = json.load(file)
    except json.JSONDecodeError as error:
        print(f"syntax error: {error}.")
        return []
    except FileNotFoundError:
        print('File not found.')
        return []
    else:
        return data

def load_city_forecast_history(city_name, source):
    city_slug = city_name.strip().lower().replace(" ", "_")

    folder = Path("data") / "forecasts" / city_slug / source
    files = sorted(folder.glob("*.json"))

    main_city = None

    for filename in files:
        data = load_json(filename)

        if data is None:
            continue

        current_city = City.from_dict(data)

        if current_city is None:
            continue

        if main_city is None:
            main_city = City(
                current_city.name,
                current_city.latitude,
                current_city.longitude,
                current_city.country_code,
                current_city.timezone,
            )

        main_city.add_forecasts(current_city.forecasts)

    return main_city
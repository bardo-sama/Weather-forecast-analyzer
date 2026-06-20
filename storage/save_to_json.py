import json
from pathlib import Path
from settings import BASE_DIR
from support_item.helpers import pretty_date

def save_city_to_json(data):
    if not data or data is None:
        print('File is empty.')
        return

    name = data.get('name')

    if not data.get('forecasts'):
        print("Forecasts are empty.")
        return

    start_period = data["forecasts"][0]["period"]
    end_period = data["forecasts"][-1]["period"]


    start_date = pretty_date(start_period, 'start_date')

    end_date = pretty_date(end_period, 'end_date')


    filename = BASE_DIR / f'{name}_{start_date}_{end_date}.json'
    filename = Path(filename)

    filename.parent.mkdir(parents=True, exist_ok=True)


    with filename.open('w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

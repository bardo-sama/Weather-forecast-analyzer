import json
from support_item.helpers import name_for_json

def save_city_to_json(data):
    if not data or data is None:
        print('File is empty.')
        return

    if not data.get('forecasts'):
        print("Forecasts are empty.")
        return

    filename = name_for_json(data)
    filename.parent.mkdir(parents=True, exist_ok=True)


    with filename.open('w', encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

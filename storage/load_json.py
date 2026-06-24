import json
from pathlib import Path

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
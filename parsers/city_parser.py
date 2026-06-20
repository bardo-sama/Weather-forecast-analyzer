from support_item.helpers import return_right_name

def city_parser(city):
    if not city or city is None:
        return False
    current_data = city[0]

    get_valid_name = current_data['name']

    name = return_right_name(get_valid_name)

    clean_data = {
        'name': name,
        'latitude': current_data.get('latitude'),
        'longitude': current_data.get('longitude'),
        'country_code': current_data.get('country_code'),
        'timezone': current_data.get('timezone')
    }

    return clean_data

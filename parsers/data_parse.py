from datetime import datetime

def parse_datetime(data):
    raw_time = data.get('requested_time')

    clean_date = datetime.strftime(raw_time, "%Y-%m-%dT%H:%M")

    return clean_date


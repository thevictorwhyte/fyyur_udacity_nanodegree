from datetime import datetime

def filter_past_shows(item):
    # Returns true if start time is less that current time hence the show has past
    return item['start_time'] < datetime.today().strftime("%m/%d/%Y, %H:%M:%S")

def filter_upcoming_shows(item):
    # Returns true if start time is less that current time hence the show has past
    return item['start_time'] >= datetime.today().strftime("%m/%d/%Y, %H:%M:%S")

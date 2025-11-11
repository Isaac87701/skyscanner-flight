thonfrom datetime import datetime

def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%B %d, %Y')

def get_today_date():
    return datetime.today().strftime('%Y-%m-%d')
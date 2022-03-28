import requests
from decimal import *
from datetime import datetime



def currency_rates(val):
    val = val.upper()
    link = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(link).text

    if val not in response:
        return None

    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{rub}, {datetime.strftime(datetime(day=day, month=month, year=year), '%d:%m:%Y')}"

print(currency_rates('GBP'))

# 1.

# Проверить, установлен ли пакет pillow в глобальном окружении.
# Если да — зафиксировать версию. Установить самую свежую версию pillow,
# если ранее она не была установлена. Сделать подтверждающий скриншот.
# Создать и активировать виртуальное окружение. Убедиться, что в нем нет пакета
# pillow. Сделать подтверждающий скриншот. Установить в виртуальное окружение
# pillow версии 7.1.1 (или другой, отличной от самой свежей). Сделать
# подтверждающий скриншот. Деактивировать виртуальное окружение. Сделать
# подтверждающий скриншот. Скрины нумеровать двухразрядными числами,
# например: «01.jpg», «02.jpg». Если будут проблемы с pillow - можно поработать
# с другим пакетом: например, requests
"""
Подтверждение в файле 01.jpg

"""
# 2.

# #Написать функцию currency_rates(), принимающую в качестве аргумента код
# валюты (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по
# отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация:
# выполнить предварительно запрос к API в обычном браузере, посмотреть
# содержимое ответа. Можно ли, используя только методы класса str, решить
# поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами
# использовать вместо float тип Decimal? Сильно ли усложняется код функции при
# этом? Если в качестве аргумента передали код валюты, которого нет в ответе,
# вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
# регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

import requests

def currency_rates(val):
    val = val.upper()
    link = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(link).text

    if val not in response:
        return None

    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    return rub

print(currency_rates('GBP'))

# 3.
# *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать
# кроме курса дату, которая передаётся в ответе сервера. Дата должна быть в виде
# объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
# использовать в ответе функции?


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
print(currency_rates('gbp'))

# 4.
# Написать свой модуль utils и перенести в него функцию currency_rates()
# из предыдущего задания. Создать скрипт, в котором импортировать этот модуль
# и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего
# лишнего не происходит.

import utils

print(utils.currency_rates('GBP'))


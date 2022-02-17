# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать
# http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
# в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
# str, решить поставленную задачу? Функция должна возвращать результат числового типа,
# например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
# вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
# аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
# функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
# выведите курсы доллара и евро.

import requests


def currency_rates(key):
    currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = currency.text
    list1 = []
    list2 = []
    for el1 in content.split('<CharCode>')[1:]:
        list_currency1 = el1.split('</CharCode>')[0]
        list1.append(list_currency1)
    for el2 in content.split('<Value>')[1:]:
        list_currency2 = el2.split('</Value>')[0]
        list2.append(list_currency2)
    d = dict(zip(list1, list2))
    return d.get(key.upper(), 'None')
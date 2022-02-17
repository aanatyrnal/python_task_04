# 3. *(вместо 2) Доработать функцию currency_rates():
# теперь она должна возвращать кроме курса дату, которая передаётся в ответе сервера.
# Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа,
# какой тип данных лучше использовать в ответе функции?

import requests

def currency_rates(key):
    currency = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = currency.text
    list1 = []
    list2 = []
    for date in content.split('<ValCurs Date="')[1:]:
        date = date.split('"')[0]
    for el1 in content.split('<CharCode>')[1:]:
        list_currency1 = el1.split('</CharCode>')[0]
        list1.append(list_currency1)
    for el2 in content.split('<Value>')[1:]:
        list_currency2 = el2.split('</Value>')[0]
        list2.append(list_currency2)
    d = dict(zip(list1, list2))
    #print(d)
    key = d.get(key.upper(), 'None')
    return (f' {key} на {date}')


print(currency_rates('USD'))
print(currency_rates('eur'))
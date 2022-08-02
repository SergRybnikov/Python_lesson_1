import requests


def currency_rates(currency, currencies):
    return round(currencies.get(currency.lower()), 2)

currencies = dict()
link = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
if link.status_code == 200:
    for info_text in link.text.split('<Nominal>')[1:]:
        info = info_text.split('</Value>')[0].split('</Nominal><Name>')
        nominal = int(info[0])
        info2 = info[1].split('</Name><Value>')
        currency_type = info2[0]
        value = float(info2[1].replace(',', '.'))
        currencies[currency_type.lower()] = value / nominal

print(currency_rates('Доллар США', currencies))
print(currency_rates('Евро', currencies))
print(currency_rates('Фунт стерлингов Соединенного королевства', currencies))

import requests


def get_requests(currency):
    currency = currency.upper()
    response = requests.get('https://bitpay.com/api/rates')
    data = response.json()

    for num in data:
        if num['code'] == currency:
            return num['name'], num['rate']



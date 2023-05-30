import requests

initial_currency = input().upper()
response = requests.get(f'http://www.floatrates.com/daily/{initial_currency}.json').json()
rate_used = {}

try:
    rate_used['usd'] = response['usd']['rate']
except KeyError:
    pass
try:
    rate_used['eur'] = response['eur']['rate']
except KeyError:
    pass

while True:

    currency_to_change = input().lower()
    if currency_to_change == 'usd':
        rate = rate_used['usd']
    elif currency_to_change == 'eur':
        rate = rate_used['eur']
    elif currency_to_change == '':
        break

    money_to_change = float(input())
    print('Checking the cache...')
    rate = str(response[f'{currency_to_change}']['rate'])
    check = rate_used.get(f'{currency_to_change}')

    if check is None:
        rate_used[f'{currency_to_change}'] = rate
        print('Sorry, but it is not in the cache!')
    else:
        print('Oh! It is in the cache!')

    final_money = money_to_change * float(rate)
    print(f'You received {round(final_money, 2)} {currency_to_change.upper()}')


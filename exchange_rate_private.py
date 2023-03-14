import requests  # бібліотека для роботи
import time
import getstatus as gs

res_privat = requests.get('https://api.privatbank.ua/'
                          'p24api/pubinfo?exchange&coursid=5')
gs.get_status(res_privat)
eur = res_privat.json()[0]
usd = res_privat.json()[1]
user_valute = input("Оберіть який курс вам вивести[EUR,USD]: ")
user_valute = user_valute.upper()
match user_valute:
    case 'USD':
        print(f"Валюта: {usd['ccy']}\n\tКупівля: {usd['buy']}"
              f" Продаж: {usd['sale']}")
    case 'EUR':
        print(f"Валюта: {eur['ccy']}\n\tКупівля: {eur['buy']}"
              f" Продаж: {eur['sale']}")
    case user_valute if user_valute != 'USD' or user_valute != ' EUR':
        print('Помилка вводу!')
        user_valute = input("Оберіть який курс вам вивести[EUR,USD]: ")
        user_valute = user_valute.upper()
        match user_valute:
            case 'USD':
                print(f"Валюта: {usd['ccy']}\n\tКупівля: {usd['buy']}"
                      f" Продаж: {usd['sale']}")
            case 'EUR':
                print(f"Валюта: {eur['ccy']}\n\tКупівля: {eur['buy']}"
                      f" Продаж: {eur['sale']}")
time.sleep(7)

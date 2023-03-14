import requests  # бібліотека для роботи
import time
import getstatus as gs

res_privat = requests.get('https://api.privatbank.ua/'
                          'p24api/pubinfo?exchange&coursid=5')
gs.get_status(res_privat)
eur = res_privat.json()[0]
usd = res_privat.json()[1]
user_valute = input("Оберіть валюту[EUR,USD]: ")
user_valute = user_valute.upper()
try:
    amount = int(input('Введіть суму: '))
except ValueError:
    print("Помилка вводу суми, введіть лише цифри!")
    amount = int(input('Введіть сумму: '))
if amount <= 0:
    print("Помилка вводусумми, введіть позитивне число!")
    amount = int(input('Введіть сумму: '))
match user_valute:
    case 'USD':
        buy = float(usd['buy'])
        sale = float(usd['sale'])
        print(sale)
        print(f"Валюта: {amount} {user_valute}"
              f"\n\tКупівля: {round((buy * amount),3)}"
              f" Продаж: {round((sale * amount),3)}")
    case 'EUR':
        buy = float(eur['buy'])
        sale = float(eur['sale'])
        print(f"Валюта: {amount} {user_valute}"
              f"\n\tКупівля: {round((buy * amount),3)}"
              f" Продаж: {round((sale * amount),3)}")
    case user_valute if user_valute != 'USD' or user_valute != 'EUR':
        print('Помилка вводу валюти, повторіть!')
        user_valute = input("Оберіть валюту[EUR,USD]: ")
        user_valute = user_valute.upper()
        match user_valute:
            case 'USD':
                buy = float(usd['buy'])
                sale = float(usd['sale'])
                print(sale)
                print(f"Валюта: {amount} {user_valute}"
                      f"\n\tКупівля: {round((buy * amount),3)}"
                      f" Продаж: {round((sale * amount),3)}")
            case 'EUR':
                buy = float(eur['buy'])
                sale = float(eur['sale'])
                print(f"Валюта: {amount} {user_valute}"
                      f"\n\tКупівля: {round((buy * amount),3)}"
                      f" Продаж: {round((sale * amount),3)}")

time.sleep(10)

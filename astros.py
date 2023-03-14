import requests
import time

response = requests.get("http://api.open-notify.org/astros.json")
resp_astros = response.json()
if response.status_code == 200:
    print('\nIt`s OK, good connection!\n')
print(f"Total numbers of astros: {resp_astros['number']}\n")
astronauts = resp_astros['people']
print("Names of astronauts:")
num = 1
for i in astronauts:
    print(f'{num}){i["name"]}')
    num = num + 1
time.sleep(10)

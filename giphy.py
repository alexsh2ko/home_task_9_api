import requests
import json
import time

key = "ifxcN2DInREnFe83Ym1OABrD2zP2bsBj"
user_word = input("Введіть ваше слово: ")
url = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={user_word}"
resp_search = requests.get(url)
resp_json = resp_search.json()
for gif in resp_json["data"]:
    print(gif["url"])
time.sleep(15)

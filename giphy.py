import requests
import time

user_word = input("Введіть ваше слово: ")


def give_giphy(user_word: str) -> str:
    '''
    The function accepts a request from a user and
    displays the search result based on the user's input from giphy.com

    Parameters
    ----------
        user_word : the variable contains a string from user input

    Returns
    -------
    Displaying user search results from giphy.com
    '''
    key = "ifxcN2DInREnFe83Ym1OABrD2zP2bsBj"
    url = f"https://api.giphy.com/v1/gifs/search?api_key={key}&q={user_word}"
    resp_search = requests.get(url)
    resp_json = resp_search.json()
    for gif in resp_json["data"]:
        return print(gif["url"])


give_giphy(user_word)
time.sleep(15)

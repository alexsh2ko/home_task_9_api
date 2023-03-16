import requests
import time
us_city = input("Enter city name: ")
api_key = "6f6a636241627bb40d71f0a52a2cf100"


def weather_searching(us_city: str, api_key: str) -> str:
    '''
    The function accepts a request from a user and
    displays information about the weather
    based on the user's city input from openweathermap.org

    Parameters
    ----------
        us_city : the variable contains a string from user input
        api_key : the variable contains a string
                  with api key from openweathermap.org

    Returns
    -------
    Displaying information about the weather in user city
    '''
    response = requests.get(f"https://api.openweathermap.org/"
                            f"data/2.5/weather?q={us_city}"
                            f"&appid={api_key}&units=metric")
    resp_weather = response.json()
    if resp_weather.status_code == 200:
        summary_res = response.json()
        temp = summary_res["main"]["temp"]
        feels_like = summary_res["main"]["feels_like"]
        description = summary_res["weather"][0]["description"]
        temp_min = summary_res["main"]["temp_min"]
        temp_max = summary_res["main"]["temp_max"]
        humidity = summary_res["main"]["humidity"]
        wind = summary_res["wind"]["speed"]
        return print(f"\nCurrent weather in {us_city}:\n \n{description}"
                     f"\ntemperature is {temp}°C but feels like {feels_like}°C"
                     f"\nmin temperature is {temp_min}"
                     f"\nmax temperature is {temp_max}"
                     f"\nhumidity is {humidity}"
                     f"\nwind speed is {wind}")
    else:
        print("Error retrieving weather information.")


weather_searching(us_city, api_key)
time.sleep(7)

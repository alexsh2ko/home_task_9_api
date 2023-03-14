import requests
import time
api_key = "6f6a636241627bb40d71f0a52a2cf100"
us_city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={us_city}&appid={api_key}&units=metric"
response = requests.get(url)
resp_weather = response.json()
if response.status_code == 200:
    summary_res = response.json()
    temp = summary_res["main"]["temp"]
    feels_like = summary_res["main"]["feels_like"]
    description = summary_res["weather"][0]["description"]
    temp_min = summary_res["main"]["temp_min"]
    temp_max = summary_res["main"]["temp_max"]
    humidity = summary_res["main"]["humidity"]
    sea_level = summary_res["main"]["sea_level"]
    grnd_level = summary_res["main"]["grnd_level"]
    wind = summary_res["wind"]["speed"]
    print(f"Current weather in {us_city}: \n{description}"
          f"\ntemperature is {temp}°C but feels like {feels_like}°C"
          f"\nmin temperature is {temp_min}"
          f"\nmax temperature is {temp_max}"
          f"\nhumidity is {humidity}"
          f"\nsea level is {sea_level}"
          f"\ngrnd level is {grnd_level}"
          f"\nwind speed is {wind}")
else:
    print("Error retrieving weather information.")
time.sleep(7)

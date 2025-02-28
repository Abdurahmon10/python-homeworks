import requests
import json
import os



API_KEY = os.getenv("API_KEY")
print(API_KEY)



city="Tashkent"


weather=requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}").json()

lat=weather[0]["lat"]
lon=weather[0]["lon"]

info=requests.get(f"https://api.openweathermap.org/data/3.0/onecalllat={lat}&lon={lon}&appid={API_KEY}")

print(f"Info Status Code: {info.status_code}")
print(f"Info Response Text: {info.text}")

# If the request was successful, print the weather data
if info.status_code == 200:
    weather_data = info.json()
    print(weather_data)
else:
    print(f"Failed to fetch weather data. Status code: {info.status_code}")



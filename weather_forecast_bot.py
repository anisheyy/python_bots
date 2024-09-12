import requests
from datetime import datetime

def hPa_to_pascal(pressure):
    return pressure * 100

def return_celcius(temp):
    return temp - 273.16

def print_forecasts(data):
    daily_forecasts = {}
    for entry in data["list"]:
        date = entry["dt_txt"].split()[0]
        if date not in daily_forecasts:
            daily_forecasts[date] = []
        daily_forecasts[date].append(entry)

    for date, forecasts in daily_forecasts.items():
        print(f"\nWeather Forecast for {date}:")
        print("-" * 40)
        for forecast in forecasts:
            time = forecast["dt_txt"].split()[1]
            temp = return_celcius(forecast["main"]["temp"])
            humidity = forecast["main"]["humidity"]
            pressure = hPa_to_pascal(forecast["main"]["pressure"])
            wind_speed = forecast["wind"]["speed"]
            

            print(f"Time: {time}")
            print(f"  Temperature: {temp:.2f}C")
            print(f"  Humidity: {humidity}%")
            print(f"  Pressure: {pressure}Pa")
            print(f"  Wind: {wind_speed} m/s")


base_url = "http://api.openweathermap.org/data/2.5/forecast?"
city = "Kathmandu"
api_key = "08bc91ba769fa712534f66b88408674a"

complete_url = base_url + "q=" + city + "&appid=" + api_key

response = requests.get(complete_url)
data = response.json()

# print(data)

if data["cod"] != 404:
    print_forecasts(data)
else:
    print("error")
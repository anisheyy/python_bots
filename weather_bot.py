import requests

api_key = "08bc91ba769fa712534f66b88408674a"  
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Lokanthali" 
complete_url = base_url + "q=" + city + "&appid=" + api_key

response = requests.get(complete_url)
data = response.json()


# print(data)

if data["cod"] != "404":
    weather = data["main"]
    temp = weather["temp"]
    pres = weather["pressure"]
    humi = weather["humidity"]
    visibility = data["visibility"]
    wind = data["wind"]
    w_speed = wind["speed"]
    print(f"Wind speed at {city}: {w_speed}")
    print(f"Visibility of {city}: {visibility}")
    print(f"Temperature in {city}: {temp}")
    print(f"Pressure in {city}: {pres}")
    print(f"Humidity in {city}: {humi}")
else:
    print("City not found!")

import requests

city = input("Enter city name: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

geo_response = requests.get(geo_url)

geo_data = geo_response.json()

if "results" in geo_data:

    latitude = geo_data["results"][0]["latitude"]
    longitude = geo_data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    weather_response = requests.get(weather_url)

    weather_data = weather_response.json()

    print("\n==============================")
    print("      Weather Report")
    print("==============================")
    print(f"City         : {city.title()}")
    print(f"Temperature  : {weather_data['current_weather']['temperature']} °C")
    print(f"Wind Speed   : {weather_data['current_weather']['windspeed']} km/h")
    print("==============================")
else:
    print("City not found")
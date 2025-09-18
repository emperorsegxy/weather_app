from dotenv import load_dotenv
import os
import requests

load_dotenv()

def get_current_weather(city="Ikorodu"):
    API_KEY = os.getenv("WEATHER_API_KEY")
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    print(response, 'resp')
    if response.status_code == 200:
        return response.json()
    return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather_data = get_current_weather(city)
    if weather_data:
        print(f"Current temperature in {city}: {weather_data['main']['temp']}°C")
    else:
        print("City not found or API error.")
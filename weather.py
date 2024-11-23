from dotenv import load_dotenv
import requests
import os

# Load environment variables from .env file
load_dotenv()

def get_current_weather(city="Kansas City"):
    """
    Fetch current weather data for the given city from OpenWeatherMap API.
    """
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    return requests.get(request_url).json()

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name: ")
    weather_data = get_current_weather(city)
    print("\nWeather Data:")
    pprint(weather_data)

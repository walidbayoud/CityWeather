from dotenv import load_dotenv
import requests
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[
                        logging.StreamHandler()
                    ])

# Load environment variables from .env file
load_dotenv()

def get_current_weather(key, city="Kansas City"):
    """
    Fetch current weather data for the given city from OpenWeatherMap API.
    """
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={key}&q={city}&units=metric'
    
    return requests.get(request_url).json()


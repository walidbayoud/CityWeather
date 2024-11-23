import unittest
import logging
from weather import get_current_weather
import os

logging.basicConfig(level=logging.CRITICAL) # Disable logging
logging.getLogger().setLevel(logging.CRITICAL) # Disable all logging

API_URL_WITHOUT_KEY = "http://api.openweathermap.org/data/2.5/weather?q=Budapest&units=metric"
api_key = os.getenv("API_KEY")

class TestAPICall(unittest.TestCase):
    def test_api_request(self):
        response = get_current_weather(key=api_key, city="Budapest") # Test with a known city

        self.assertEqual(response["name"], "Budapest") # Check if the city name is correct
        self.assertEqual(response["cod"], 200) # Check if the response code is 200

    def test_unknown_city(self):
        response = get_current_weather(key=api_key, city="UnknownCity")

        self.assertEqual(response["cod"], "404") # Check if the response code is 404

    def test_empty_city(self):
        response = get_current_weather(key=api_key, city="")

        self.assertEqual(response["cod"], "400") # Check if the response code is 400

    def test_api_request_without_key(self):
        response = get_current_weather(city="Budapest", key="")

        self.assertEqual(response["cod"], 401) # Check if the response code is 401

if __name__ == "__main__":
    unittest.main()
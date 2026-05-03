import requests
from decouple import config
import geocoder
import os
import json
import random

# Services
from Services.Redis.redis import RedisStorage

class Utils:

    WEATHER_API_KEY = config("weather_api_key", cast=str)
    WEATHER_API_URL = config("weather_api_path", cast=str)
    def __init__(self):
        self._redis = RedisStorage()

    def call_weather_api(self):
        
        g = geocoder.ip('me') 
        LAT, LONG = g.latlng
    
        url = f"{self.WEATHER_API_URL}?key={self.WEATHER_API_KEY}&q={LAT},{LONG}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()

        weather_data = {
            "city_name": data['location']['name'],
            "country": data['location']['country'],
            "temp": data['current']["temp_c"],
            "condition": data['current']['condition']['text'],
            "humidity": data['current']['humidity']
        }

        self._redis.set_weather_data(weather_data)

        return weather_data

    def fetch_quote_data(self):
        quote_data_path = os.path.join(os.getcwd(), "Data", "quotes.json")

        with open(quote_data_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        
        quote = None
        while True:
            quote = random.choice(data)
            if len(quote) <= config("quote_max_length", cast=int, default=50):
                break
        
        self._redis.set_quote_data(quote)

        return quote

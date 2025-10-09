from kivy.properties import StringProperty, ListProperty
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from Storage.Cache import Cache
import requests
from decouple import config

class WeatherScreen(Screen):
    temp = StringProperty("--°")
    description = StringProperty("Loading...")
    city = StringProperty("Loading...")
    min_max_temp = StringProperty("--/--")
    background_color = ListProperty([0.961, 0.965, 0.98, 1]) # Default soothing color

    update_event = None

    def on_enter(self):
        self.update_weather_data()
        # Schedule the update to run every 300 seconds (5 minute)
        self.update_event = Clock.schedule_interval(self.update_weather, 300)

    def on_leave(self):
        # Called when screen is hidden => Cancel the scheduled update
        if self.update_event:
            self.update_event.cancel()

    def default_weather_data(self):
        return {
            "location": {"name": "Unknown City"},
            "current": {
                "temp_c": "0",
                "condition": {"text": "Error"},
                "feelslike_c": "0"
            }
        }

    def call_weather_api(self):
        try:
            lat, long = 28.6, 77.2
            url = f"{config('weather_api_path', cast=str)}?key={config('weather_api_key')}&q={lat},{long}"
            response = requests.request("GET", url)
            api_data = response.json()
        except Exception as e:
            print("ERROR", e)
            api_data = self.default_weather_data()
        return api_data

    def update_weather_data(self):
        cache = Cache()
        data = cache.get_weather_data()
        self.update_weather(data=data)
        
    def update_weather(self, dt: float|None=None, data: dict|None=None, ):
        print("Updating weather data...")
        if data is None:
            print("API call", data, dt)
            cache = Cache()
            api_data = self.call_weather_api()
            cache.set_weather_data(api_data)
        else:
            print("No api call", data, dt)
            api_data = data

        self.city = api_data['location']['name']
        self.temp = f"{int(api_data['current']['temp_c'])}°C"
        self.description = api_data['current']['condition']['text'].upper()
        self.min_max_temp = f"Feels like {int(api_data['current']['feelslike_c'])}°"
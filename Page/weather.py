import tkinter as tk
import requests
import time
from decouple import config

from Services.Style import WeatherPageStyle
from Services.Static.static import WEATHER
from Services.Redis.redis import RedisStorage
from Services.utils import Utils

class WeatherPage(tk.Frame):

    # Update in every 10 min = 600000ms
    UPDATE_INTERVAL_MS = config("weather_api_call_frequency", cast=int)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Weather"
        self.redis = RedisStorage()

        self.utils = Utils()

        self.configure(bg=WeatherPageStyle.RETRO_BG)

        # --- Create UI Elements ---
        self.weather_label = tk.Label(self, **WeatherPageStyle.WeatherLabel)
        self.weather_label.pack(**WeatherPageStyle.WeatherLabelPack)
        
        self.last_updated_label = tk.Label(self, **WeatherPageStyle.LastUpdatedLabel)
        self.last_updated_label.pack(**WeatherPageStyle.LastUpdatedLabelPack)
        
        self.fetch_weather()
    
    def fetch_weather(self):
        """
        Fetch data from redis and if data not found then call the weather api.
        Once data is available then call the update ui with details
        If an error in between, then anime style error line is shown to user
        """

        try:
            data = self.redis.get_weather_data()
            if data is None:
                data = self.utils.call_weather_api()
            
            self.after(0, self.update_ui, data)
        
        except requests.exceptions.RequestException:
            self.after(0, self.update_ui, WEATHER["Request_Error"], True)
        
        except Exception as e:
            self.after(0, self.update_ui, WEATHER["Logic_Error"], True)
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_weather)

    def update_ui(self, weather_data: dict|str, error: bool = False):
        """
        Update ui with weather data if error is False and text color is neon green (success color).
        If error is True then change text color to red (error color) and show error message in weather_data
        """

        if error:
            text_color = WeatherPageStyle.WeatherLabelStateColor["error_color"]
            weather_text = weather_data
        else:
            weather_text = f"Location: {weather_data['city_name']}, {weather_data['country']}\n"
            weather_text += f"Current temperature: {weather_data['temp']}°C\n"
            weather_text += f"Condition: {weather_data['condition']}\n"
            weather_text += f"Humidity: {weather_data['humidity']}%"

            text_color = WeatherPageStyle.WeatherLabelStateColor["success_color"]    
        
        self.weather_label.config(text=weather_text, foreground=text_color)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
        
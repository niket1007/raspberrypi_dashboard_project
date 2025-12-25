import tkinter as tk
import requests
import time
from decouple import config
import geocoder
from Services.Style import Style
from Services.Redis.redis import RedisStorage

class WeatherPage(tk.Frame):

    WEATHER_API_KEY = config("weather_api_key", cast=str)
    WEATHER_API_URL = config("weather_api_path", cast=str)
    UNITS = "metric"
    UPDATE_INTERVAL_MS = config("weather_api_call_frequency", cast=int)
    
    def __get_coordinates(self):
        g = geocoder.ip('me') 
        return g.latlng
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Weather"
        self.redis = RedisStorage()

        self.LAT, self.LONG = self.__get_coordinates()

        # --- Create UI Elements ---
        self.weather_label = tk.Label(self, text="Loading weather...", 
                                      font=(Style.font, 18),
                                      justify="left")
        self.weather_label.pack(side="top", pady=20)
        
        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           font=(Style.font, 8))
        self.last_updated_label.pack(side="bottom", pady=5)
        
        self.fetch_weather()
    
    def fetch_weather(self):
        try:
            data = self.redis.get_weather_data()
            if data is None:
                data = self.__fetch_weather_api()
            
            self.after(0, self.update_ui, data)
        
        except requests.exceptions.RequestException:
            self.after(0, self.update_ui, "Error:\nCould not fetch weather", True)
        
        except Exception as e:
            self.after(0, self.update_ui, f"An error occurred:\n{e}", True)
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_weather)


    def __fetch_weather_api(self):
        """Updates the weather data through api call."""
        url = f"{self.WEATHER_API_URL}?key={self.WEATHER_API_KEY}&q={self.LAT},{self.LONG}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        location = f"{data['location']['name']}, {data['location']['country']}"
        temp = data['current']["temp_c"]
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        
        display_text = f"Location: {location}\n"
        display_text += f"Current temperature: {temp}°C\n"
        display_text += f"Condition: {condition}\n"
        display_text += f"Humidity: {humidity}%"

        self.redis.set_weather_data(display_text)

        return display_text

    def update_ui(self, weather_text: str, error: bool = False):
        """Updates the weather data on the screen."""
        text_color = "black"
        if error:
            text_color = "red"
        
        self.weather_label.config(text=weather_text, foreground=text_color)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
        
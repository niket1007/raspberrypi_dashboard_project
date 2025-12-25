import tkinter as tk
import requests
import time
from decouple import config
from Configs.Style import Style

class WeatherPage(tk.Frame):

    WEATHER_API_KEY = config("weather_api_key", cast=str)
    WEATHER_API_URL = config("weather_api_path", cast=str)
    LAT, LONG = 28.6, 77.2
    UNITS = "metric"
    UPDATE_INTERVAL_MS = config("weather_api_call_frequency", cast=int)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Weather"
        # --- Create UI Elements ---
        self.weather_label = tk.Label(self, text="Loading weather...", 
                                      font=(Style.font, 18),
                                      justify="left")
        self.weather_label.pack(side="top", pady=20)
        
        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           font=(Style.font, 8))
        self.last_updated_label.pack(side="bottom", pady=5)
        
        self.fetch_weather()

    def update_ui(self, weather_text, text_color="black"):
        """Updates the weather data on the screen."""
        self.weather_label.config(text=weather_text, foreground=text_color)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
    
    def fetch_weather(self):
        """Updates the weather data through api call."""
        try:
            url = f"{self.WEATHER_API_URL}?key={self.WEATHER_API_KEY}&q={self.LAT},{self.LONG}"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            temp = data['current']["temp_c"]
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            
            display_text = f"Current temperature: {temp}°C\n"
            display_text += f"Condition: {condition}\n"
            display_text += f"Humidity: {humidity}%"
            
            self.after(0, self.update_ui, display_text, "black")

        except requests.exceptions.RequestException:
            self.after(0, self.update_ui, "Error:\nCould not fetch weather", "red")
        
        except Exception as e:
            self.after(0, self.update_ui, f"An error occurred:\n{e}", "red")
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_weather)

import tkinter as tk
from tkinter import ttk
import requests
import threading
import time
from decouple import config
from Style import Style

# Ensure you have a .env file or replace this with your actual key string
WEATHER_API_KEY = config("weather_api_key", cast=str)
CITY = "New York"
UNITS = "metric"
UPDATE_INTERVAL_MS = 300000 # 5 minutes

class WeatherPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Weather"
        # --- Create UI Elements ---
        self.title_label = ttk.Label(self, text="Weather", 
                                    font=(Style.font, 24, "bold"))
        self.title_label.pack(side="top", pady=10)

        self.weather_label = ttk.Label(self, text="Loading weather...", 
                                      font=(Style.font, 18),
                                      justify="left")
        self.weather_label.pack(side="top", pady=20)
        
        self.last_updated_label = ttk.Label(self, text="Last updated: Never",
                                           font=(Style.font, 8))
        self.last_updated_label.pack(side="bottom", pady=5)
        
        # --- Start the update loop ---
        self.start_weather_update()

    def start_weather_update(self):
        threading.Thread(target=self.fetch_weather, daemon=True).start()

    # Fixed typo: renamed from update__ui to update_ui to match exception calls
    def update_ui(self, weather_text, text_color="black"):
        self.weather_label.config(text=weather_text, foreground=text_color)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")

    def fetch_weather(self):
        try:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}&aqi=no"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            temp = data['current'][f'temp_{"c" if UNITS == "metric" else "f"}']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            
            display_text = f"Current temperature: {temp}°{'C' if UNITS == 'metric' else 'F'}\n"
            display_text += f"Condition: {condition}\n"
            display_text += f"Humidity: {humidity}%"
            
            self.after(0, self.update_ui, display_text, "black")

        except requests.exceptions.RequestException:
            self.after(0, self.update_ui, "Error:\nCould not fetch weather", "red")
        
        except Exception as e:
            self.after(0, self.update_ui, f"An error occurred:\n{e}", "red")
        
        finally:
            self.after(UPDATE_INTERVAL_MS, self.start_weather_update)
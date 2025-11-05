import ttkbootstrap as ttk
import requests
import threading
import time
from decouple import config

WEATHER_API_KEY = config("weather_api_key", cast=str)
CITY = "New York"
UNITS = "metric"
UPDATE_INTERVAL_MS = 300000 # 5 minutes

class WeatherPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # --- Create UI Elements ---
        # 'bootstyle="primary"' makes the title the accent color
        self.title_label = ttk.Label(self, text="Weather", 
                                    font="Helvetica 18 bold", 
                                    bootstyle="primary")
        self.title_label.pack(side="top", pady=10)

        # 'bootstyle="inverse-dark"' for white text
        self.weather_label = ttk.Label(self, text="Loading weather...", 
                                      font="Helvetica 14", 
                                      bootstyle="inverse-dark",
                                      justify="left")
        self.weather_label.pack(side="top", pady=20)
        
        # 'bootstyle="secondary"' for a muted gray text
        self.last_updated_label = ttk.Label(self, text="Last updated: Never",
                                           font="Helvetica 8",
                                           bootstyle="secondary")
        self.last_updated_label.pack(side="bottom", pady=5)
        
        # --- Start the update loop ---
        self.start_weather_update()

    def start_weather_update(self):
        threading.Thread(target=self.fetch_weather, daemon=True).start()

    def update__ui(self, weather_text, style="inverse-dark"):
        self.weather_label.config(text=weather_text, bootstyle=style)
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
            
            display_text = f"Current temperature: {temp}°{'C' if UNITS == "metric" else 'F'}\n"
            display_text += f"Condition: {condition}\n"
            display_text += f"Humidity: {humidity}%"
            
            self.after(0, self.update__ui, display_text)

        except requests.exceptions.RequestException:
            # 'bootstyle="danger"' will make the error text red
            self.after(0, self.update_ui, "Error:\nCould not fetch weather", "danger")
        
        except Exception as e:
            self.after(0, self.update_ui, f"An error occurred:\n{e}", "danger")
        
        finally:
            # This is the 5-minute scheduler
            self.after(UPDATE_INTERVAL_MS, self.start_weather_update)

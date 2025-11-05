import tkinter as tk
import requests
import threading
import time
from decouple import config

# NOTE: You'll need to add your API key and city
WEATHER_API_KEY = config('weather_api_key', cast=str)
CITY = "New York"
UNITS = "metric" # or "imperial"

# 5 minutes in milliseconds (5 * 60 * 1000)
UPDATE_INTERVAL_MS = 300000 

class WeatherPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller

        # --- Create UI Elements ---
        self.title_label = tk.Label(self, text="Weather", 
                                    font=controller.title_font, 
                                    bg="black", fg="white")
        self.title_label.pack(side="top", pady=10)

        self.weather_label = tk.Label(self, text="Loading weather...", 
                                      font=controller.body_font, 
                                      bg="black", fg="white",
                                      justify="left")
        self.weather_label.pack(side="top", pady=20)
        
        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           font=("Helvetica", 8),
                                           bg="black", fg="gray")
        self.last_updated_label.pack(side="bottom", pady=5)
        
        # --- Start the update loop ---
        self.start_weather_update()

    def start_weather_update(self):
        # This function runs the 'fetch_weather' function in a new thread
        # This keeps the UI responsive
        threading.Thread(target=self.fetch_weather, daemon=True).start()

    def fetch_weather(self):
        # This is the 'blocking' function that runs in the background
        try:
            url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={CITY}&aqi=no"
            
            response = requests.get(url, timeout=10)
            response.raise_for_status() # Raise an error for bad responses
            
            data = response.json()
            
            # Extract data
            temp = data['current'][f'temp_{"c" if UNITS == "metric" else "f"}']
            condition = data['current']['condition']['text']
            humidity = data['current']['humidity']
            
            # Format the output string
            display_text = f"Current temperature: {temp}°{'C' if UNITS == "metric" else 'F'}\n"
            display_text += f"Condition: {condition}\n"
            display_text += f"Humidity: {humidity}%"
            
            # Schedule the UI update on the main thread
            self.after(0, self.update_ui, display_text)

        except requests.exceptions.RequestException:
            # Handle network errors
            self.after(0, self.update_ui, "Error:\nCould not fetch weather")
        
        except Exception as e:
            # Handle other errors (like JSON parsing)
            self.after(0, self.update_ui, f"An error occurred:\n{e}")
        
        finally:
            # --- THIS IS THE SCHEDULER ---
            # After the function finishes (or fails),
            # schedule this function to run again in 5 minutes.
            self.after(UPDATE_INTERVAL_MS, self.start_weather_update)

    def update_ui(self, weather_text):
        # This function is guaranteed to run on the main thread
        self.weather_label.config(text=weather_text)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
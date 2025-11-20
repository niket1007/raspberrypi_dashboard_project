import tkinter as tk
import requests
import threading
import time
from decouple import config

QUOTE_API_URL = config("quote_api_path", cast=str)
UPDATE_INTERVAL_MS = config("quote_api_call_frequency", cast=int)

class QuotePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # --- Create UI Elements ---
        self.title_label = tk.Label(self, text="Quote of the Moment", 
                                    font=("Helvetica", 18, "bold"))
        self.title_label.pack(side="top", pady=10, padx=20)

        center_frame = tk.Frame(self)
        center_frame.pack(fill="both", expand=True)

        self.quote_label = tk.Label(center_frame, text="Loading quote...", 
                                      font=("Helvetica", 16, "bold", "italic"), 
                                      wraplength=750,
                                      anchor="center")
        self.quote_label.pack(side="top", pady=(20, 10), padx=20)
        
        self.char_label = tk.Label(center_frame, text="", 
                                      font=("Helvetica", 12), 
                                      anchor="center")
        self.char_label.pack(side="top", pady=(0, 20), padx=20)

        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           font=("Helvetica", 8))
        self.last_updated_label.pack(side="bottom", pady=5)
        
        self.fetch_quote()

    def fetch_quote(self):
        try:
            response = requests.get(QUOTE_API_URL, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            data = data['data']

            quote = f"\"{data['content']}\""
            character = f"- {data['character']['name']}"
            anime = f"({data['anime']['name']})"
            
            self.after(0, self.update_ui, quote, character, anime)

        except requests.exceptions.RequestException as e :
            print(e)
            self.after(0, self.update_ui, "Error: Could not fetch quote.", "", "", "red")
        
        except Exception as e:
            self.after(0, self.update_ui, f"An error occurred: {e}", "", "", "red")
        
        finally:
            self.after(UPDATE_INTERVAL_MS, self.fetch_quote)

    def update_ui(self, quote, character, anime, text_color="black"):
        self.quote_label.config(text=quote, foreground=text_color)
        self.char_label.config(text=f"{character} {anime}")
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
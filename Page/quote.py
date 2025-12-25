import tkinter as tk
import requests
import time
from decouple import config
from Services.Style import QuotePageStyle
from Services.Redis.redis import RedisStorage

class QuotePage(tk.Frame):
    
    QUOTE_API_URL = config("quote_api_path", cast=str)
    UPDATE_INTERVAL_MS = config("quote_api_call_frequency", cast=int)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Quote"
        self.redis = RedisStorage()

        # --- Create UI Elements ---
        center_frame = tk.Frame(self)
        center_frame.pack(**QuotePageStyle.FramePack)

        self.quote_label = tk.Label(center_frame, text="Loading quote...", 
                                      **QuotePageStyle.QuoteLabel)
        self.quote_label.pack(**QuotePageStyle.QuoteLabelPack)
        
        self.char_label = tk.Label(center_frame, text="", 
                                      **QuotePageStyle.CharacterLabel)
        self.char_label.pack(**QuotePageStyle.CharacterLabelPack)

        self.refresh_button = tk.Button(self, text="Refresh", command=lambda _: self.fetch_quote())

        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           **QuotePageStyle.LastUpdatedLabel)
        self.last_updated_label.pack(**QuotePageStyle.LastUpdatedLabelPack)
        
        self.fetch_quote()
    
    def update_redis_data(self, data: dict):
        self.redis.set_quote_data(data)
    
    def fetch_quote(self):
        try:
            data = self.redis.get_quote_data()
            if data is None:
                print("called api")
                data = self.__fetch_quote_api()
            
            self.after(0, self.update_ui, data)

        except requests.exceptions.RequestException as e :
            print(e)
            data = {
                "content": "The connection has been severed. We must rely on our own strength.",
                "charcter": {
                    "name": "Error"
                },
                "anime": {
                    "name": "API"
                }
            }
            self.after(0, self.update_ui, data, True)
        
        except Exception as e:
            print(e)
            data = {
                "content": "The threads of fate have snapped. This error exceeds the boundaries of this world's logic.",
                "charcter": {
                    "name": "Error"
                },
                "anime": {
                    "name": "Logic"
                }
            }
            self.after(0, self.update_ui, data, True)
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_quote)

    
    def __fetch_quote_api(self):
        """Fetch anime quote through api call."""
        response = requests.get(self.QUOTE_API_URL, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        data = data['data']

        self.update_redis_data(data)

        return data

    def update_ui(self, data: dict, error: bool = False):
        """Updates the quote in the screen."""

        quote = data['content']
        character = f"- {data['character']['name']}"
        anime = f"({data['anime']['name']})"

        foreground_color = QuotePageStyle.QuoteLabelStateColor["success_color"]
        if error:
            foreground_color = QuotePageStyle.QuoteLabelStateColor["error_color"]

        self.quote_label.config(text=quote, foreground=foreground_color)
        self.char_label.config(text=f"{character} {anime}")
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
import tkinter as tk
import time
import random
from decouple import config
import os
import json
from Services.Style import QuotePageStyle
from Services.Redis.redis import RedisStorage
from Services.Static.static import QUOTE

class QuotePage(tk.Frame):
    
    UPDATE_INTERVAL_MS = config("quote_file_call_frequency", cast=int)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Quote"
        self.redis = RedisStorage()

        # --- Create UI Elements ---
        center_frame = tk.Frame(self)
        center_frame.pack(**QuotePageStyle.FramePack)

        self.quote_label = tk.Label(center_frame, **QuotePageStyle.QuoteLabel)
        self.quote_label.pack(**QuotePageStyle.QuoteLabelPack)

        self.last_updated_label = tk.Label(self, **QuotePageStyle.LastUpdatedLabel)
        self.last_updated_label.pack(**QuotePageStyle.LastUpdatedLabelPack)
        
        self.fetch_quote()
    
    def update_redis_data(self, data: dict):
        self.redis.set_quote_data(data)
    
    def fetch_quote(self):
        try:
            data = self.redis.get_quote_data()
            if data is None:
                data = self.__fetch_quote_file()
            
            self.after(0, self.update_ui, data)

        except OSError as e :
            print(e)
            self.after(0, self.update_ui, QUOTE["File_Error"], True)
        
        except Exception as e:
            print(e)
            self.after(0, self.update_ui, QUOTE["Logic_Error"], True)
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_quote)

    
    def __fetch_quote_file(self):
        """Fetch anime quote through reading the quote data file."""

        quote_data_path = os.path.join(os.getcwd(), "Data", "quotes.json")
        with open(quote_data_path, "r") as file:
            data = json.load(file)
        
        quote = ""
        while True:
            quote = random.choice(data)
            if len(quote) <= config("quote_max_length", cast=int, default=50):
                break
        
        self.update_redis_data(quote)

        return quote

    def update_ui(self, data: dict, error: bool = False):
        """Updates the quote in the screen."""

        foreground_color = QuotePageStyle.QuoteLabelStateColor["success_color"]
        if error:
            foreground_color = QuotePageStyle.QuoteLabelStateColor["error_color"]

        self.quote_label.config(text=data["quote"], foreground=foreground_color)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")

import tkinter as tk
import time
import random
from decouple import config
import os
import json

# Services
from Services.Style import QuotePageStyle
from Services.Redis.redis import RedisStorage
from Services.Static.static import QUOTE
from Services.utils import Utils

class QuotePage(tk.Frame):
    
    UPDATE_INTERVAL_MS = config("quote_file_call_frequency", cast=int)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Quote"
        self._redis = RedisStorage()
        self._utils = Utils()

        self.configure(bg=QuotePageStyle.RETRO_BG)

        # --- Create UI Elements ---
        center_frame = tk.Frame(self, bg=QuotePageStyle.RETRO_BG)
        center_frame.pack(**QuotePageStyle.FramePack)

        self.quote_label = tk.Label(center_frame, **QuotePageStyle.QuoteLabel)
        self.quote_label.pack(**QuotePageStyle.QuoteLabelPack)

        self.last_updated_label = tk.Label(self, **QuotePageStyle.LastUpdatedLabel)
        self.last_updated_label.pack(**QuotePageStyle.LastUpdatedLabelPack)
        
        self.fetch_quote()
    

    def fetch_quote(self):
        try:
            data = self._redis.get_quote_data()
            if data is None:
                data = self._utils.fetch_quote_data()
            
            self.after(0, self.update_ui, data)

        except OSError as e :
            print(e)
            self.after(0, self.update_ui, QUOTE["File_Error"], True)
        
        except Exception as e:
            print(e)
            self.after(0, self.update_ui, QUOTE["Logic_Error"], True)
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_quote)

    def update_ui(self, data: dict, error: bool = False):

        foreground_color = QuotePageStyle.QuoteLabelStateColor["success_color"]
        if error:
            foreground_color = QuotePageStyle.QuoteLabelStateColor["error_color"]

        self.quote_label.config(text=data["quote"], foreground=foreground_color)
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")

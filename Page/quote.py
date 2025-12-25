import tkinter as tk
import requests
import time
from decouple import config
from Configs.Style import QuotePageStyle

class QuotePage(tk.Frame):
    
    QUOTE_API_URL = config("quote_api_path", cast=str)
    UPDATE_INTERVAL_MS = config("quote_api_call_frequency", cast=int)
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Quote"

        # --- Create UI Elements ---
        center_frame = tk.Frame(self)
        center_frame.pack(**QuotePageStyle.FramePack)

        self.quote_label = tk.Label(center_frame, text="Loading quote...", 
                                      **QuotePageStyle.QuoteLabel)
        self.quote_label.pack(**QuotePageStyle.QuoteLabelPack)
        
        self.char_label = tk.Label(center_frame, text="", 
                                      **QuotePageStyle.CharacterLabel)
        self.char_label.pack(**QuotePageStyle.CharacterLabelPack)

        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           **QuotePageStyle.LastUpdatedLabel)
        self.last_updated_label.pack(**QuotePageStyle.LastUpdatedLabelPack)
        
        self.fetch_quote()

    def fetch_quote(self):
        """Fetch anime quote through api call."""
        try:
            response = requests.get(self.QUOTE_API_URL, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            data = data['data']

            quote = f"\"{data['content']}\""
            character = f"- {data['character']['name']}"
            anime = f"({data['anime']['name']})"
            
            self.after(0, self.update_ui, quote, character, anime)

        except requests.exceptions.RequestException as e :
            print(e)
            self.after(0, self.update_ui, "The connection has been severed. We must rely on our own strength.", "Error", "", True)
        
        except Exception as e:
            print(e)
            self.after(0, self.update_ui, "The threads of fate have snapped. This error exceeds the boundaries of this world's logic.", "Error", "", True)
        
        finally:
            self.after(self.UPDATE_INTERVAL_MS, self.fetch_quote)

    def update_ui(self, quote: str, character: str, anime: str, error: bool = False):
        """Updates the quote in the screen."""
        foreground_color = QuotePageStyle.QuoteLabelStateColor["success_color"]
        if error:
            foreground_color = QuotePageStyle.QuoteLabelStateColor["error_color"]

        self.quote_label.config(text=quote, foreground=foreground_color)
        self.char_label.config(text=f"{character} {anime}")
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
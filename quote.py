import ttkbootstrap as ttk
import requests
import threading
import time

QUOTE_API_URL = "https://api.animechan.io/v1/quotes/random"
UPDATE_INTERVAL_MS = 300000 # 5 minutes

class QuotePage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        # --- Create UI Elements ---
        self.title_label = ttk.Label(self, text="Quote of the Moment", 
                                    font="Helvetica 18 bold", 
                                    bootstyle="primary")
        self.title_label.pack(side="top", pady=10, padx=20)

        center_frame = ttk.Frame(self)
        center_frame.pack(fill="both", expand=True)

        # 'wraplength' is still important for long quotes
        self.quote_label = ttk.Label(center_frame, text="Loading quote...", 
                                      font="Helvetica 16 bold italic", 
                                      bootstyle="inverse-dark",
                                      wraplength=750,
                                      anchor="center")
        self.quote_label.pack(side="top", pady=(20, 10), padx=20)
        
        # 'bootstyle="secondary"' for the muted/gray text
        self.char_label = ttk.Label(center_frame, text="", 
                                      font="Helvetica 12", 
                                      bootstyle="secondary",
                                      anchor="center")
        self.char_label.pack(side="top", pady=(0, 20), padx=20)

        self.last_updated_label = ttk.Label(self, text="Last updated: Never",
                                           font="Helvetica 8",
                                           bootstyle="secondary")
        self.last_updated_label.pack(side="bottom", pady=5)
        
        # --- Start the update loop ---
        self.start_quote_update()

    def start_quote_update(self):
        threading.Thread(target=self.fetch_quote, daemon=True).start()

    def fetch_quote(self):
        try:
            response = requests.get(QUOTE_API_URL, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            print(data)
            data = data['data']

            quote = f"\"{data['content']}\""
            character = f"- {data['character']['name']}"
            anime = f"({data['anime']['name']})"
            
            self.after(0, self.update_ui, quote, character, anime)

        except requests.exceptions.RequestException as e :
            print(e)
            self.after(0, self.update_ui, "Error: Could not fetch quote.", "", "", "danger")
        
        except Exception as e:
            self.after(0, self.update_ui, f"An error occurred: {e}", "", "", "danger")
        
        finally:
            # This is the 5-minute scheduler
            self.after(UPDATE_INTERVAL_MS, self.start_quote_update)

    def update_ui(self, quote, character, anime, style="inverse-dark"):
        self.quote_label.config(text=quote, bootstyle=style)
        self.char_label.config(text=f"{character} {anime}")
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
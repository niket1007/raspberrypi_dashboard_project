import tkinter as tk
import requests
import threading
import time

# API endpoint from your original project's README
QUOTE_API_URL = "https://api.animechan.io/v1/quotes/random"

# 5 minutes in milliseconds (5 * 60 * 1000)
UPDATE_INTERVAL_MS = 300000 

class QuotePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller

        # --- Create UI Elements ---
        self.title_label = tk.Label(self, text="Quote of the Moment", 
                                    font=controller.title_font, 
                                    bg="black", fg="white")
        self.title_label.pack(side="top", pady=10, padx=20)

        # Main frame to center the quote
        center_frame = tk.Frame(self, bg="black")
        center_frame.pack(fill="both", expand=True)

        self.quote_label = tk.Label(center_frame, text="Loading quote...", 
                                      font=controller.quote_font, 
                                      bg="black", fg="white",
                                      wraplength=750) # Wrap text at 750px
        self.quote_label.pack(side="top", pady=(20, 10), padx=20)
        
        self.char_label = tk.Label(center_frame, text="", 
                                      font=controller.quote_char_font, 
                                      bg="black", fg="gray")
        self.char_label.pack(side="top", pady=(0, 20), padx=20)

        self.last_updated_label = tk.Label(self, text="Last updated: Never",
                                           font=("Helvetica", 8),
                                           bg="black", fg="gray")
        self.last_updated_label.pack(side="bottom", pady=5)
        
        # --- Start the update loop ---
        self.start_quote_update()

    def start_quote_update(self):
        # Run the 'fetch_quote' function in a new thread
        threading.Thread(target=self.fetch_quote, daemon=True).start()

    def fetch_quote(self):
        # This is the 'blocking' function that runs in the background
        try:
            response = requests.get(QUOTE_API_URL, timeout=10)
            response.raise_for_status() # Raise an error for bad responses
            
            data = response.json()
            data = data["data"]
            # Extract data from animechan.io
            quote = f"\"{data['content']}\""
            character = f"- {data['character']['name']}"
            anime = f"({data['anime']['name']})"
            
            # Schedule the UI update on the main thread
            self.after(0, self.update_ui, quote, character, anime)

        except requests.exceptions.RequestException:
            # Handle network errors
            self.after(0, self.update_ui, "Error: Could not fetch quote.", "", "")
        
        except Exception as e:
            # Handle other errors (like JSON parsing)
            self.after(0, self.update_ui, f"An error occurred: {e}", "", "")
        
        finally:
            # --- THIS IS THE SCHEDULER ---
            # After the function finishes (or fails),
            # schedule this function to run again in 5 minutes.
            self.after(UPDATE_INTERVAL_MS, self.start_quote_update)

    def update_ui(self, quote, character, anime):
        # This function is guaranteed to run on the main thread
        self.quote_label.config(text=quote)
        self.char_label.config(text=f"{character} {anime}")
        self.last_updated_label.config(text=f"Last updated: {time.strftime('%I:%M:%S %p')}")
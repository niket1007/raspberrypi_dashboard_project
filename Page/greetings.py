import tkinter as tk
import time
import datetime

class GreetingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Home"

        # --- Create a Split Layout ---
        left_frame = tk.Frame(self)
        left_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

        self.time_label = tk.Label(left_frame, 
                                    font=("Helvetica", 55, "bold"))
        self.time_label.pack(side="top", expand=True, anchor="center")
        
        self.date_label = tk.Label(left_frame, 
                                    font=("Helvetica", 18, "bold"))
        self.date_label.pack(side="top", expand=True, anchor="center")

        self.greeting_label = tk.Label(left_frame, 
                                    font=("Helvetica", 18, "bold"))
        self.greeting_label.pack(side="top", expand=True, anchor="center")

        # --- Start the update loop ---
        self.update_time_and_greeting()

    def get_greeting(self):
        """Returns a time-appropriate greeting."""
        current_hour = datetime.datetime.now().hour
        
        if 5 <= current_hour < 12:
            return "Good morning!"
        elif 12 <= current_hour < 18:
            return "Good afternoon!"
        else:
            return "Good evening!"

    def update_time_and_greeting(self):
        """Updates the time, date, and greeting labels every second."""
        
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%A, %B %d, %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        # Fixed: Uses the dynamic greeting function instead of hardcoded text
        self.greeting_label.config(text=self.get_greeting())
        
        self.after(1000, self.update_time_and_greeting)
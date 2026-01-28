import tkinter as tk
import time
import datetime
from Services.Style import GreetingsPageStyle

class GreetingsPage(tk.Frame):

    DATETIME_UPDATE_TIMER = 1000

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "" # Kept empty for styling

        self.configure(bg=GreetingsPageStyle.RETRO_BG)
        
        # --- Create a Split Layout ---
        greeting_frame = tk.Frame(self, bg=GreetingsPageStyle.RETRO_BG)
        greeting_frame.pack(**GreetingsPageStyle.MainFrame)

        self.time_label = tk.Label(self, **GreetingsPageStyle.TimeLabel)
        self.time_label.pack(**GreetingsPageStyle.TimeLabelPack)
        
        self.date_label = tk.Label(self, **GreetingsPageStyle.DateLabel)
        self.date_label.pack(**GreetingsPageStyle.DateAndGreetingPack)

        self.greeting_label = tk.Label(greeting_frame, **GreetingsPageStyle.GreetingLabel)
        self.greeting_label.pack(**GreetingsPageStyle.DateAndGreetingPack)

        # --- Start the update loop ---
        self.update_time_and_greeting()

    def get_greeting(self):
        current_hour = datetime.datetime.now().hour
        
        if 5 <= current_hour < 12:
            return "Good Morning!"
        elif 12 <= current_hour < 18:
            return "Good Afternoon!"
        else:
            return "Good Evening!"

    def update_time_and_greeting(self):
        
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%A, %B %d, %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.greeting_label.config(text=self.get_greeting())
        
        self.after(self.DATETIME_UPDATE_TIMER, self.update_time_and_greeting)

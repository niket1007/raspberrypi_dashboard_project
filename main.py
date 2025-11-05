import tkinter as tk
from tkinter import font  # Used for styling

# Import your page modules
from weather import WeatherPage
from quote import QuotePage
# from todo_page import TodoPage

class DashboardApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # --- Basic Window Setup ---
        self.title("Raspberry Pi Dashboard")
        self.geometry("408x320")  # Set to your screen size
        # self.attributes("-fullscreen", True) # Uncomment for fullscreen on Pi
        self.configure(bg="black")

        # --- Font Styles ---
        self.title_font = font.Font(family='Helvetica', size=18, weight="bold")
        self.body_font = font.Font(family='Helvetica', size=12)
        self.quote_font = font.Font(family='Helvetica', size=14, weight="bold", slant="italic")
        self.quote_char_font = font.Font(family='Helvetica', size=12)

        # --- Main Container for Pages ---
        container = tk.Frame(self, bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --- Navigation Bar ---
        nav_frame = tk.Frame(self, bg="gray20")
        nav_frame.pack(side="bottom", fill="x")

        # --- Page Dictionary ---
        self.frames = {}

        # --- Instantiate and Add Pages ---
        # Add all your page classes here
        for PageClass in (GreetingsPage, WeatherPage, QuotePage): # Added QuotePage
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # --- Add Navigation Buttons ---
        btn_greeting = tk.Button(nav_frame, text="Home", 
                                 command=lambda: self.show_frame("GreetingsPage"))
        btn_weather = tk.Button(nav_frame, text="Weather", 
                                command=lambda: self.show_frame("WeatherPage"))
        btn_quote = tk.Button(nav_frame, text="Quote", 
                                command=lambda: self.show_frame("QuotePage"))
        
        btn_greeting.pack(side="left", fill="x", expand=True)
        btn_weather.pack(side="left", fill="x", expand=True)
        btn_quote.pack(side="left", fill="x", expand=True)


        # --- Show the first page ---
        self.show_frame("GreetingsPage")

    def show_frame(self, page_name):
        # Bring the requested frame to the front
        frame = self.frames[page_name]
        frame.tkraise()

# --- A simple "Home" page to start ---
class GreetingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="black")
        self.controller = controller
        
        label = tk.Label(self, text="Welcome to your Dashboard!",
                         font=controller.title_font, 
                         bg="black", fg="white")
        label.pack(side="top", fill="both", expand=True)


# --- Main entry point ---
if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
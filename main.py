import ttkbootstrap as ttk
# We no longer need the 'font' module, ttkbootstrap handles it.

# Import your page modules
from weather import WeatherPage
from quote import QuotePage
# from todo_page import TodoPage

class DashboardApp(ttk.Window):
    def __init__(self, *args, **kwargs):
        # Initialize the ttk.Window
        # We set a theme here. "darkly" is a great-looking dark theme.
        # Other options: "cyborg", "superhero", "vapor", "litera" (light)
        super().__init__(*args, **kwargs, themename="darkly")

        # --- Basic Window Setup ---
        self.title("Raspberry Pi Dashboard")
        self.geometry("480x320")  # Set to your screen size
        # self.attributes("-fullscreen", True) # Uncomment for fullscreen on Pi

        # --- Main Container for Pages ---
        container = ttk.Frame(self, bootstyle="dark")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --- Navigation Bar ---
        # Using "secondary" bootstyle for a different color
        nav_frame = ttk.Frame(self, bootstyle="secondary")
        nav_frame.pack(side="bottom", fill="x")

        # --- Page Dictionary ---
        self.frames = {}

        # --- Instantiate and Add Pages ---
        for PageClass in (GreetingsPage, WeatherPage, QuotePage):
            page_name = PageClass.__name__
            frame = PageClass(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # --- Add Navigation Buttons ---
        # 'bootstyle="primary"' makes them the main accent color
        btn_greeting = ttk.Button(nav_frame, text="Home", 
                                  bootstyle="primary",
                                  command=lambda: self.show_frame("GreetingsPage"))
        btn_weather = ttk.Button(nav_frame, text="Weather", 
                                 bootstyle="primary",
                                 command=lambda: self.show_frame("WeatherPage"))
        btn_quote = ttk.Button(nav_frame, text="Quote", 
                                bootstyle="primary",
                                command=lambda: self.show_frame("QuotePage"))
        
        # We use 'fill' and 'expand' to make buttons equal width
        btn_greeting.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        btn_weather.pack(side="left", fill="x", expand=True, padx=2, pady=2)
        btn_quote.pack(side="left", fill="x", expand=True, padx=2, pady=2)

        # --- Show the first page ---
        self.show_frame("GreetingsPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

# --- A simple "Home" page to start ---
class GreetingsPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        
        # 'bootstyle="inverse-dark"' makes the text white on a dark bg
        # 'font="Helvetica 24 bold"' is an easier way to set font
        label = ttk.Label(self, text="Welcome to your Dashboard!",
                         font="Helvetica 24 bold", 
                         bootstyle="inverse-dark")
        label.pack(side="top", fill="both", expand=True, padx=20, pady=20)


# --- Main entry point ---
if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
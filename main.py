import tkinter as tk
from tkinter import ttk

# Import all our page modules
from Page.greetings import GreetingsPage
from Page.weather import WeatherPage
# from quote import QuotePage

class DashboardApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # --- Basic Window Setup ---
        self.title("Raspberry Pi Dashboard")
        self.geometry("480x320")
        # self.attributes("-fullscreen", True) 

        # --- Main Container for Pages ---
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --- Navigation Bar ---
        nav_frame = ttk.Frame(self)
        nav_frame.pack(side="bottom", fill="x")

        # --- Page Dictionary & List ---
        self.frames = {
            0: GreetingsPage,
            1: WeatherPage
            # 2: QuotePage,
        }
        self.page_list = [] # To keep track of the order
        self.current_page_index = 0

        # --- Instantiate and Add Pages ---
        # Add QuotePage to this tuple if you uncomment the import
        for index in self.frames:
            frame = self.frames[index](parent=container, controller=self)
            
            self.frames[index] = frame
            
            frame.grid(row=0, column=0, sticky="nsew")

        # --- Add Navigation Buttons (Next / Prev) ---
        # We use a single function 'switch_page' with a direction parameter
        btn_prev = ttk.Button(nav_frame, text="<< Prev", 
                              command=lambda: self.switch_page(-1))
        
        btn_next = ttk.Button(nav_frame, text="Next >>", 
                              command=lambda: self.switch_page(1))
        
        self.page_label = ttk.Label(nav_frame, text=self.frames[0].widgetName, 
                               border=2, borderwidth=2, relief="solid", 
                               font=("Helvetica", 10, "bold"), justify="center", background="white")
        btn_prev.pack(side="left", fill="x", expand=True, padx=0, pady=2, ipady=5)
        self.page_label.pack(side="left", fill="x", expand=True, padx=0, pady=2, ipady=5)
        btn_next.pack(side="left", fill="x", expand=True, padx=0, pady=2, ipady=5)

        # --- Show the first page ---
        self.show_frame(self.frames[0])

    def show_frame(self, page_frame: ttk.Frame):
        """Brings the specified frame to the front."""
        frame = page_frame
        frame.tkraise()

    def switch_page(self, delta):
        """
        Moves to the next or previous page.
        delta = 1 for Next, -1 for Prev
        """
        # Calculate new index with wrap-around (modulo operator)
        new_index = (self.current_page_index + delta) % len(self.frames)
        
        # Get the name of the new page
        page_frame = self.frames[new_index]
        self.current_page_index = new_index
        self.page_label.config(text=page_frame.widgetName)
        # Show it
        self.show_frame(page_frame)

# --- Main entry point ---
if __name__ == "__main__":
    app = DashboardApp()
    # app.config(cursor="none")
    app.mainloop()
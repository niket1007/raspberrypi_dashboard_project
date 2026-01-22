import tkinter as tk
from decouple import config
import importlib
import threading

# Import our page modules
from Page.greetings import GreetingsPage

from Services.Style import MainPageStyle
from Services.Redis.redis import RedisStorage
from Services.Redis.redis_sub import RedisSub

class DashboardApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis = RedisStorage()
        _ = RedisSub()
        
        # --- Basic Window Setup ---
        self.title(MainPageStyle.Title)
        self.geometry(MainPageStyle.Geometry)
        if config("app_platform", "windows") == "windows":
            self.attributes("-fullscreen", False)
        else:
            self.attributes("-fullscreen", True)
            self.config(cursor="none")

        # --- Navigation Bar ---
        nav_frame = tk.Frame(self)
        nav_frame.pack(**MainPageStyle.NavFramePack)

        # --- Main Container for Pages ---
        container = tk.Frame(self)
        container.pack(**MainPageStyle.MainContainerPack)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # --- Page Dictionary & List ---
        self.page_list = self.__get_page_lists()
        self.current_page_index = 0

        # --- Instantiate Pages ---
        for index in range(len(self.page_list)):
            frame = self.page_list[index](parent=container, controller=self)
            
            self.page_list[index] = frame
            
            frame.grid(**MainPageStyle.EachPageFrameGrid)

        # --- Add Navigation Buttons (Next / Prev) ---
        btn_prev = tk.Button(nav_frame, text="<< Prev", 
                              command=lambda: self.switch_page(-1))
        
        btn_next = tk.Button(nav_frame, text="Next >>", 
                              command=lambda: self.switch_page(1))
        
        self.page_label = tk.Label(nav_frame, text=self.page_list[0].widgetName, 
                                   **MainPageStyle.ScreenInfoLabel)
        
        btn_prev.pack(**MainPageStyle.ButtonPack)
        self.page_label.pack(**MainPageStyle.ScreenInfoLabelPack)
        btn_next.pack(**MainPageStyle.ButtonPack)
        
        # --- Show the first page ---
        self.show_frame(self.page_list[0])
        self.setup_hardware_buttons()

    def __get_page_lists(self) -> list:
        pages = [GreetingsPage]
        screens = self.redis.get_screen_configuration()

        for screen in screens:
            if screen["visibility"]:
                module_name = f"Page.{screen["name"].lower()}"
                class_name = f"{screen["name"].capitalize()}Page"
                module = importlib.import_module(module_name)
                page_class = getattr(module, class_name)
                pages.append(page_class)
        return pages

    def show_frame(self, page_frame: tk.Frame):
        """Brings the specified frame to the front."""
        page_frame.tkraise()

    def switch_page(self, delta):
        """
        Moves to the next or previous page.
        delta = 1 for Next, -1 for Prev
        """
        new_index = (self.current_page_index + delta) % len(self.page_list)
        
        page_frame = self.page_list[new_index]
        self.current_page_index = new_index
        self.page_label.config(text=page_frame.widgetName)

        self.show_frame(page_frame)
    
    def setup_hardware_buttons(self):
        env = config("app_platform", "windows")
        if env == "raspberrypi":
            try:
                from gpiozero import Button
                # Store buttons as instance attributes so they aren't garbage collected
                self.btn_prev = Button(18, bounce_time=0.1)
                self.btn_next = Button(24, bounce_time=0.1)
                
                # Link buttons directly to your existing switch_page method
                # Using lambda to ensure the call happens on press
                self.btn_prev.when_pressed = lambda: self.switch_page(-1)
                self.btn_next.when_pressed = lambda: self.switch_page(1)
                
                print("Hardware buttons initialized.")
            except Exception as e:
                print(f"GPIO Error: {e}")

        
# --- Main entry point ---
if __name__ == "__main__":
    threading.Thread(target=setup_buttons, daemon=True).start()
    app = DashboardApp()
    app.mainloop()
    
import tkinter as tk
from tkinter import ttk
import calendar
import datetime
import holidays

class CalendarPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.widgetName = "Calendar"
        self.config(cursor="none")

        # --- Mock Data (Replacing Storage.Cache) ---
        # In your real app, you would fetch this from your data source
        self.user_events = {
            "15": "Doctor Appointment", 
            "25": "Project Deadline"
        }

        # --- UI Layout ---
        # 1. Top: Month and Year Label
        self.month_label = ttk.Label(self, text="Loading...", font=("Helvetica", 9, "bold"))
        self.month_label.pack(pady=(5, 10))

        # 2. Middle: Calendar Grid Container
        self.calendar_frame = ttk.Frame(self)
        self.calendar_frame.config(cursor="none")
        self.calendar_frame.pack(expand=True, fill="both", padx=20)

        # 3. Bottom: Info Label (equivalent to holiday_info_label)
        self.info_label = ttk.Label(self, text="Tap a date for info", 
                                    font=("Helvetica", 10), 
                                    foreground="gray")
        self.info_label.pack(pady=5)

        # --- Draw Weekday Headers ---
        days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        for col, day in enumerate(days):
            lbl = ttk.Label(self.calendar_frame, text=day, font=("Helvetica", 8, "bold"))
            lbl.grid(row=0, column=col, sticky="nsew", padx=20)
            self.calendar_frame.grid_columnconfigure(col, weight=1)

        # --- Populate Data ---
        self.populate_calendar()

    def populate_calendar(self):
        today = datetime.date.today()
        year = today.year
        month = today.month

        # 1. Update Header
        self.month_label.config(text=today.strftime("%B %Y")) # e.g., "November 2025"

        # 2. Fetch Holidays (India - as per your Kivy code)
        holidays_dict = {}
        if holidays:
            try:
                # Fetching holidays for IN (India)
                holidays_dict = holidays.country_holidays('IN', years=year)
            except Exception as e:
                print(f"Error loading holidays: {e}")

        # 3. Clear old date buttons if re-populating
        for widget in self.calendar_frame.grid_slaves():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        # 4. Generate Month Matrix
        # Returns a list of weeks, where each day is a number (0 = day belongs to other month)
        cal = calendar.monthcalendar(year, month)

        # 5. Draw Buttons for Dates
        for r, week in enumerate(cal):
            for c, day in enumerate(week):
                if day == 0:
                    continue # Skip empty slots

                calc_date = datetime.date(year, month, day)
                
                # --- Logic Checks (Ported from CalendarScreen.py) ---
                is_today = (calc_date == today)
                is_holiday = calc_date in holidays_dict
                is_user_event = str(day) in self.user_events
                
                holiday_text = holidays_dict.get(calc_date, "")
                user_text = self.user_events.get(str(day), "")

                # --- Styling Logic ---
                bg_color = "#f0f0f0" # Default gray/white
                fg_color = "black"
                font_style = ("Helvetica", 8)

                # Priority: Today > Holiday/Event
                if is_today and (is_holiday or is_user_event):
                    bg_color = "#007bff"
                    fg_color = "red"  
                    font_style = ("Helvetica", 11, "bold")
                elif is_today:
                    bg_color = "#007bff" # Blue background for "Today"
                    fg_color = "white"   
                    font_style = ("Helvetica", 11, "bold")
                elif is_holiday or is_user_event:
                    if not is_today:
                        fg_color = "red" # Red text for holidays not on today
                        font_style = ("Helvetica", 11, "bold")
                    # If it IS today, we keep white text on blue bg

                # We use standard tk.Button (not ttk) because ttk makes changing 
                # specific background colors per-button difficult.
                btn = tk.Button(self.calendar_frame, 
                                text=str(day),
                                bg=bg_color,
                                fg=fg_color,
                                activebackground=bg_color,
                                activeforeground=fg_color,
                                font=font_style,
                                relief="flat",
                                borderwidth=0,
                                cursor="none",
                                # Pass data to the click handler using lambda defaults
                                command=lambda d=day, h=holiday_text, u=user_text: self.on_date_click(d, h, u))
                
                btn.grid(row=r+1, column=c, sticky="nsew", padx=2, pady=2, ipady=5)
                self.calendar_frame.grid_rowconfigure(r+1, weight=1)

    def on_date_click(self, day, holiday_text, user_text):
        """Updates the info label when a date is clicked."""
        info_parts = []
        if holiday_text:
            info_parts.append(f"Holiday({day}): {holiday_text}")
        if user_text:
            info_parts.append(f"Event({day}): {user_text}")
            
        if info_parts:
            self.info_label.config(text="; ".join(info_parts), foreground="red")
        else:
            # Default text if nothing special on that date
            self.info_label.config(text=f"Selected Date: {day}", foreground="black")
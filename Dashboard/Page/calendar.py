import tkinter as tk
import calendar
import datetime
import holidays
from decouple import config
from Services.Redis.redis import RedisStorage
from Services.Style import CalendarPageStyle

class CalendarPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.widgetName = "Calendar"

        self.redis = RedisStorage()
        self.user_events = self.redis.get_calendar_user_data()

        # --- UI Layout ---
        # 1. Top: Month and Year Label
        self.month_label = tk.Label(self, **CalendarPageStyle.MonthLabel)
        self.month_label.pack(**CalendarPageStyle.MonthLabelPack)

        # 2. Middle: Calendar Grid Container
        self.calendar_frame = tk.Frame(self)
        if config("app_platform", "windows") != "windows":
            self.calendar_frame.config(cursor="none")
        self.calendar_frame.pack(**CalendarPageStyle.CalendarFramePack)

        # 3. Bottom: Info Label
        self.info_label = tk.Label(self, **CalendarPageStyle.InfoLabel)
        self.info_label.pack(**CalendarPageStyle.InfoLabelPack)

        # --- Draw Weekday Headers ---
        days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        for col, day in enumerate(days):
            lbl = tk.Label(self.calendar_frame, text=day, **CalendarPageStyle.WeeekDayHeaderLabel)
            lbl.grid(row=0, column=col, **CalendarPageStyle.WeekDayHeaderLabelPack)
            self.calendar_frame.grid_columnconfigure(col, weight=1)

        # --- Populate Data ---
        self.populate_calendar()

    def populate_calendar(self):
        today = datetime.date.today()
        year = today.year
        month = today.month

        # 1. Update Header
        self.month_label.config(text=today.strftime("%B %Y")) # e.g., "November 2025"

        # 2. Fetch Holiday
        holidays_dict = {}
        if holidays:
            try:
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
                is_user_event = calc_date in self.user_events
                
                holiday_text = holidays_dict.get(calc_date, "")
                user_text = self.user_events.get(str(day), "")

                # --- Styling Logic ---
                bg_color = "#f0f0f0" # Default gray/white
                fg_color = "black"
                font_style = ("Helvetica", 8)

                if is_today and (is_holiday or is_user_event):
                    # Red foreground and blue background for today and holiday or user event
                    bg_color = "#007bff"
                    fg_color = "red"  
                    font_style = ("Helvetica", 11, "bold")
                elif is_today:
                    # Blue background for today and no holdiday or user event
                    bg_color = "#007bff" 
                    fg_color = "white" 
                    font_style = ("Helvetica", 11, "bold")
                elif (is_holiday or is_user_event) and not is_today:
                    # White background and red foreground for holiday or user event but not today
                    fg_color = "red"
                    font_style = ("Helvetica", 11, "bold")
                
                # Specific background colors per-button.
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
                                command=lambda d=day, h=holiday_text, u=user_text: self.on_date_click(d, h, u))
                
                btn.grid(row=r+1, column=c, sticky="nsew", padx=2, pady=2, ipady=5)
                self.calendar_frame.grid_rowconfigure(r+1, weight=1)

    def on_date_click(self, day, holiday_text, user_text):
        """Updates the info label when a date is clicked."""
        info_parts = []
        if holiday_text:
            info_parts.append(f"{holiday_text}")
        if user_text:
            info_parts.append(f"{user_text}")
        
        if info_parts:
            text = f'Event {day}: {", ".join(info_parts)}'
            self.info_label.config(text=text, foreground="red")
        else:
            self.info_label.config(text=f"Selected Date: {day}", foreground="black")
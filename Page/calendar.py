import tkinter as tk
import calendar
import datetime
import holidays
from decouple import config
from Services.Redis.redis import RedisStorage
from Services.Style import CalendarPageStyle, MainPageStyle

class CalendarPage(tk.Frame):

    UPDATE_INTERVAL = config("calendar_update_frequency", cast=int)

    def __init__(self, parent, controller):
        super().__init__(parent, bg=MainPageStyle.BackgroundColor)
        self.controller = controller
        self.widgetName = "Calendar"

        self.redis = RedisStorage()

        # --- UI Layout ---
        # 1. Top: Month and Year Label
        self.month_label = tk.Label(self, **CalendarPageStyle.MonthLabel)
        self.month_label.pack(**CalendarPageStyle.MonthLabelPack)

        # 2. Middle: Calendar Grid Container
        self.calendar_frame = tk.Frame(self, bg=MainPageStyle.BackgroundColor)
        if config("app_platform", "windows") != "windows":
            self.calendar_frame.config(cursor="none")
        self.calendar_frame.pack(**CalendarPageStyle.CalendarFramePack)

        # 3. Bottom: Info Label
        self.info_label = tk.Label(self, **CalendarPageStyle.InfoLabel)
        self.info_label.pack(**CalendarPageStyle.InfoLabelPack)

        # --- Draw Weekday Headers ---
        days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
        for col, day in enumerate(days):
            lbl = tk.Label(self.calendar_frame, text=day, **CalendarPageStyle.WeekDayHeaderLabel)
            lbl.grid(row=0, column=col, **CalendarPageStyle.WeekDayHeaderLabelPack)
            self.calendar_frame.grid_columnconfigure(col, weight=1)

        # --- Populate Data ---
        self.populate_calendar()

    def populate_calendar(self):
        today = datetime.date.today()
        year = today.year
        month = today.month
        self.user_events = self.redis.get_calendar_user_data()

        # 1. Update Header (Cyberpunk style)
        self.month_label.config(text=today.strftime("%B %Y").upper())

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
        cal = calendar.monthcalendar(year, month)

        # 5. Draw Buttons for Dates
        for r, week in enumerate(cal):
            for c, day in enumerate(week):
                if day == 0:
                    continue # Skip empty slots

                calc_date = datetime.date(year, month, day)

                # --- Logic Checks ---
                is_today = (calc_date == today)
                is_holiday = calc_date in holidays_dict
                is_user_event = str(calc_date) in self.user_events
                
                holiday_text = holidays_dict.get(calc_date, "")
                user_text = self.user_events.get(str(calc_date), "")

                # --- Cyberpunk Styling Logic ---
                bg_color = "#1a1a2e"  # Default dark grid
                fg_color = "#a0a0ff"  # Dimmed text
                font_style = ("Courier New", 8)

                if is_today and (is_holiday or is_user_event):
                    # Cyan background with magenta text for today + event
                    bg_color = "#00f2ff"
                    fg_color = "#ff00ff"  
                    font_style = ("Orbitron", 9, "bold")
                elif is_today:
                    # Cyan background for today
                    bg_color = "#00f2ff" 
                    fg_color = "#0a0a0a" 
                    font_style = ("Orbitron", 9, "bold")
                elif (is_holiday or is_user_event) and not is_today:
                    # Magenta text for holidays/events
                    fg_color = "#ff00ff"
                    font_style = ("Courier New", 9, "bold")
                
                btn = tk.Button(self.calendar_frame, 
                                text=str(day),
                                bg=bg_color,
                                fg=fg_color,
                                activebackground=bg_color,
                                activeforeground=fg_color,
                                font=font_style,
                                relief="flat",
                                borderwidth=1,
                                cursor="none",
                                command=lambda d=day, h=holiday_text, u=user_text: self.on_date_click(d, h, u))
                
                btn.grid(row=r+1, column=c, sticky="nsew", padx=1, pady=1, ipady=2)
                self.calendar_frame.grid_rowconfigure(r+1, weight=1)

        self.after(self.UPDATE_INTERVAL, self.populate_calendar)

    def on_date_click(self, day, holiday_text, user_text):
        """Updates the info label when a date is clicked."""
        info_parts = []
        if holiday_text:
            info_parts.append(f"{holiday_text}")
        if user_text:
            info_parts.append(f"{user_text}")
        
        if info_parts:
            text = f'▶ EVENT {day}: {", ".join(info_parts)}'.upper()
            self.info_label.config(text=text, foreground="#ff00ff")
            if len(text) > 30:
                self.info_label.config(**CalendarPageStyle.InfoLabelSmallFont)
        else:
            self.info_label.config(text=f"▶ DATE: {day}", foreground="#a0a0ff")

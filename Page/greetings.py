import tkinter as tk
import time
import datetime
import holidays

from Services.Style import GreetingsPageStyle
from Services.Redis.redis import RedisStorage

class GreetingsPage(tk.Frame):

    DATETIME_UPDATE_TIMER = 1000
    COUNT_UPDATE_TIMER = 10000

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "" # Kept empty for styling
        self._redis = RedisStorage()

        self.configure(bg=GreetingsPageStyle.RETRO_BG)
        
        # --- Create a Split Layout ---
        greeting_frame = tk.Frame(self, bg=GreetingsPageStyle.RETRO_BG)
        greeting_frame.pack(**GreetingsPageStyle.MainFrame)

        meeting_event_frame = tk.Frame(self, bg=GreetingsPageStyle.RETRO_BG)
        meeting_event_frame.pack(**GreetingsPageStyle.MainFrame)

        self.time_label = tk.Label(greeting_frame, **GreetingsPageStyle.TimeLabel)
        self.time_label.pack(**GreetingsPageStyle.TimeLabelPack, ipady=0)
        
        self.date_label = tk.Label(greeting_frame, **GreetingsPageStyle.DateLabel)
        self.date_label.pack(**GreetingsPageStyle.DateAndCountPack, ipady=0)

        self.meeting_and_event_label = tk.Label(meeting_event_frame, **GreetingsPageStyle.CountLabel)
        self.meeting_and_event_label.pack(**GreetingsPageStyle.DateAndCountPack)

        # --- Start the update loop ---
        self.update_time_and_greeting()
        self.update_meeting_and_event_count()

    def update_meeting_and_event_count(self):
        today = datetime.date.today()
        year = today.year
        user_events = self._redis.get_calendar_user_data()
        holidays_dict = holidays.country_holidays('IN', years=year)
        meetings = self._redis.get_meetings_data()
        meetings_count, holidays_count, user_events_count = 0, 0, 0

        if meetings is not None:
            meetings_count = 0
            for meeting in meetings.split("\n"):
                if str(today) in meeting:
                    meetings_count += 1
        if holidays_dict is not None:
            holidays_count =  len(holidays_dict.get(today, {}))
        if user_events is not None:
            user_events_count =  len(user_events.get(str(today), {}))
        
        text = f"> DAILY_BRIEFING_INITIATED\n> TOTAL_EVENTS: {user_events_count + holidays_count}\n> ACTIVE_MEETINGS: {meetings_count}"
        self.meeting_and_event_label.config(text=text)

        self.after(self.COUNT_UPDATE_TIMER, self.update_meeting_and_event_count)

    def update_time_and_greeting(self):
        
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%A, %B %d, %Y")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        
        self.after(self.DATETIME_UPDATE_TIMER, self.update_time_and_greeting)

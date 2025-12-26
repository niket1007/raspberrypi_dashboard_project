import tkinter as tk
from decouple import config
from Services.Redis.redis import RedisStorage
from Services.Style import MeetingPageStyle

class MeetingsPage(tk.Frame):

    UPDATE_INTERVAL = config("meetings_redis_frequency", cast=int)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Meetings"
        self.redis = RedisStorage()

        # --- Meetings List Content ---
        self.meeting_label = tk.Label(self,**MeetingPageStyle.MeetingLabel)
        self.meeting_label.pack(**MeetingPageStyle.MeetingLabelPack)

        self.load_meetings()

    def load_meetings(self):
        meeting_texts = self.redis.get_meetings_data()
        self.meeting_label.config(text=meeting_texts)

        self.after(self.UPDATE_INTERVAL, self.load_meetings)
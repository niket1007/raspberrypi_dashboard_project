import tkinter as tk
from Services.Redis.redis import RedisStorage
from Services.Style import MeetingPageStyle

class MeetingsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.widgetName = "Meetings"
        self.redis = RedisStorage()

        # --- Todo List Content ---
        self.meeting_label = tk.Label(self,**MeetingPageStyle.MeetingLabel)
        self.meeting_label.pack(**MeetingPageStyle.MeetingLabelPack)

        self.load_meetings()

    def load_meetings(self):
        meeting_texts = self.redis.get_meetings_data()
        self.meeting_label.config(text=meeting_texts)
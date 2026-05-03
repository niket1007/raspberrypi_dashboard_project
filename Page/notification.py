import tkinter as tk
import time
import json
from decouple import config
from Services.Style import NotificationStyle


class NotificationOverlay(tk.Frame):

    DISPLAY_DURATION = config("notification_screen_live", cast=int)
    SKIP_APP = ["Automate", "Myntra", "Moto Actions & Gestures", "Phone"]

    def __init__(self, parent, controller):
        super().__init__(parent,  **NotificationStyle.CardBorder)
        self.controller = controller
        self._timer = None

        # --- Header Row: tag label + timestamp ---
        header_row = tk.Frame(self, bg=NotificationStyle.CardBorder["bg"])
        header_row.pack(fill="x", padx=10, pady=(8, 2))

        self.tag_label = tk.Label(header_row, text="NOTIF", **NotificationStyle.TagLabel)
        self.tag_label.pack(side="left")

        self.time_label = tk.Label(header_row, text="", **NotificationStyle.TimeLabel)
        self.time_label.pack(side="right")

        # --- Title Row ---
        self.title_label = tk.Label(self, text="", **NotificationStyle.TitleLabel)
        self.title_label.pack(fill="x", padx=10, pady=(0, 2))

        # --- Body Row ---
        self.body_label = tk.Label(self, text="", **NotificationStyle.BodyLabel)
        self.body_label.pack(fill="x", padx=10, pady=(0, 8))

    def show(self, raw_data: str):
        display_text = self._get_message(raw_data)
        if display_text == "skip":
            return

        tag, title, body = display_text
        tag_colors = NotificationStyle.TAG_COLORS.get(tag, NotificationStyle.TAG_COLORS["DEFAULT"])

        self.tag_label.config(text=tag, bg=tag_colors["bg"], fg=tag_colors["fg"])
        self.time_label.config(text=time.strftime("%H:%M:%S"))
        self.title_label.config(text=f"> {title}_")
        self.body_label.config(text=body)

        self.place(**NotificationStyle.FramePlace)
        self.tkraise()

        # Cancel previous auto-dismiss timer if a new notification arrives
        if self._timer is not None:
            self.after_cancel(self._timer)

        self._timer = self.after(self.DISPLAY_DURATION, self.hide)

    def hide(self):
        self.place_forget()
        self._timer = None
    
    def _get_message(self, data):
        data = json.loads(data)

        msg_type = data.get("type", None)
        if data.get("type") == "batterystat":
            # Payload: {"type": "batterystat", "percentage": 76}
            percentage = data.get("percentage")
            return "BATT", "BATTERY_STATUS", f"LEVEL: {percentage}"
        if msg_type == "batterycharge":
            # Payload when charger plugged in: {"type": "batterycharge", "power_source": 2}
            # Payload when charger plugged out: {"type": "batterycharge", "power_source": null}
            if data.get("power_source", None):
                return "BATT", "BATTERY_STATUS", f"SOURCE: Phone_Plugged_In"           
            else:
                return "BATT", "BATTERY_STATUS", f"SOURCE: Phone_Plugged_Out"
        if msg_type == "notif":
            # Payload: {"type": "notif", "display_name": "Moto Actions & Gestures", 
            # "title": "Overcharge protection is on", "ticker_text": null, 
            # "text": null, "package": "com.motorola.actions"}
            app_name = data.get("display_name")
            if app_name in self.SKIP_APP:
                return "skip"
            title = data.get("title")
            text = data.get("text")
            text =  text[:40] + "...." if len(text) > 40 and text is not None else text 
            ticker_text = data.get("ticker_text")

            if app_name == title:
                if ticker_text is None or ticker_text == "":
                    text = text
                else:
                    text = f"{ticker_text}\n{text}"
            else:
                if ticker_text is None or ticker_text == "":
                    text = f"{title}\n{text}"
                else:
                    text = f"{ticker_text}\n{text}"
            
            return "NOTIF", app_name, text
        elif msg_type == "outcall":
            # Payload: {"type": "outcall", "phone_number": "xxxxxxxxx", "name": "xxxxxxx"}
            name = data.get("name")
            if name is None or len(name) == 0:
                name = data.get("phone_number")
            return "OUTCALL", "OUTGOING_CALL", f"DIALING: {name}"
        elif msg_type == "incall":
            # Payload: {"type": "incall", "phone_number": "xxxxxxx", "name": "xxxxxxxx"}
            name = data.get("name")
            if name is None or len(name) == 0:
                name = data.get("phone_number")
            return "INCALL", "INCOMING_CALL", f"CALLER: {name}"
        return "skip"

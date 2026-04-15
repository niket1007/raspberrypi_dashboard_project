import tkinter as tk
import time
from decouple import config
from Services.Style import NotificationStyle
from Services.NotificationService import NotificationService


class NotificationOverlay(tk.Frame):

    DISPLAY_DURATION = config("notification_screen_live", cast=int)

    def __init__(self, parent, controller):
        super().__init__(parent,  **NotificationStyle.CardBorder)
        self.controller = controller
        self._notif_service = NotificationService()
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
        display_text = self._notif_service.get_message(raw_data)
        if display_text == "skip":
            return

        tag, title, body = self._parse(display_text)
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

    def _parse(self, text: str) -> tuple[str, str, str]:
        """Split display_text from NotificationService into (tag, title, body)."""
        lines = text.strip().split("\n")
        first = lines[0]

        if first.startswith("Incoming call"):
            caller = first.replace("Incoming call from ", "").replace("............", "").strip()
            return "INCALL", "INCOMING_CALL", f"CALLER: {caller}"

        if first.startswith("Calling"):
            callee = first.replace("Calling", "").replace("...........", "").strip()
            return "OUTCALL", "OUTGOING_CALL", f"DIALING: {callee}"

        if first.startswith("Phone Battery"):
            level = first.split(":")[1].strip()
            return "BATT", "BATTERY_STATUS", f"LEVEL: {level}"

        if first in ("Phone Plugged In", "Phone Plugged Out"):
            status = first.upper().replace(" ", "_")
            return "BATT", "BATTERY_STATUS", f"SOURCE: {status}"

        # Generic app notification — e.g. "Slack: message body"
        parts = first.split(":", 1)
        title = parts[0].strip().upper().replace(" ", "_")
        body = (parts[1].strip() if len(parts) > 1 else "")
        if len(lines) > 1:
            body += "\n" + "\n".join(lines[1:])
        return "NOTIF", title, body

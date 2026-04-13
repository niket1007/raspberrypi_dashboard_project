import json

class NotificationService():
    GMAIL = "Gmail"
    SKIP_APP = ["Automate", "Myntra", "Moto Actions & Gestures", "Phone"]
    CLOCK = "Clock"
    WHATSAPP = "WhatsApp"
    TEAMS = "Teams"

    def get_message(self, data: str) -> str:
        data = json.loads(data)

        msg_type = data.get("type", None)
        if data.get("type") == "batterystat":
            # Payload for batterystat
            # {"type": "batterystat", "percentage": 76}
            percentage = data.get("percentage")
            return f"Phone Battery: {percentage}"
        if msg_type == "batterycharge":
            # Payload for batterycharge
            # When charger plugged in: {"type": "batterycharge", "power_source": 2}
            # When charger plugged out: {"type": "batterycharge", "power_source": null}
            if data.get("power_source", None):
                return "Phone Plugged In"
            else:
                return "Phone Plugged Out"
        if msg_type == "notif":
            # Payload for notif
            # {"type": "notif", "display_name": "Moto Actions & Gestures", 
            # "title": "Overcharge protection is on", "ticker_text": null, 
            # "text": null, "package": "com.motorola.actions"}
            app_name = data.get("display_name")
            if app_name in self.SKIP_APP:
                return "skip"
            title = data.get("title")
            text = data.get("text")
            text =  text[:40] + "...." if len(text) > 40 else text 
            ticker_text = data.get("ticker_text")

            if app_name == title:
                if ticker_text is None or ticker_text == "":
                    return f"{app_name}\n{text}"
                else:
                    return f"{app_name}\n{ticker_text}\n{text}"
            else:
                if ticker_text is None or ticker_text == "":
                    return f"{app_name}: {title}\n{text}"
                else:
                    return f"{app_name}: {title}\n{ticker_text}\n{text}"
        elif msg_type == "outcall":
            # Payload for outcall
            # {"type": "outcall", "phone_number": "xxxxxxxxx", "name": "xxxxxxx"}
            name = data.get("name")
            return f"Calling {name}..........."
        elif msg_type == "incall":
            # Payload for incall
            # {"type": "incall", "phone_number": "xxxxxxx", "name": "xxxxxxxx"}
            name = data.get("name")
            if name is None or name == "":
                name = data.get("phone_number")
            return f"Incoming call from {name}............"
        return "skip"

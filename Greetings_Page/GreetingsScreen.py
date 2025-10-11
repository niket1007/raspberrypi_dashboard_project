from kivy.properties import StringProperty
from CustomScreen.customScreen import CustomScreen
from kivy.clock import Clock
from datetime import datetime
from Logger.Logger import log
from Static.Messages.messages import (GREETINGS_ON_ENTER_EVENT, GREETINGS_TEXT_UDPATE)

class GreetingsScreen(CustomScreen):
    date_text = StringProperty("DD-MM-YYYY")
    time_text = StringProperty("HH:MM:SS AM/PM")
    greeting_text = StringProperty("Welcome")

    update_datetime_event = None

    def on_enter(self, *args):
        log.debug(GREETINGS_ON_ENTER_EVENT)
        self.update_datetime()

        current_hour = datetime.now().hour
        if 5 <= current_hour < 12:
            self.greeting_text = "Good Morning"
        elif 12 <= current_hour < 17:
            self.greeting_text = "Good Afternoon"
        else:
            self.greeting_text = "Good Evening"

        log.debug(GREETINGS_TEXT_UDPATE.format(current_hour, self.greeting_text))
        self.update_datetime_event = Clock.schedule_interval(self.update_datetime, 1)
        return super().on_enter()
    
    def update_datetime(self, *args):
        curr = datetime.now()
        self.date_text = curr.strftime("%A, %B %d")
        self.time_text = curr.strftime("%I:%M:%S %p")


